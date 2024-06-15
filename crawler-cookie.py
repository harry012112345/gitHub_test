import urllib.request as req
def getData(url):
 url="https://www.ptt.cc/bbs/Gossiping/index.html"
 request=req.Request(url, headers={
     "cookie":"over18=1",
     "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
     })
 with req.urlopen(request) as response:
     data=response.read().decode("utf-8")

 import bs4
 root=bs4.BeautifulSoup(data, "html.parser")
 titles=root.find_all("div",class_="title")
 for title in titles:
    if title.a != None:
     print(title.a.string)
 nextLink=root.find("a",string="‹ 上頁")
 return nextLink["href"]

pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<5:
 pageURL="https://www.ptt.cc"+getData(pageURL)
 count+=1