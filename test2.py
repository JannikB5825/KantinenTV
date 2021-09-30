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

user32 = ctypes.windll.user32
screensize = str(user32.GetSystemMetrics(0)) + "x" + str(user32.GetSystemMetrics(1))
osPath = os.path.dirname(os.path.abspath(__file__)).replace("/","\\")
osPath = osPath.replace("\\","\\")+"\\"


#Create an instance of tkinter frame
root = Tk()

app = QApplication(sys.argv)
screen = app.screens()[0]
dpi = screen.physicalDotsPerInch()
app.quit()
root.tk.call('tk', 'scaling', '-displayof', '.', dpi/72.0)
root.geometry(screensize)

#Create a canvas
canvas= Canvas(root,width=root.winfo_screenwidth(),height=root.winfo_screenheight())
canvas.place(x =0, y = 0)
url = 'https://newsapi.org/v2/top-headlines?country=de&apiKey=cc1ce8c5d19b4a198fcd040fcbb47a6a'
result = requests.get(url, verify=False)        
json = json_.loads(result.text)
raw_data = urllib.request.urlopen(json["articles"][0]["urlToImage"]).read()

    
basewidth = 700
img = Image.open(io.BytesIO(raw_data))
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img= ImageTk.PhotoImage(img)
canvas.create_image(0,0,anchor=NW,image=img)

root.mainloop()
