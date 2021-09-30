from tkinter import *
import time
import threading
from random import randint as randint, uniform as randlimit
import stockAPI
import ctypes

user32 = ctypes.windll.user32
CHAR_UP = "\u25B2"
CHAR_DOWN = "\u25BC"
CHAR_EVEN = "="
SPEED = 100
FONTSIZE = 25
stock_market = stockAPI.get_both(stockAPI.stocks, stockAPI.cryptos)

class AplicationTkinter(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initGUI()
        self.scroll_ticker()

    def initGUI(self):
        self.frm_1 = Frame(self.parent)
        self.frm_1.place(x=0,y=0)
        self.lblfr_1 = LabelFrame(self.parent)
        self.lblfr_1.place(x=0,y=0)
        self.market_one = StockMarket(stock_market)
        self.txt_ticker_widget = Text(self.lblfr_1, background='black', height=1, width=500, wrap="none", font=("bold",FONTSIZE))
        self.txt_ticker_widget.pack(side=TOP, fill=X)
        self.txt_ticker_widget.tag_configure("up", foreground="green")
        self.txt_ticker_widget.tag_configure("down", foreground="red")
        self.txt_ticker_widget.tag_configure("even", foreground="white")
        self.tag = {CHAR_DOWN: "down", CHAR_EVEN: "even", CHAR_UP: "up"}

    def scroll_ticker(self):
        self.txt_ticker_widget.configure(state=NORMAL)
        self.txt_ticker_widget.insert(END, self.market_one.get_next_character(),
                                      self.tag[self.market_one.get_tag()])  # TODO simplify
        self.txt_ticker_widget.see(END)
        self.txt_ticker_widget.configure(state=DISABLED)
        self.txt_ticker_widget.after(SPEED, self.scroll_ticker)  # recursive each interval of millisecs


class StockTicker():

    def __init__(self, list_data):
        self.symbol, self.price, self.direction, self.change = list_data

    def ticker_to_text(self):
        return " |  {} {} {} {} ".format(self.symbol, self.price, self.direction, self.change)


class StockMarket():
    
    def __init__(self, l_inicial):
        self.smarket = []
        self.load_market(l_inicial)
        self.current_ticker = self.get_one_ticker()

    def load_market(self, l_inicial):
        for data_ticker in l_inicial:
            simple_ticker = StockTicker(data_ticker)
            self.smarket.append(simple_ticker)


    def get_one_ticker(self):
        self.one_ticker = self.smarket.pop(0)
        self.smarket.append(self.one_ticker)
        self.index = 0
        return self.one_ticker.ticker_to_text()

    def get_next_character(self):
        if self.index == len(self.current_ticker):
            self.current_ticker = self.get_one_ticker()
            self.index = 0
        self.character_symbol = self.current_ticker[self.index:self.index+1]
        self.index += 1
        return self.character_symbol

    def get_tag(self):
        return self.one_ticker.direction

#def main():
#    the_window = Tk()
#    aplicacion = AplicationTkinter(the_window)
#    # init the GUI process
#    the_window.mainloop()
#
#if __name__ == '__main__':
#    main()