// KEPT ALIVE thumbnails. usage: node thumb.mjs <thumb.json> <out_dir>
// thumb.json: {"image":"/abs/frame.jpg","pos":"60% 40%","zoom":135,
//   "A":{"big":"RAFT<br><s>SINKING</s>","tag":"ALASKA · NIGHT"},
//   "C":{"kicker":"2 MILES OFFSHORE","big":"HIS RAFT WAS <s>SINKING</s>"},
//   "ring":{"x":930,"y":420,"r":150,"color":"alarm"},   // optional ring; color "alarm" = red #E5383B (Format v2), default teal
//   "arrow":{"x1":700,"y1":160,"x2":880,"y2":330}}      // optional red arrow pointing at the key detail
// "B":{"kicker":"…","big":"4 MINUTES<br><em>TO LIVE</em>"} — text right, red underline; <em> = red word.
// Any variant may override image/pos/zoom/ring/arrow (different frame per variant for Test & Compare).
// Rules: 1–5 words, real frame from the video, nothing in bottom-right (duration badge), no injuries in close-up.
import fs from "fs"; import path from "path"; import { createRequire } from "module";
const require = createRequire(import.meta.url); const { chromium } = require("playwright");
const NM = path.resolve(path.dirname(new URL(import.meta.url).pathname), "node_modules");
const cfg = JSON.parse(fs.readFileSync(process.argv[2])); const out = process.argv[3]; fs.mkdirSync(out, { recursive: true });
const font = (f, file) => `@font-face{font-family:${f};src:url(data:font/woff2;base64,${fs.readFileSync(`${NM}/@fontsource/${file}`).toString("base64")})}`;
const IMGS = {}; const img = (f) => (IMGS[f] ??= `data:image/jpeg;base64,${fs.readFileSync(f).toString("base64")}`);
const C = { abyss: "#0A1214", foam: "#EEF2EF", signal: "#2BB3A3", flare: "#F2B33D", sonar: "#6CF29A", alarm: "#E5383B" };
const hi = (s) => s.replace(/<s>/g, `<span style="color:${C.signal}">`).replace(/<\/s>/g, "</span>");
const CSS = `${font("BC9", "saira-condensed/files/saira-condensed-latin-800-normal.woff2")}
${font("JBM", "martian-mono/files/martian-mono-latin-500-normal.woff2")}
*{margin:0;padding:0;box-sizing:border-box}
.t{position:relative;width:1280px;height:720px;overflow:hidden;background:${C.abyss};color:${C.foam}}
.ph{position:absolute;inset:0;filter:contrast(1.08) saturate(1.12)}
.big{font-family:BC9;line-height:.88;text-transform:uppercase;text-shadow:0 5px 0 rgba(0,0,0,.5),0 0 36px rgba(0,0,0,.7)}
.mono{font-family:JBM;letter-spacing:.06em}
.tag{display:inline-block;font-family:BC9;text-transform:uppercase;color:${C.abyss};background:${C.flare};padding:6px 18px 4px}
.ro{position:absolute;left:44px;top:36px;font-size:26px;display:flex;align-items:center;gap:12px;background:rgba(10,18,20,.78);padding:8px 16px}
.dot{width:16px;height:16px;border-radius:50%;background:${C.signal};box-shadow:0 0 14px ${C.signal}}
.logo{position:absolute;left:44px;bottom:34px;display:flex;align-items:center;gap:12px;font-family:BC9;font-size:40px}`;
const ringSvg = (ring) => { if (!ring) return ""; const RC = ring.color === "alarm" ? C.alarm : C.signal;
  return `<svg style="position:absolute;inset:0" width="1280" height="720"><circle cx="${ring.x}" cy="${ring.y}" r="${ring.r}" fill="none" stroke="${RC}" stroke-width="${RC === C.alarm ? 12 : 9}" style="filter:drop-shadow(0 0 8px rgba(0,0,0,.8))"/>
  <circle cx="${ring.x}" cy="${ring.y}" r="${ring.r + 18}" fill="none" stroke="${RC}" stroke-width="3" stroke-dasharray="14 12" opacity=".8"/></svg>`; };
