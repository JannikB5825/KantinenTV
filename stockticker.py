from tkinter import *
import time
import threading
from random import randint as randint, uniform as randlimit


class AplicationTkinter(Frame):
    """
    Class of tkinter.Frame subclass, Initializes the GUI
    methods:
        initGUI, draws the layout
        scroll_ticker, inserts character by character in the Text widget
    """
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initGUI()
        self.scroll_ticker()

    def initGUI(self):
        # changes the window icon
        self.parent.title("Stock Exchange Ticker")
        # fix a status bar at the bottom of the window, for future improvements
        self.status_bar = Label(self.parent, text="", bd=1, relief=SUNKEN, anchor=W)
        self.status_bar.pack(side=BOTTOM, fill=X)
        # content Frame for entry, for future improvements
        self.frm_1 = Frame(self.parent)
        self.frm_1.pack()
        self.var_entry = StringVar()
        self.ent_1 = Entry(self.frm_1, textvariable=self.var_entry)
        self.ent_1.pack()
        self.var_entry.set("a default value")
        str_ent_1 = self.ent_1.get()
        # content LabelFrame to show the ticker scrolling line of text
        self.lblfr_1 = LabelFrame(self.parent, text="Ventana de Resultados")
        self.lblfr_1.pack()
        # creates an instance of the StockMarket class for contents the the data
        self.market_one = StockMarket(stock_market)
        # the scrolling line of Text for show the data
        self.txt_ticker_widget = Text(self.lblfr_1, background='black', height=1, width=56, wrap="none")
        self.txt_ticker_widget.pack(side=TOP, fill=X)
        self.txt_ticker_widget.tag_configure("up", foreground="#00ff00")
        self.txt_ticker_widget.tag_configure("down", foreground="#ff0000")
        self.txt_ticker_widget.tag_configure("even", foreground="white")
        self.tag = {CHAR_DOWN: "down", CHAR_EVEN: "even", CHAR_UP: "up"}

    def scroll_ticker(self):
        self.txt_ticker_widget.configure(state=NORMAL)
        self.txt_ticker_widget.insert(END, self.market_one.get_next_character(),
                                      self.tag[self.market_one.get_tag()])  # TODO simplify
        self.txt_ticker_widget.see(END)
        self.txt_ticker_widget.configure(state=DISABLED)
        self.txt_ticker_widget.after(SPEED, self.scroll_ticker)  # recursive each interval of millisecs


CHAR_UP = "\u25B2"
CHAR_DOWN = "\u25BC"
CHAR_EVEN = "="
SPEED = 100
UPDATE_TIME = 60

# INITIAL DATA, this must be changed to implement the load of a external source
stock_market = [["GOOG", "587.25", CHAR_UP, "(+12.14)"],
                ["AAPL", "237.14", CHAR_UP, "(+7.25)"],
                ["GTAT", "87.47", CHAR_DOWN, "(-1.18)"],
                ["KNDI", "167.32", CHAR_UP, "(+6.85)"],
                ["ORCL", "482.91", CHAR_DOWN, "(-24.65)"],
                ["FBOK", "327.67", CHAR_DOWN, "(-11.78)"],
                ["TWTR", "842.41", CHAR_UP, "(+15.45)"]]


class StockTicker():

    def __init__(self, list_data):
        self.symbol, self.price, self.direction, self.change = list_data

    def update_ticker(self):
        flt_price = float(self.price)
        if randint(0, 9) == 0:
            self.direction = CHAR_EVEN
        else:
            increase_percent = randlimit(-5, 5)
            # TODO implementar normalvariate(0, 0.02) o gauss(0, 0.02)
            flt_change = flt_price * increase_percent / 100
            flt_new_price = flt_price + flt_change
            self.price = "{:.2f}".format(flt_new_price)
            if flt_change < 0:
                self.direction = CHAR_DOWN
            elif flt_change == 0:
                self.direction = CHAR_EVEN
            else:
                self.direction = CHAR_UP
            self.change = "({:+.2f})".format(flt_change)

    def ticker_to_text(self):
        return " |  {} {} {} {} ".format(self.symbol, self.price, self.direction, self.change)


class StockMarket():

    def __init__(self, l_inicial):
        self.smarket = []
        self.load_market(l_inicial)
        self.current_ticker = self.get_one_ticker()
        self.thread_updating = UpdateThread(self)
        self.thread_updating.start()

    def load_market(self, l_inicial):
        for data_ticker in l_inicial:
            simple_ticker = StockTicker(data_ticker)
            self.smarket.append(simple_ticker)

    def update_market(self):
        for j in range(len(self.smarket)):
            self.smarket[j].update_ticker()

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


class UpdateThread(threading.Thread):
    def __init__(self, market_1):
        self.my_check = " CHECK "   # TODO replace with initial source data.
        self.the_market = market_1
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(UPDATE_TIME)
        self.the_market.update_market()
        print(" UPDATED!!!")    # for debugging
        self.run()


# STARTS THE PROGRAM
def main():
    the_window = Tk()
    aplicacion = AplicationTkinter(the_window)
    # init the GUI process
    the_window.mainloop()

if __name__ == '__main__':
    main()