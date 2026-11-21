import json,gzip,sys,re
d=sys.argv[1]; ident=sys.argv[2]
pi=json.load(gzip.open(f"{d}/{ident}_pi.json.gz"))
t=gzip.open(f"{d}/{ident}_st.txt.gz").read().decode('utf8','replace')
out={}
for i,p in enumerate(pi):
    out[i]=t[p[0]:p[1]]
json.dump(out,open(f"{d}/{ident}_pages.json","w"))
print(len(pi))
