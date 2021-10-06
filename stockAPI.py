import requests
import json
import time

stocks = {
    '0OLD.LON' : 'Adidas',
    #'AIR.DEX' : 'Airbus',
    #'0M6S.LON' : 'Allianz',
    #'BAS.DEX' : 'BASF',
    #'BAYN.DEX' : 'Bayer',
    #'BMW.FRK' : 'BMW',
    #'0MPT.LON' : 'Brenntag',
    #'CTTAF' : 'Continental',
    #'0RBE.LON' : 'Covestro',
    #'0NXX.LON' : 'Daimler',
    #'0RTC.LON' : 'Delivery Hero',
    #'0H7D.LON' : 'Deutsche Bank',
    #'DB1.DEX' : 'Deutsche Börse',
    #'0H3Q.LON' : 'Deutsche Post',
    #'0MPP.LON' : 'E.on',
    #'0H9X.LON' : 'Fresenius Medical Care',
    #'FSNUF' : 'Fresenius',
    #'0MG2.LON' : 'HeidelbergCement',
    #'HFG.DEX' : 'HelloFresh',
    #'HEN.DEX' : 'Henkel',
    #'0KED.LON' : 'Infineon',
    #'LIN.DEX' : 'Linde',
    #'6MK.DEX' : 'Merck',
    #'0FC9.LON' : 'MTU Aero Engines',
    #'MUV2.DEX' : 'Münchener Rückversicherungs-Gesellschaft',
    #'POAHF' : 'Porsche',
    #'PUM.DEX' : 'PUMA',
    #'QGEN' : 'QIAGEN',
    #'RWE.FRK' : 'RWE',
    #'SAP.DEX' : 'SAP',
    #'SRT3.DEX' : 'Sartorius',
    #'0P6M.LON' : 'Siemens',
    #'ENR.DEX' : 'Siemens Energy',
    #'SEMHF' : 'Siemens Healthineers',
    #'0G6T.LON' : 'Symrise',
    #'TSLA' : 'Tesla',
    #'VOW3.DEX' : 'Volkswagen',
    #'0QFT.LON' : 'Vonovia',
    #'0QXN.LON' : 'Zalando'
}
cryptos = {
    'BTC' : 'Bitcoin',
    #'ETH' : 'Ethereum',
    #'BNB' : 'Binance Coin',
    #'ADA' : 'Cardano',
    #'DOGE' : 'Dogecoin'
}


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
    for symbol in cryptos.keys():
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
        back.append([cryptos[symbol], str(close), char, dif])
    return back

def get_both(stocks, cryptos):
    back = get_stock(stocks)
    for x in get_cryptos(cryptos):
        back.append(x)
    return back
