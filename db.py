import json
from pymongo import MongoClient

f = open("data.json","r")
data = json.load(f)


#Creating a pymongo client
client = MongoClient('localhost', 27017)

#Getting the database instance

if 'adcuratio' in client.list_database_names():
    client.drop_database('adcuratio')
db = client['adcuratio']
    
#Creating a collection
url_collection = db['url']
heading_collection = db['heading']
metadata_collection = db['metadata']

# url_collection.insert_many([{"url":article["url"]}for article in data])

# heading_collection.insert_many([{"heading":article["heading"]}for article in data])

# metadata_collection.insert_many([{"img_url":article["img_url"],"title":article["title"],"upvote":article["upvote"]}for article in data])

for article in data:
    url_id = url_collection.insert_one({"url":article['url']}).inserted_id
    heading_collection.insert_one({"heading":article["heading"],"url_id":url_id})
    metadata_collection.insert_one({"img_url":article["img_url"],"title":article["title"],"upvote":article["upvote"],"url_id":url_id})