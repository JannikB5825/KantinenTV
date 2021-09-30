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
  
root = Tk()
canvas= Canvas(root,width=root.winfo_screenwidth(),height=root.winfo_screenheight())
canvas.place(x =0, y = 0)

def get_team():
    url3 = "https://api.openligadb.de/getbltable/bl1/2021"
    time.sleep(1)
    result = requests.get(url3, verify=False)
    if result:
        json = json_.loads(result.text)
        tabelle = []
        for i in range(0,17):
            tabelle.append(json[i]["teamName"])
        return tabelle
    else:
        return None
def get_points():
    url3 = "https://api.openligadb.de/getbltable/bl1/2021"
    time.sleep(1)
    result = requests.get(url3, verify=False)
    if result:
        json = json_.loads(result.text)
        points = []
        for i in range(0,17):
            points.append(json[i]["points"])
        return points
    else:
        return None
    
points = get_points()
team = get_team()

class Table:
      
    def __init__(self,root):
          
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                  
                self.e = Entry(root, width=20, fg='black',
                               font=('Arial',16,'bold'))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

#img2 = ImageTk.PhotoImage(Image.open(osPath + "C:\Users\kai.selenski\OneDrive - Bender GmbH & Co.KG\Desktop\Git\KantinenTV\Wappen\Dortmunt.png"))
#canvas.create_image(65,850,anchor=NW,image=img2)
  
# take the data
lst = [ (team)
]

   
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
   
# create root window
t = Table(root)
root.mainloop()
