import sys
import requests
from bs4 import BeautifulSoup
import time
import requests_ntlm
import urllib3
import re
from datetime import datetime
import urllib
import base64

username = "jannik.becker"
password = "BenderCoaster5"

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

print(send_request('https://intra.mybender.com/de/PublishingImages/Seiten/News/Informationstechnologie/Freigabe-iOS-15-/Update_Tablets_Phones_1080x1080px.jpg').content)