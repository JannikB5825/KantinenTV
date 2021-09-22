import requests
import json


stocks = ["ADDYY","ALV.DE"]
def get_stock(stocks):
    back = ""
    for symbol in stocks:
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=EP7VOHUF5XUQMVEX'
        r = requests.get(url, verify=False)
        data = json.loads(r.text)["Global Quote"]
        back += data["01. symbol"] + " " + data["05. price"] + " " + data["10. change percent"] + "     "
    return back

print(get_stock(stocks))