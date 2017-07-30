# coding: utf-8
import requests
import time
import bs4
import json
import sys
import Tkinter

class Exchange_list:
    Exchange = set()

class Exchange:
    name = ""
    url = ""
    coins = set([])

    def __init__(self, name):
        self.name = name.upper()

    def set_name(self, name):
        self.name = name

    def set_url(self, url):
        self.url = url

    def add_coin(self, coin):
        self.coins.add(coin)

    def get_coins(self):
        return self.coins

    def get_coin_number(self, coin):
        return self.coin.length()

    def set_price(self):
        for index in self.coins:
            index.set_price()

    def show_price(self):
        for index in self.coins:
            index.show_price()



class Coin:
    name = ""
    api_ticker = ""
    api_key = list()
    price = 0.0
    type = ""
    def __init__(self, name, type, api_ticker, api_key):
        self.name = name.upper()
        self.type = type
        self.api_ticker = api_ticker
        self.api_key = api_key

    def set_price(self):
        request = requests.get(self.api_ticker)
        if request.status_code != 200 and request.ok == True:
            return request.status_code
        data = request.json()
        for key in self.api_key:
            data = data[key]
        self.price = data

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def show_price(self):
        if self.type == "₩":
            print(self.get_name() + "price = " + str(self.price) + "₩")
            return
        if self.type == "$":
            print(self.get_name() + "price = $" + str(self.price))

class Frame:
    def __init__(self):

    def createWidgets(self)
        self.QUIT = Button(self)


