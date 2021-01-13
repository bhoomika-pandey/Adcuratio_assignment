# ycombinator scrapper

This projects is made as a part of Adcuratio assignment.  
It scrapes the first 120 articles from "https://news.ycombinator.com".  

For every article this scrapes:  
1. url
1. heading
1. title
1. image
1. description
1. votes

Steps to run:  

1. Open this repository in a virtual environment
1. run requirements.txt using => `pip install -r requirements.txt`
1. start mongodb usinf - `sudo systemctl start  mongod`
1. run main.py - Fetching title, url and votes from "https://news.ycombinator.com" 
1. run travel.py - Fetching heading, description and image for every article  
1. run db.py - Storing the results in mongodb database





