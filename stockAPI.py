#install yfinance
import requests
import json
import yfinance as yf

stocks = ["ADS"]
for symbol in stocks:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=EP7VOHUF5XUQMVEX'
    r = requests.get(url, verify=False)
    data = json.loads(r.text)
    data = data[list(data.keys())[1]]
    res = list(data.keys())[0]
    open = float(data[res]["1. open"])
    close = float(data[res]["4. close"])
    perc = round((((open - close)/open) * 100),2)
    if perc > 0:
        perc = "+" + str(perc) + "%"
    else:
        perc = str(perc) + "%"

    print(stock + " " + str(close) + " " + perc)