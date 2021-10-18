import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
from requests_ntlm import HttpNtlmAuth
import requests_ntlm

def send_request(url, username, password):
    """
    Sends a request to the url with the credentials specified. Returns the final response
    """
    session = requests.Session()
    session.verify = False
    session.auth = requests_ntlm.HttpNtlmAuth(username, password)
    response = session.get(url)
 
    return response

class CrawledFetcher():
  def __init__(self, title, content, date, image):
    self.title = title
    self.content = content
    self.author = "Bender"
    self.date = date
    self.image = image
  def selfList(self):
    return [str(self.title), str(self.content), str(self.author), str(self.date), str(self.image)]


class ArticleFetcher():
  #bender.de  
  def fetch():
    url = "https://www.bender.de/unternehmen/news"
    articles = [ ]
    time.sleep(1)
    r = requests.get(url)
    doc = BeautifulSoup(r.text, "html.parser")
    for card in doc.select(".row.news-list-item"):
      content = card.select_one("p.bodytext").text
      title = card.select_one("a").get("title")
      date = card.select_one("time").text[3:-4]
      img = card.select_one("img").get("src")
      crawled = CrawledFetcher(title, content, date, img)
      articles.append(crawled.selfList())
    return articles[:5]

  def fetchIntra():
    url = "https://intra.mybender.com/de"
    articles = [ ]
    time.sleep(1)
    r = send_request(url, "jannik.becker", "BenderCoaster5")
    doc = BeautifulSoup(r.text, "html.parser")
    print(doc)
    for card in doc.select("tr.ms-itmHoverEnabled "):
      strong = card.select_one("strong").text
      if "â€‹" in strong:
        strong = "".join(c for c in strong if ord(c)<128)
      title = card.select_one("p")
      if type(title) != """NoneType""":
        title = title.get_text().replace("\xa0"," ")
        title = "".join(c for c in title if ord(c)<128)[len(strong):]
      #date = card.select_one("time").text[3:-4]
      #img = card.select_one("img").get("src")
      crawled = CrawledFetcher(strong, title, "date", "img")
      articles.append(crawled.selfList())
    return articles
  
srticels = ArticleFetcher.fetchIntra()
for x in srticels:
  print(x[0])
  print(x[1])