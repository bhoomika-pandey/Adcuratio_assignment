import requests
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

res = requests.get('https://news.ycombinator.com',headers = headers)
soup = BeautifulSoup(res.text,"lxml")

posts = soup.find("table", {"class": "itemlist"})

trs = posts.find_all('tr')
athings = trs[0::3]
scores_links = trs[1::3]
data = []


for a, s in zip(athings, scores_links):
    try:
        url = a.find('a', {"class":"storylink"})['href']
        if not url.startswith("http"):
            url = "https://news.ycombinator.com/"+url
    except Exception as e:
        url = ""
    try:
        title = a.find('a', {"class":"storylink"}).text
    except Exception as e:
        title = ""
    try:
        upvote = s.find('span', {"class":"score"}).text.replace(" points", "")
    except Exception as e:
        upvote = ""
    data.append({"url":url, "title":title, "upvote":upvote})
    
# print(data[0])

f = open("data.json","w")
import json
json.dump(data[:-1], f)


# [
# {
    # url: ".......",
    # description: "........",
    # title: "...........",
    # upvotes: "......"
# },
# {
    # url: ".......",
    # description: "........",
    # title: "...........",
    # upvotes: "......"
# },
# {
    # url: ".......",
    # description: "........",
    # title: "...........",
    # upvotes: "......"
# },
# {
    # url: ".......",
    # description: "........",
    # title: "...........",
    # upvotes: "......"
# },
# {
    # url: ".......",
    # description: "........",
    # title: "...........",
    # upvotes: "......"
# }
# ]