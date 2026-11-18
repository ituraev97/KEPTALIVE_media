import subprocess, os, sys
A="/home/claude/clips/arch_raw"; O="/home/claude/clips"
def t(s):
    m,x=s.split(":"); return int(m)*60+float(x)
X = [  # name, source, start, end
 ("sav_build","yt_pzfu_Sru79M","0:52","1:10"),("sav_aides","yt_pzfu_Sru79M","1:16","2:26"),("sav_ward","yt_pzfu_Sru79M","2:56","4:30"),
 ("sav_walk","yt_pzfu_Sru79M","5:36","5:50"),("sav_train","yt_pzfu_Sru79M","5:52","7:50"),("sav_quay","yt_pzfu_Sru79M","8:52","9:58"),
 ("sav_mercy","yt_pzfu_Sru79M","10:20","11:26"),
 ("ny_liberty","yt_zkbFB4iOSps","0:16","1:44"),("ny_litter","yt_zkbFB4iOSps","9:20","10:40"),("ny_parade","yt_zkbFB4iOSps","16:56","18:20"),
 ("nh_convoy","yt_OifYcadH7FM","5:48","7:36"),("nh_load","yt_OifYcadH7FM","9:32","9:58"),("nh_unload","yt_OifYcadH7FM","10:52","11:10"),
 ("bac_barrage","yt_NTOTDS46Ikw","1:48","2:30"),("bac_crawl","yt_NTOTDS46Ikw","3:24","4:06"),("bac_trench","yt_NTOTDS46Ikw","4:40","5:22"),
 ("bac_aid","yt_NTOTDS46Ikw","7:36","8:30"),("bac_litter","yt_NTOTDS46Ikw","12:48","13:12"),("bac_cem","yt_NTOTDS46Ikw","18:32","19:52"),
 ("ma_trucks","yt_6hhKks9fg9c","0:52","1:40"),("ma_jam","yt_6hhKks9fg9c","3:40","4:12"),("ma_mud","yt_6hhKks9fg9c","7:04","8:16"),
 ("ma_litter","yt_6hhKks9fg9c","8:36","8:46"),("ma_road","yt_6hhKks9fg9c","10:36","11:12"),("ma_esnes","yt_6hhKks9fg9c","6:00","6:44"),
 ("am_choc","yt_Y9v6b6uFWt8","3:44","4:10"),("am_gas","yt_Y9v6b6uFWt8","8:36","8:56"),("am_letter","yt_Y9v6b6uFWt8","10:12","10:42"),
 ("am_advance","yt_LHmIST-EtMo","2:28","3:16"),("am_fh","yt_LHmIST-EtMo","4:52","5:06"),
 ("fis_tents","yt_gk8dunh3fZE","1:12","1:42"),("fis_sign","yt_gk8dunh3fZE","3:28","4:06"),
 ("sm_barrage","yt_T5r5ewWxvuM","1:44","2:56"),("sm_aid","yt_T5r5ewWxvuM","6:20","6:46"),
 ("arg_fh","yt_ZZ6PtbHehcw","1:40","1:54"),("arg_mg","yt_ZZ6PtbHehcw","3:08","3:44"),("arg_mud","yt_ZZ6PtbHehcw","4:32","4:46"),
 ("arg_pan","yt_s5MIf2MMB0c","0:08","1:14"),("arg_tents","yt_s5MIf2MMB0c","1:40","2:02"),("arg_aid","yt_s5MIf2MMB0c","3:40","3:54"),
 ("ct_amb","yt_CVeYj6HiKos","4:16","4:26"),
 ("gas_cloud","yt_CNtOiMRw_e0","0:52","1:46"),("gas_masks","yt_CNtOiMRw_e0","2:08","2:52"),("gas_trench","yt_CNtOiMRw_e0","3:04","4:10"),
 ("gas_litter","yt_CNtOiMRw_e0","4:20","4:30"),("gas_party","yt_CNtOiMRw_e0","5:56","6:38"),
 ("gh36","fc-fc-45","0:48","1:04"),
]
only = sys.argv[1:]
for n,src,a,b in X:
    if only and n not in only: continue
    out=f"{O}/{n}.mp4"
    if os.path.exists(out) and not only: continue
    f=f"{A}/{src}.mp4"
    w,h=map(int,subprocess.check_output(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height","-of","csv=p=0",f]).decode().split(","))
    if src.startswith("fc-"):
        vf="fps=24,scale=656:480,setsar=1,framerate=fps=30"
    else:
        aw=h*4//3; vf=f"crop={aw}:{h}:{(w-aw)//2}:0,setsar=1,framerate=fps=30"
    subprocess.run(["ffmpeg","-nostdin","-v","error","-y","-ss",str(t(a)),"-i",f,"-f","lavfi","-i","anullsrc=r=48000:cl=stereo","-t",str(t(b)-t(a)),
        "-vf",vf,"-map","0:v","-map","1:a","-c:v","libx264","-preset","veryfast","-crf","18","-pix_fmt","yuv420p","-c:a","aac","-shortest",out],check=True)
    print("ok",n,flush=True)
print("ALLDONE")
