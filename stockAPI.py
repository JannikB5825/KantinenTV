import requests
import json


stocks = ["ADDYY","ALV.DE"]
cryptos = ["BTC"]


def get_stock(stocks):
    back = ""
    for symbol in stocks:
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=EP7VOHUF5XUQMVEX'
        r = requests.get(url, verify=False)
        data = json.loads(r.text)["Global Quote"]
        back += data["01. symbol"] + " " + data["05. price"] + " " + data["10. change percent"] + "     "
    return back


def get_cryptos(cryptos):
    back = ""
    for symbol in cryptos:
        url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market=EUR&apikey=EP7VOHUF5XUQMVEX'
        r = requests.get(url, verify=False)
        data = json.loads(r.text)["Time Series (Digital Currency Daily)"]
        res = list(data.keys())[1]
        data = data[res]
        open = round(float(data["1a. open (EUR)"]),1)
        close = round(float(data["4a. close (EUR)"]),1)
        dif = close - open
        dif = round((dif/open * 100),1)
        if dif > 0:
            dif = "+" + str(dif) + "%"
        else:
            dif = str(dif) + "%"
        back += symbol + " " + str(close) + " " + dif + "    "
    return back

print(get_cryptos(cryptos))