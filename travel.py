import json
import requests
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

f = open("data.json","r")
data = json.load(f)

htags = ['h1','h2','h3','h4','h5','h6']
for i, article in enumerate(data):
    url = article["url"]
    res = requests.get(url,headers = headers)
    soup = BeautifulSoup(res.text, "lxml")
    
# Getting headings
    heading = ""
    for htag in htags:
        head = soup.find(htag)
        if head != None:
            heading = head.text.replace("\n", "").strip()
            break
    else:
        head = ""
    article["heading"] = heading
    
#  Getting image urls   
    img_url = ""
    img_tag = soup.find("img")
    
    if not img_tag == None:
        img_url = img_tag['src']
        if not img_url.startswith("http"):
            img_url = url + img_url
    article["img_url"] = img_url
    
    
    print(f"processed{i}")
f = open("data.json","w")
json.dump(data, f)