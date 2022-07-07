import random
import requests
import datetime
import time
from bs4 import BeautifulSoup


url = "https://www.theguardian.com/uk"



def scrape(url):
  
  randomUrls = [ 
    "https://www.facebook.com/", 
    "https://www.google.co.uk", 
    "https://www.twitter.com"
    ]

  headers = {
    'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Referer': random.choice(randomUrls) 
    }

  results = requests.get(url, headers=headers, allow_redirects=False)


  # beautiful soup methods are now available to clean this data response
  soup = BeautifulSoup(results.text, "html.parser")
  
  headline_html = soup.find('span', class_='js-headline-text')

  if headline_html != None:
    headline = headline_html.text.strip()
  else:
    headline = fail

  print(headline)  

scrape(url)
  

