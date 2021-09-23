import requests
import json
import time

stocks = [
          "Dax",
          "Dow Jones",
          "NasDaq",
          "adidas",
          "Airbus",
          "Allianz",
          "BASF",
          "Bayer",
          "BMW",
          "Brenntag",
          "continental",
          "covestro",
          "daimler",
          "Delivery Hero",
          "Deutsche Bank",
          "Deutsche Börse",
          "Deutsche Post",
          "E.on",
          "Fresenius Medical Care",
          "Fresenius",
          "HeidelbergCement",
          "HelloFresh",
          "Henkel",
          "Infineon",
          "Linde",
          "Merck",
          "MTU Aero Engines",
          "Münchener Rückversicherungs-Gesellschaft",
          "Porsche",
          "PUMA",
          "QIAGEN",
          "RWE",
          "SAP",
          "Sartorius",
          "Siemens",
          "Siemens Energy",
          "Siemens Healthineers",
          "Symrise",
          "Volkswagen",
          "Vonovia",
          "Zalando"]
back = {}
for x in stocks:
    time.sleep(14)
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={x}&apikey=EP7VOHUF5XUQMVEX'
    r = requests.get(url, verify=False)
    data = json.loads(r.text)
    print(x)
    if data["bestMatches"] != {}:
        back[data["bestMatches"][0]["1. symbol"]] = x

for x in back:
    print("'" + x + "' : '" + back[x] + "'")