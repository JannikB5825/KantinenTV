import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


class CrawledFetcher():
  def __init__(self, content, title, image):
    self.content = content
    self.title = title
    self.image = image

 

class ArticleFetcher():  
  def fetch(self):
    url = "https://www.bender.de/unternehmen/news"
    articles = [ ]
    print(url)
    time.sleep(1)
    r = requests.get(url)
    doc = BeautifulSoup(r.text, "html.parser")
    for image in doc.findAll('img'):
      v = image.get('src', image.get('dfr-src'))
      if v is not None:
        print(v)

    for card in doc.select("div.row news-list-item"):
      content = card.select_one("p.bodytext").text
      title = card.select("a.title").text
      image = card.select_one("img.img-responsive").text
      crawled = CrawledFetcher(content, title, image)
      articles.append(crawled)

    return articles

 #moin

fetcher = ArticleFetcher()
for article in fetcher.fetch():
  print(article.image + ": " + article.title)