const arrowSvg = (a) => { if (!a) return "";
  const ang = Math.atan2(a.y2 - a.y1, a.x2 - a.x1), h = 46, w = 0.5;
  const p1 = [a.x2 - h * Math.cos(ang - w), a.y2 - h * Math.sin(ang - w)], p2 = [a.x2 - h * Math.cos(ang + w), a.y2 - h * Math.sin(ang + w)];
  const ex = a.x2 - 30 * Math.cos(ang), ey = a.y2 - 30 * Math.sin(ang);
  return `<svg style="position:absolute;inset:0;filter:drop-shadow(0 4px 6px rgba(0,0,0,.7))" width="1280" height="720">
    <line x1="${a.x1}" y1="${a.y1}" x2="${ex}" y2="${ey}" stroke="${C.alarm}" stroke-width="16" stroke-linecap="round"/>
    <polygon points="${a.x2},${a.y2} ${p1[0]},${p1[1]} ${p2[0]},${p2[1]}" fill="${C.alarm}"/></svg>`; };
const ph = (o) => `<div class="ph" style="background:url(${img(o.image || cfg.image)});background-position:${o.pos || cfg.pos || "50% 50%"};background-size:${o.zoom || cfg.zoom || 100}%"></div>`;
const marks = (o) => ringSvg("ring" in o ? o.ring : cfg.ring) + arrowSvg("arrow" in o ? o.arrow : cfg.arrow);
const mark = `<svg width="52" height="52" viewBox="0 0 512 512"><rect width="512" height="512" rx="112" fill="#13242A"/><path d="M64,300 H150 Q174,258 198,300 H262 M262,118 V392 M262,284 L350,118 M262,284 L366,392 L396,300 H440" fill="none" stroke="${C.signal}" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/><circle cx="452" cy="300" r="20" fill="${C.sonar}"/></svg>`;
const grad = (p) => `<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,18,20,.96) 0%,rgba(10,18,20,.85) ${p}%,rgba(10,18,20,0) ${p + 26}%)"></div>`;
const html = {
  A: (o) => `<div class="t">${ph(o)}${grad(30)}${marks(o)}
    <div class="ro mono"><div class="dot"></div>${cfg.badge || "KEPT ALIVE · REAL FOOTAGE"}</div>
    <div style="position:absolute;left:44px;top:118px">
      <div class="big" style="font-size:${o.size || 200}px">${hi(o.big)}</div>
      ${o.tag ? `<div class="tag" style="font-size:${o.tsize || 62}px;margin-top:22px">${o.tag}</div>` : ""}</div>
    <div class="logo">${mark}KEPT&nbsp;<span style="color:${C.signal}">ALIVE</span></div></div>`,
  B: (o) => `<div class="t">${ph(o)}<div style="position:absolute;inset:0;background:linear-gradient(270deg,rgba(10,18,20,.95) 0%,rgba(10,18,20,.8) 30%,rgba(10,18,20,0) 58%)"></div>${marks(o)}
    <div style="position:absolute;right:44px;top:56px;width:600px;text-align:right">
      ${o.kicker ? `<div class="mono" style="font-size:${o.ksize || 32}px;color:${C.sonar}">${o.kicker}</div>` : ""}
      <div class="big" style="font-size:${o.size || 170}px;margin-top:10px">${hi(o.big).replace(/<em>/g, `<span style="color:${C.alarm}">`).replace(/<\/em>/g, "</span>")}</div>
      <div style="height:12px;width:220px;background:${C.alarm};margin:22px 0 0 auto"></div></div>
    <div class="logo">${mark}KEPT&nbsp;<span style="color:${C.signal}">ALIVE</span></div></div>`,
  C: (o) => `<div class="t">${ph(o)}${grad(36)}${marks(o)}
    <div style="position:absolute;left:44px;top:70px;width:640px">
      <div class="mono" style="font-size:${o.ksize || 34}px;color:${C.sonar}">${o.kicker}</div>
      <div class="big" style="font-size:${o.size || 150}px;margin-top:14px">${hi(o.big)}</div></div>
    <div class="logo">${mark}KEPT&nbsp;<span style="color:${C.signal}">ALIVE</span></div></div>`,
};
const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1280, height: 720 } });
for (const k of ["A", "B", "C"]) {
  if (!cfg[k]) continue;
  await pg.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>${html[k](cfg[k])}</body></html>`);
  await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(150);
  await pg.screenshot({ path: path.join(out, `thumb_${k}.jpg`), type: "jpeg", quality: 92 });
  console.log("thumb", k);
}
await b.close();
