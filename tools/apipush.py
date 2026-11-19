import subprocess,json,base64,urllib.request,sys
R="https://api.github.com/repos/gugewang319-spec/mintchoco-demo"
def api(m,path,data=None):
  req=urllib.request.Request(R+path,method=m,data=json.dumps(data).encode() if data else None,headers={"Accept":"application/vnd.github+json","Content-Type":"application/json"})
  return json.load(urllib.request.urlopen(req))
base=sys.argv[1];branch=sys.argv[2]
remote=api("GET",f"/git/ref/heads/{branch}")["object"]["sha"]
assert remote.startswith(base),("remote moved",remote)
files=subprocess.check_output(["git","diff","--name-only",base,"HEAD"]).decode().split()
tree=[]
import os
for f in files:
  if not os.path.exists(f):
    tree.append({"path":f,"mode":"100644","type":"blob","sha":None});continue
  c=open(f,'rb').read()
  b=api("POST","/git/blobs",{"content":base64.b64encode(c).decode(),"encoding":"base64"})
  tree.append({"path":f,"mode":"100644","type":"blob","sha":b["sha"]})
bt=api("GET",f"/git/commits/{remote}")["tree"]["sha"]
t=api("POST","/git/trees",{"base_tree":bt,"tree":tree})
msg=subprocess.check_output(["git","log","-1","--format=%s"]).decode().strip()
c=api("POST","/git/commits",{"message":msg,"tree":t["sha"],"parents":[remote]})
api("PATCH",f"/git/refs/heads/{branch}",{"sha":c["sha"]})
print(c["sha"][:7],len(files))
