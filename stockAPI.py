import requests
import json
import time

stocks = ["ADDYY","ALV.DE"]
cryptos = ["BTC","ETH"]


def get_stock(stocks):
    back = []
    for symbol in stocks:
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=EP7VOHUF5XUQMVEX'
        r = requests.get(url, verify=False)
        data = json.loads(r.text)["Global Quote"]
        close = str(round(float(data["05. price"]),1))
        dif = float(data["10. change percent"][:-1])
        dif = round(dif, 1)
        char = ""
        if dif > 0:
            dif = "+" + str(dif) + "%"
            char = "\u25B2"
        elif dif < 0:
            dif = str(dif) + "%"
            char = "\u25BC"
        else:
            dif = "0.0%"
            char = "="
            
        back.append([data["01. symbol"], close, char, dif])
        time.sleep(1.5)
    return back


def get_cryptos(cryptos):
    back = []
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
        char = ""
        if dif > 0:
            dif = "+" + str(dif) + "%"
            char = "\u25B2"
        elif dif < 0:
            dif = str(dif) + "%"
            char = "\u25BC"
        else:
            dif = "0.0%"
            char = "="
        back.append([symbol, str(close), char, dif])
        time.sleep(1.5)
    return back

def get_both(stocks, cryptos):
    back = get_stock(stocks)
    for x in get_cryptos(cryptos):
        back.append(x)
    return back
