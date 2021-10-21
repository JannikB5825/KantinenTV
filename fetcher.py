import sys
import requests
from bs4 import BeautifulSoup
import time
import requests_ntlm
import urllib3
import re
from datetime import datetime
import os

username = "jannik.becker"
password = "BenderCoaster5"
osPath = os.path.dirname(os.path.abspath(__file__)).replace("/","\\")
osPath = osPath.replace("\\","\\")+"\\"
filePath = osPath


def disable_warnings(): 
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def send_request(url):
    """
    Sends a request to the url with the credentials specified. Returns the final response
    """
    global username, password
    disable_warnings()
    session = requests.Session()
    session.verify = False
    session.auth = requests_ntlm.HttpNtlmAuth(username, password)
    response = session.get(url)
 
    return response

class CrawledFetcher():
  def __init__(self, title, content, date, image):
    self.title = title
    self.content = content
    self.author = "Bender123"
    self.date = date
    self.image = image
  def selfList(self):
    return [str(self.title), str(self.content), str(self.author), str(self.date), str(self.image)]


class ArticleFetcher():
  #bender.de  
  def fetch():
    disable_warnings()
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
      if img == None:
        img = "Bender123"
      crawled = CrawledFetcher(title, content, date, img)
      articles.append(crawled.selfList())
    return articles[:5]

  def fetchIntra():

    disable_warnings()
    url = "https://intra.mybender.com"
    articles = [ ]
    time.sleep(1)
    r = send_request(url)
    doc = BeautifulSoup(r.text, "html.parser")
    
    main_body = doc.find_all("tbody")[1]
    for card in main_body.find_all("tr")[1].find_all("tr")[1:]:
      img = "Bender123"
      title = card.get_text()
      strong = card.select_one("strong").text
      date = card.find("nobr").text[:-6]
      title = title[len(strong)+16:]
      
      
      if type(title) != """NoneType""":
        title = "".join(c for c in title if ord(c)<128)
        title = title.replace("\xa0"," ")
        title = title.replace("\u200b","")
        
      if type(strong) != """NoneType""":
        strong = "".join(c for c in strong if ord(c)<128)
        strong = strong.replace("\u200b","")

      linkToMain = re.findall(r'"([^"]*)"', str(card.find("a")))
      if len(linkToMain) > 0:
        if linkToMain[0][0] != "/":
          linkToMain = "Bender123"
        else:
          linkToMain = url + linkToMain[0]
          newR = send_request(linkToMain)
          newDoc = BeautifulSoup(newR.text, "html.parser")
          imageMain = newDoc.find("div", {"class": "ms-rtestate-field"})
          img = imageMain.select_one("img").get("src")
          if img[:3] == "/de":
            img = url + img
          else:
            img = "Bender123"
      else:
        linkToMain = "Bender123"
      
      crawled = CrawledFetcher(strong, title, date, img)
      articles.append(crawled.selfList())
    return articles
  
  #def fetchFromFile():
  #  articles = [ ]
  #  with open(filePath + "news.csv", "r") as r:
  #    lines = r.readlines()
  #    if lines != None:
  #      for line in lines:
  #        crawled = CrawledFetcher(line.split(";"))
  #        articles.append(crawled.selfList())
  #  r.close()
  #  return articles

def getBothDates():
  list1 = ArticleFetcher.fetch()
  list2 = ArticleFetcher.fetchIntra()
  #list3 = ArticleFetcher.fetchFromFile()
  joined = list1 + list2
  joined.sort(key=lambda date: datetime.strptime(date[3], "%d.%m.%Y"))
  joined.reverse()
  return joined