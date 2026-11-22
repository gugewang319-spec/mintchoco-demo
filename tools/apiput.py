import json,base64,urllib.request,sys
R="https://api.github.com/repos/gugewang319-spec/mintchoco-demo"
def api(m,p,d=None):
  r=urllib.request.Request(R+p,method=m,data=json.dumps(d).encode() if d else None,headers={"Accept":"application/vnd.github+json","Content-Type":"application/json"});return json.load(urllib.request.urlopen(r))
base,branch,msg=sys.argv[1:4];files=sys.argv[4:]
remote=api("GET",f"/git/ref/heads/{branch}")["object"]["sha"];assert remote.startswith(base),remote
tree=[{"path":f,"mode":"100644","type":"blob","sha":api("POST","/git/blobs",{"content":base64.b64encode(open(f,'rb').read()).decode(),"encoding":"base64"})["sha"]} for f in files]
t=api("POST","/git/trees",{"base_tree":api("GET",f"/git/commits/{remote}")["tree"]["sha"],"tree":tree})
c=api("POST","/git/commits",{"message":msg,"tree":t["sha"],"parents":[remote]})
api("PATCH",f"/git/refs/heads/{branch}",{"sha":c["sha"]});print(c["sha"])
