#Import the required Libraries
from tkinter import *
import json as json_
import requests
import time
from PIL import ImageTk,Image
import sys
from PyQt5.QtWidgets import QApplication
from datetime import datetime
import ctypes
import os
import urllib
import io
#import stockticker

user32 = ctypes.windll.user32
screensize = str(user32.GetSystemMetrics(0)) + "x" + str(user32.GetSystemMetrics(1))
normalScreenDPI = 157.74020756611984
faktor = normalScreenDPI / dpi
95.95804195804195
app = QApplication(sys.argv)
screen = app.screens()[0]
dpi = screen.physicalDotsPerInch()
app.quit()

root = Tk()
root.tk.call('tk', 'scaling', '-displayof', '.', dpi/72.0)
root.geometry(screensize)
canvas= Canvas(root,width=root.winfo_screenwidth(),height=root.winfo_screenheight())
canvas.place(x =0, y = 0)
canvas.create_text(0,0,text="test",font="bold 550", anchor=NW)


print(dpi)
root.attributes('-fullscreen', True)
root.mainloop()