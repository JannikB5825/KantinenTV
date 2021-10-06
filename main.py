import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


class CrawledFetcher():
  def __init__(self, content, title, image):
    self.content = content
    self.title = title
    self.image = image
  def selfString(self):
    return str(str(self.content) + " " + str(self.title) + " " + str(self.image))


class ArticleFetcher():  
  def fetch(self):
    url = "https://www.bender.de/unternehmen/news"
    articles = [ ]
    time.sleep(1)
    r = requests.get(url)
    doc = BeautifulSoup(r.text, "html.parser")

    for card in doc.select(".row.news-list-item"):
      content = card.select_one("p.bodytext").text
      title = card.select("a.title")
      img = card.select_one("img").get("src")
      crawled = CrawledFetcher(content, title, img)
      articles.append(crawled)
    return articles



root = tk.Tk()
fetcher = ArticleFetcher()
button = tk.Button(root, text="Next image", command=lambda: nextImage())
button.pack()
panel = tk.Label(root)
panel.pack(side="bottom", fill="both", expand="yes")
card = fetcher.fetch()
counter = 0

def __main__():
  #w = open("test.txt","a")
  #for x in range(0,5):
  #  w.write(card[x].selfString())
  #  w.write("\n")
  root.after(0, __main__)

root.after(100, __main__)
root.mainloop()
