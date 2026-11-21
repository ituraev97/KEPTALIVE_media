import sys,json,gzip,re,urllib.request,os
ident,pat=sys.argv[1],sys.argv[2]
for suf in ['_hocr_pageindex.json.gz','_hocr_searchtext.txt.gz']:
    fn=ident+suf
    if not os.path.exists(fn): urllib.request.urlretrieve(f"https://archive.org/download/{ident}/{fn}",fn)
pi=json.load(gzip.open(ident+'_hocr_pageindex.json.gz')); t=gzip.open(ident+'_hocr_searchtext.txt.gz').read().decode('utf8','replace')
for i,p in enumerate(pi):
    s=' '.join(t[p[0]:p[1]].split())
    if re.search(pat,s,re.I): print(ident,i)
