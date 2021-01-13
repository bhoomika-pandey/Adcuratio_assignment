import json
import requests
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

data = []

for page in range(1,5):

    res = requests.get(f'https://news.ycombinator.com/news?p={page}',headers = headers)
    soup = BeautifulSoup(res.text,"lxml")

    posts = soup.find("table", {"class": "itemlist"})

    trs = posts.find_all('tr')
    athings = trs[0::3]
    scores_links = trs[1::3]

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

        if url != "":
            data.append({"url":url, "title":title, "upvote":upvote})
    
f = open("data.json","w")
json.dump(data, f, ensure_ascii=False)
f.close()

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