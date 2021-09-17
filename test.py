from bs4 import BeautifulSoup as BSHTML
import urllib
page = urllib.request.open("https://www.bender.de/unternehmen/news")
soup = BSHTML(page)
images = soup.findAll('img')
for image in images:
    #print image source
    print(image['src'])
    #print alternate text
    print(image['alt'])