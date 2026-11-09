// KEPT ALIVE thumbnails. usage: node thumb.mjs <thumb.json> <out_dir>
// thumb.json: {"image":"/abs/frame.jpg","pos":"60% 40%","zoom":135,
//   "A":{"big":"RAFT<br><s>SINKING</s>","tag":"ALASKA · NIGHT"},
//   "C":{"kicker":"2 MILES OFFSHORE","big":"HIS RAFT WAS <s>SINKING</s>"},
//   "ring":{"x":930,"y":420,"r":150}}  // optional target ring around the subject
// Rules: 1–5 words, real frame from the video, nothing in bottom-right (duration badge), no injuries in close-up.
import fs from "fs"; import path from "path"; import { createRequire } from "module";
const require = createRequire(import.meta.url); const { chromium } = require("playwright");
const NM = path.resolve(path.dirname(new URL(import.meta.url).pathname), "node_modules");
const cfg = JSON.parse(fs.readFileSync(process.argv[2])); const out = process.argv[3]; fs.mkdirSync(out, { recursive: true });
const font = (f, file) => `@font-face{font-family:${f};src:url(data:font/woff2;base64,${fs.readFileSync(`${NM}/@fontsource/${file}`).toString("base64")})}`;
const IMG = `data:image/jpeg;base64,${fs.readFileSync(cfg.image).toString("base64")}`;
const C = { abyss: "#0A1214", foam: "#EEF2EF", signal: "#2BB3A3", flare: "#F2B33D", sonar: "#6CF29A" };
const hi = (s) => s.replace(/<s>/g, `<span style="color:${C.signal}">`).replace(/<\/s>/g, "</span>");
const CSS = `${font("BC9", "saira-condensed/files/saira-condensed-latin-800-normal.woff2")}
${font("JBM", "martian-mono/files/martian-mono-latin-500-normal.woff2")}
*{margin:0;padding:0;box-sizing:border-box}
.t{position:relative;width:1280px;height:720px;overflow:hidden;background:${C.abyss};color:${C.foam}}
.ph{position:absolute;inset:0;background:url(${IMG});background-position:${cfg.pos || "50% 50%"};background-size:${cfg.zoom || 100}%;filter:contrast(1.08) saturate(1.12)}
.big{font-family:BC9;line-height:.88;text-transform:uppercase;text-shadow:0 5px 0 rgba(0,0,0,.5),0 0 36px rgba(0,0,0,.7)}
.mono{font-family:JBM;letter-spacing:.06em}
.tag{display:inline-block;font-family:BC9;text-transform:uppercase;color:${C.abyss};background:${C.flare};padding:6px 18px 4px}
.ro{position:absolute;left:44px;top:36px;font-size:26px;display:flex;align-items:center;gap:12px;background:rgba(10,18,20,.78);padding:8px 16px}
.dot{width:16px;height:16px;border-radius:50%;background:${C.signal};box-shadow:0 0 14px ${C.signal}}
.logo{position:absolute;left:44px;bottom:34px;display:flex;align-items:center;gap:12px;font-family:BC9;font-size:40px}`;
const ringSvg = cfg.ring ? `<svg style="position:absolute;inset:0" width="1280" height="720"><circle cx="${cfg.ring.x}" cy="${cfg.ring.y}" r="${cfg.ring.r}" fill="none" stroke="${C.signal}" stroke-width="9"/>
  <circle cx="${cfg.ring.x}" cy="${cfg.ring.y}" r="${cfg.ring.r + 18}" fill="none" stroke="${C.signal}" stroke-width="3" stroke-dasharray="14 12" opacity=".8"/></svg>` : "";
const mark = `<svg width="52" height="52" viewBox="0 0 512 512"><rect width="512" height="512" rx="112" fill="#13242A"/><path d="M64,300 H150 Q174,258 198,300 H262 M262,118 V392 M262,284 L350,118 M262,284 L366,392 L396,300 H440" fill="none" stroke="${C.signal}" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/><circle cx="452" cy="300" r="20" fill="${C.sonar}"/></svg>`;
const grad = (p) => `<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,18,20,.96) 0%,rgba(10,18,20,.85) ${p}%,rgba(10,18,20,0) ${p + 26}%)"></div>`;
const html = {
  A: (o) => `<div class="t"><div class="ph"></div>${grad(30)}${ringSvg}
    <div class="ro mono"><div class="dot"></div>${cfg.badge || "KEPT ALIVE · REAL FOOTAGE"}</div>
    <div style="position:absolute;left:44px;top:118px">
      <div class="big" style="font-size:${o.size || 200}px">${hi(o.big)}</div>
      ${o.tag ? `<div class="tag" style="font-size:${o.tsize || 62}px;margin-top:22px">${o.tag}</div>` : ""}</div>
    <div class="logo">${mark}KEPT&nbsp;<span style="color:${C.signal}">ALIVE</span></div></div>`,
  C: (o) => `<div class="t"><div class="ph"></div>${grad(36)}${ringSvg}
    <div style="position:absolute;left:44px;top:70px;width:640px">
      <div class="mono" style="font-size:${o.ksize || 34}px;color:${C.sonar}">${o.kicker}</div>
      <div class="big" style="font-size:${o.size || 150}px;margin-top:14px">${hi(o.big)}</div></div>
    <div class="logo">${mark}KEPT&nbsp;<span style="color:${C.signal}">ALIVE</span></div></div>`,
};
const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1280, height: 720 } });
for (const k of ["A", "C"]) {
  if (!cfg[k]) continue;
  await pg.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>${html[k](cfg[k])}</body></html>`);
  await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(150);
  await pg.screenshot({ path: path.join(out, `thumb_${k}.jpg`), type: "jpeg", quality: 92 });
  console.log("thumb", k);
}
await b.close();
