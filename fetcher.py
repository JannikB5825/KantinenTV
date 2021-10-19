import sys
import requests
from bs4 import BeautifulSoup
import time
import requests_ntlm
import urllib3
import re
from datetime import datetime

username = "jannik.becker"
password = "BenderCoaster5"

def disable_warnings(): 
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def send_request(url, username, password):
    """
    Sends a request to the url with the credentials specified. Returns the final response
    """
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
    self.author = "Bender"
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
      crawled = CrawledFetcher(title, content, date, img)
      articles.append(crawled.selfList())
    return articles[:5]

  def fetchIntra():
    global username, password
    
    disable_warnings()
    url = "https://intra.mybender.com"
    articles = [ ]
    time.sleep(1)
    r = send_request(url, username, password)
    doc = BeautifulSoup(r.text, "html.parser")
    
    main_body = doc.find_all("tbody")[1]
    for card in main_body.find_all("tr")[1].find_all("tr")[1:]:
      date = "date"
      title = card.get_text()
      strong = card.select_one("strong").text
      img = "Bender"
      date = card.find("nobr").text[:-6]
      if type(strong) != """NoneType""":
        strong = "".join(c for c in strong if ord(c)<128)
        strong = strong.replace("\u200b","")
      
      if type(title) != """NoneType""":
        title = title.replace("\xa0"," ")
        title = title.replace("\u200b","")
        title = "".join(c for c in title if ord(c)<128)[len(strong)-1:]
      
      linkToMain = re.findall(r'"([^"]*)"', str(card.find("a")))
      if len(linkToMain) > 0:
        if linkToMain[0][0] != "/":
          linkToMain = "Bender"
        else:
          linkToMain = url + linkToMain[0]
          newR = send_request(linkToMain, username, password)
          newDoc = BeautifulSoup(newR.text, "html.parser")
          imageMain = newDoc.find("div", {"class": "ms-rtestate-field"})
          img = imageMain.select_one("img").get("src")
          if img[:3] == "/de":
            img = url + img
          else:
            img = "Bender"
      else:
        linkToMain = "Bender"
      
      crawled = CrawledFetcher(strong, title, date, img)
      articles.append(crawled.selfList())
    return articles

def getBothDates():
  list1 = ArticleFetcher.fetch()
  list2 = ArticleFetcher.fetchIntra()
  joined = list1 + list2
  joined.sort(key=lambda date: datetime.strptime(date[3], "%d.%m.%Y"))
  return joined.reverse()