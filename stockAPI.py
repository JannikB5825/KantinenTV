import requests
import json
import time

stocks = {
    '0OLD.LON' : 'adidas',
    'AIRA.FRK' : 'Airbus',
    '0M6S.LON' : 'Allianz',
    'BASFX' : 'BASF',
    'BAYRY' : 'Bayer',
    'BMW.FRK' : 'BMW',
    '0MPT.LON' : 'Brenntag',
    'CTTAF' : 'continental',
    '0RBE.LON' : 'covestro',
    '0NXX.LON' : 'daimler',
    '0RTC.LON' : 'Delivery Hero',
    '0H7D.LON' : 'Deutsche Bank',
    'DB1.DEX' : 'Deutsche Börse',
    '0H3Q.LON' : 'Deutsche Post',
    '0MPP.LON' : 'E.on',
    '0H9X.LON' : 'Fresenius Medical Care',
    'FSNUF' : 'Fresenius',
    '0MG2.LON' : 'HeidelbergCement',
    'HELFY' : 'HelloFresh',
    'HENKY' : 'Henkel',
    '0KED.LON' : 'Infineon',
    'LIN.DEX' : 'Linde',
    'MRK' : 'Merck',
    '0FC9.LON' : 'MTU Aero Engines',
    'MUV2.DEX' : 'Münchener Rückversicherungs-Gesellschaft',
    'POAHF' : 'Porsche',
    'PUMA.TRV' : 'PUMA',
    'QGEN' : 'QIAGEN',
    'RWE.FRK' : 'RWE',
    'SAP' : 'SAP',
    'SARTF' : 'Sartorius',
    '0P6M.LON' : 'Siemens',
    'ENR.DEX' : 'Siemens Energy',
    'SEMHF' : 'Siemens Healthineers',
    '0G6T.LON' : 'Symrise',
    'TSLA' : 'Tesla',
    '0P6N.LON' : 'Volkswagen',
    '0QFT.LON' : 'Vonovia',
    '0QXN.LON' : 'Zalando'
}
cryptos = ["BTC","ETH"]


def get_stock(stocks):
    back = []
    for symbol in stocks.keys():
        time.sleep(15)
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
            
        back.append([stocks[symbol], close, char, dif])
    return back


def get_cryptos(cryptos):
    back = []
    for symbol in cryptos:
        time.sleep(15)
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
    return back

def get_both(stocks, cryptos):
    back = get_stock(stocks)
    for x in get_cryptos(cryptos):
        back.append(x)
    return back

