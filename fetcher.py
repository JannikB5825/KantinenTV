import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


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


