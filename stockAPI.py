import requests
import json
import time

stocks = ["ADDYY","ALV.DE"]
cryptos = ["BTC"]


def get_stock(stocks):
    back = []
    for symbol in stocks:
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=EP7VOHUF5XUQMVEX'
        r = requests.get(url, verify=False)
        data = json.loads(r.text)["Global Quote"]
        dif = float(data["10. change percent"][:-1])
        dif = round(dif, 1)
        if dif > 0:
            dif = "+" + str(dif) + "%"
        else:
            dif = str(dif) + "%"
        back.append([data["01. symbol"], data["05. price"], dif])
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
        if dif > 0:
            dif = "+" + str(dif) + "%"
        else:
            dif = str(dif) + "%"
        back.append([symbol, str(close), dif])
        time.sleep(1.5)
    return back

def get_both(stocks, cryptos):
    back = get_stock(stocks)
    for x in get_cryptos(cryptos):
        back.append(x)
    return back

print(get_both(stocks, cryptos))