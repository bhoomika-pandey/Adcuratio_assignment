import requests 
from bs4 import BeautifulSoup
URL = 'https://news.ycombinator.com​'
r = requests.get(URL) 

#soup = BeautifulSoup(r.content, 'html5lib')
#print(soup.prettify() 

#import urllib.request

#more_links = True
#page = 1
#quotes = []
#while(more_links):
#parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
#resp = urllib.request.urlopen("https://news.ycombinator.com")
#soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
#url_list = soup.find(class_='storylink')
#heading_list = url_list.find_all('a')

#Create for loop to print out all artists' names
#for heading in heading_list:
 #   print(heading.prettify())
#
# next_link = soup.select_one('.next > a')

#if(next_link):
#    page += 1
#else:
#    more_links = False
#markup = requests.get(f'https://news.ycombinator.com').text
#
## pass the string to a BeatifulSoup object
#soup = BeautifulSoup(markup, 'html.parser')
#
##this will hold all the quotes
#quotes = []
#
## now we can select elements
#for item in soup.select('.quote'):
#    quote = {}
#    quote['title'] = item.select_one('.title').get_text()
#    quote['description'] = item.select_one('.description').get_text()
#
#    # get the tags element
#    tags = item.select_one('.tags')
#
#    # get each tag text from the tags element
#    quote['tags'] = [tag.get_text() for tag in tags.select('.tag')]
#    quotes.append(quote)
#    
#print(quotes)

#client = pymongo.MongoClient("mongodb+srv://bhoomika-pandey:<password>@adcuratiovassignment.lsau5.mongodb.net/<dbname>?retryWrites=true&w=majority")
#db = client.test
