import urllib.request as req
url="https://medium.com/_/api/collections/15f753907972/stream?to=1714805084979&ignoredIds=33e743431419&ignoredIds=803bff156c94&ignoredIds=e01ff8f55ad5&ignoredIds=c0990715ff82&ignoredIds=d7184417f44a&ignoredIds=2cfb1dafa901&page=5"
request=req.Request(url, headers={
     "cookie":"over18=1",
     "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
     })
with req.urlopen(request) as response:
     data=response.read().decode("utf-8")

import json
data=data.replace("])}while(1);</x>","")
data=json.loads(data)
posts=data["payload"]["references"]["Post"]
for key in posts:
     post=posts[key]
     print(post["title"])