if __name__ == "__main__":

    print '--Setup--'
    reload(sys)
    sys.setdefaultencoding('utf-8')
    Poloniex = Exchange("Poloniex")
    Poloniex_BTC = Coin('Poloniex_BTC', "$", 'https://poloniex.com/public?command=returnTicker', ['USDT_BTC', 'last'])
    Poloniex_ETH = Coin('Poloniex_ETH', "$", 'https://poloniex.com/public?command=returnTicker', ['USDT_ETH', 'last'])
    Poloniex_XRP = Coin('Poloniex_XRP', "$", 'https://poloniex.com/public?command=returnTicker', ['USDT_XRP', 'last'])
    Poloniex_ETC = Coin('Poloniex_ETC', "$", 'https://poloniex.com/public?command=returnTicker', ['USDT_ETC', 'last'])
    Poloniex_LTC = Coin('Poloniex_LTC', "$", 'https://poloniex.com/public?command=returnTicker', ['USDT_LTC', 'last'])
    Poloniex_DASH = Coin('Poloniex_DASH', "$", 'https://poloniex.com/public?command=returnTicker', ['USDT_DASH', 'last'])
    sys.stdout.write("*")
    Poloniex.add_coin(Poloniex_BTC)
    Poloniex.add_coin(Poloniex_ETH)
    Poloniex.add_coin(Poloniex_XRP)
    Poloniex.add_coin(Poloniex_ETC)
    Poloniex.add_coin(Poloniex_LTC)
    Poloniex.add_coin(Poloniex_DASH)
    Poloniex.set_price()
    sys.stdout.write("*")

    Bithumb = Exchange("Bithumb")
    Bithumb_BTC = Coin('Bithumb_BTC', "₩", 'https://api.bithumb.com/public/ticker?currency=BTC', ['data', 'closing_price'])
    Bithumb_ETH = Coin('Bithumb_ETH', "₩", 'https://api.bithumb.com/public/ticker?currency=ETH', ['data', 'closing_price'])
    Bithumb_XRP = Coin('Bithumb_XRP', "₩", 'https://api.bithumb.com/public/ticker?currency=XRP', ['data', 'closing_price'])
    Bithumb_ETC = Coin('Bithumb_ETC', "₩", 'https://api.bithumb.com/public/ticker?currency=ETC', ['data', 'closing_price'])
    Bithumb_LTC = Coin('Bithumb_LTC', "₩", 'https://api.bithumb.com/public/ticker?currency=LTC', ['data', 'closing_price'])
    Bithumb_DASH = Coin('Bithumb_DASH', "₩", 'https://api.bithumb.com/public/ticker?currency=DASH', ['data', 'closing_price'])
    sys.stdout.write("*")
    Bithumb.add_coin(Bithumb_BTC)
    Bithumb.add_coin(Bithumb_ETH)
    Bithumb.add_coin(Bithumb_XRP)
    Bithumb.add_coin(Bithumb_ETC)
    Bithumb.add_coin(Bithumb_LTC)
    Bithumb.add_coin(Bithumb_DASH)
    Bithumb.set_price()
    sys.stdout.write("*")

    Coinone = Exchange("Coinone")
    Coinone_BTC = Coin('Coinone_BTC', "₩", 'https://api.coinone.co.kr/ticker?currency=BTC', ['last'])
    Coinone_ETH = Coin('Coinone_ETH', "₩", 'https://api.coinone.co.kr/ticker?currency=ETH', ['last'])
    Coinone_XRP = Coin('Coinone_XRP', "₩", 'https://api.coinone.co.kr/ticker?currency=XRP', ['last'])
    Coinone_ETC = Coin('Coinone_ETC', "₩", 'https://api.coinone.co.kr/ticker?currency=ETC', ['last'])
    sys.stdout.write("*")
    Coinone.add_coin(Coinone_BTC)
    Coinone.add_coin(Coinone_ETH)
    Coinone.add_coin(Coinone_XRP)
    Coinone.add_coin(Coinone_ETC)
    Coinone.set_price()
    sys.stdout.write("*")

    OKCoin = Exchange("OKCoin")
    OKCoin_BTC = Coin('OKCoin_BTC', "$", 'https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd', ['ticker', 'last'])
    OKCoin_ETH = Coin('OKCoin_ETH', "$", 'https://www.okcoin.com/api/v1/ticker.do?symbol=eth_usd', ['ticker', 'last'])
    OKCoin_ETC = Coin('OKCoin_ETC', "$", 'https://www.okcoin.com/api/v1/ticker.do?symbol=etc_usd', ['ticker', 'last'])
    OKCoin_LTC = Coin('OKCoin_LTC', "$", 'https://www.okcoin.com/api/v1/ticker.do?symbol=ltc_usd', ['ticker', 'last'])
    sys.stdout.write("*")
    OKCoin.add_coin(OKCoin_BTC)
    OKCoin.add_coin(OKCoin_ETH)
    OKCoin.add_coin(OKCoin_ETC)
    OKCoin.add_coin(OKCoin_LTC)
    OKCoin.set_price()
    sys.stdout.write("*")

    bitFlyer = Exchange("bitFlyer")
    bitFlyer_BTC = Coin('bitFlyer_BTC', "$", 'https://api.bitflyer.jp/v1/ticker?productcode=btc_jpy', ['ltp'])
    bitFlyer_ETH = Coin('bitFlyer_ETH', "$", 'https://api.bitflyer.jp/v1/ticker?productcode=eth_jpy', ['ltp'])
    bitFlyer_XRP = Coin('bitFlyer_XRP', "$", 'https://api.bitflyer.jp/v1/ticker?productcode=xrp_jpy', ['ltp'])
    bitFlyer_ETC = Coin('bitFlyer_ETC', "$", 'https://api.bitflyer.jp/v1/ticker?productcode=etc_jpy', ['ltp'])
    bitFlyer_LTC = Coin('bitFlyer_LTC', "$", 'https://api.bitflyer.jp/v1/ticker?productcode=ltc_jpy', ['ltp'])
    bitFlyer_DASH = Coin('bitFlyer_DASH', "$", 'https://api.bitflyer.jp/v1/ticker?productcode=dash_jpy', ['ltp'])
    sys.stdout.write("*")
    bitFlyer.add_coin(bitFlyer_BTC)
    bitFlyer.add_coin(bitFlyer_ETH)
    bitFlyer.add_coin(bitFlyer_XRP)
    bitFlyer.add_coin(bitFlyer_ETC)
    bitFlyer.add_coin(bitFlyer_LTC)
    bitFlyer.add_coin(bitFlyer_DASH)
    bitFlyer.set_price()
    sys.stdout.write("*")

    Bitfinex = Exchange("Bitfinex")
    Bitfinex_BTC = Coin('Bitfinex_BTC', "$", 'https://api.bitfinex.com/v1/pubticker/BTCUSD', ['last_price'])
    Bitfinex_ETH = Coin('Bitfinex_ETH', "$", 'https://api.bitfinex.com/v1/pubticker/ETHUSD', ['last_price'])
    Bitfinex_ETC = Coin('Bitfinex_ETC', "$", 'https://api.bitfinex.com/v1/pubticker/ETCUSD', ['last_price'])
    Bitfinex_LTC = Coin('Bitfinex_LTC', "$", 'https://api.bitfinex.com/v1/pubticker/LTCUSD', ['last_price'])
    Bitfinex.add_coin(Bitfinex_BTC)
    Bitfinex.add_coin(Bitfinex_ETH)
    Bitfinex.add_coin(Bitfinex_ETC)
    Bitfinex.add_coin(Bitfinex_LTC)
    Bitfinex.set_price()
    sys.stdout.write("*")

    Korbit = Exchange("Korbit")
    Korbit_BTC = Coin('Korbit_BTC', "₩", 'https://api.korbit.co.kr/v1/ticker?currency_pair=btc_krw', ['last'])
    Korbit_ETH = Coin('Korbit_ETH', "₩", 'https://api.korbit.co.kr/v1/ticker?currency_pair=eth_krw', ['last'])
    Korbit_XRP = Coin('Korbit_XRP', "₩", 'https://api.korbit.co.kr/v1/ticker?currency_pair=xrp_krw', ['last'])
    Korbit_ETC = Coin('Korbit_ETC', "₩", 'https://api.korbit.co.kr/v1/ticker?currency_pair=etc_krw', ['last'])
    sys.stdout.write("*")
    Korbit.add_coin(Korbit_BTC)
    Korbit.add_coin(Korbit_ETH)
    Korbit.add_coin(Korbit_XRP)
    Korbit.add_coin(Korbit_ETC)
    Korbit.set_price()
    sys.stdout.write("*")
    print '--Setup Complete--'


    while True:

        Poloniex.show_price()
        Bithumb.show_price()
        Coinone.show_price()
        OKCoin.show_price()
        bitFlyer.show_price()
        Bitfinex.show_price()
        Korbit.show_price()

        time.sleep(1)
