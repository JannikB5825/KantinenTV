#Import the required Libraries
from tkinter import *
import tkinter as ui
from tkinter import messagebox 
from configparser import ConfigParser
import json as json_
import requests
import time
from PIL import ImageTk,Image
import sys
from PyQt5.QtWidgets import QApplication
from datetime import datetime

app = QApplication(sys.argv)
screen = app.screens()[0]
dpi = screen.physicalDotsPerInch()
app.quit()
#Create an instance of tkinter frame
root = Tk()
root.tk.call('tk', 'scaling', '-displayof', '.', dpi/72.0)
#Set the geometry of tkinter frame
root.geometry("1920x1080")

#Create a canvas
canvas= Canvas(root,width=root.winfo_screenwidth(),height=root.winfo_screenheight())
canvas.pack()


#Load an image in the script
img= ImageTk.PhotoImage(Image.open("C:\\KantinenTv\\KantinenTV-1\\Icon\\Black_Bars.png"))

#Add image to the Canvas Items
canvas.create_image(0,0,anchor=NW,image=img)


url = 'https://api.openweathermap.org/data/2.5/onecall?lat=50.59&lon=8.95&lang=de&exclude=current,minutely,hourly,alerts&units=metric&appid=013c319d6be43d6ff15ca9d6325c8fb2'

def get_weather():
    time.sleep(1)
    result = requests.get(url, verify=False)
    if result:
        json = json_.loads(result.text)
        # Stadt, Land, Temperatur, icon, Wetter
        max_temp = json['daily'][0]['temp']["max"]
        min_temp = json['daily'][0]['temp']["min"]
        icon = json['daily'][0]['weather'][0]['icon']
        description = json['daily'][0]['weather'][0]['description']
        max_temp1 = json['daily'][1]['temp']["max"]
        min_temp1 = json['daily'][1]['temp']["min"]
        icon1 = json['daily'][1]['weather'][0]['icon']
        max_temp2 = json['daily'][2]['temp']["max"]
        min_temp2 = json['daily'][2]['temp']["min"]
        icon2 = json['daily'][2]['weather'][0]['icon']
        max_temp3 = json['daily'][3]['temp']["max"]
        min_temp3 = json['daily'][3]['temp']["min"]
        icon3 = json['daily'][3]['weather'][0]['icon']
        max_temp4 = json['daily'][4]['temp']["max"]
        min_temp4 = json['daily'][4]['temp']["min"]
        icon4 = json['daily'][4]['weather'][0]['icon']
        max_temp5 = json['daily'][5]['temp']["max"]
        min_temp5 = json['daily'][5]['temp']["min"]
        icon5 = json['daily'][5]['weather'][0]['icon']
        final = [max_temp, min_temp, icon, description, max_temp1, min_temp1, icon1, max_temp2, min_temp2, icon2, max_temp3, min_temp3, icon3, max_temp4, min_temp4, icon4, max_temp5, min_temp5, icon5]
        return final
    else:
        return None

weather = get_weather()
des = weather[3]
ma = weather[0]
mi = weather[1]
ma1 = weather[4]
mi1 = weather[5]
ma2 = weather[7]
mi2 = weather[8]
ma3 = weather[10]
mi3 = weather[11]
ma4 = weather[13]
mi4 = weather[14]
ma5 = weather[16]
mi5 = weather[17]

canvas.create_text(90, 830, text='Grünberg', font='bold, 12')

canvas.create_text(135, 730, text=f'{int(ma//1)}° / {int(mi//1)}°', font=("bold", 12))

url2 = 'https://api.openweathermap.org/data/2.5/weather?q=gruenberg&lang=de&units=metric&appid=013c319d6be43d6ff15ca9d6325c8fb2'

def get_current():
    time.sleep(1)
    result = requests.get(url2, verify=False)
    if result:
        json = json_.loads(result.text)
        #current weather (description, temperature, icon)
        description2 = json["weather"][0]["description"]
        icon_current = json["weather"][0]["icon"]
        temp_current = json["main"]["temp"]
        x = [description2, icon_current, temp_current]
        return x
    else:
        return None

weather2 = get_current()
description = weather2[0]
icon_current = weather2[1]
temp_current = weather2[2]


img2 = ImageTk.PhotoImage(Image.open(f"C:\\KantinenTv\\KantinenTV-1\\Icon\\{icon_current}@2x.png"))
canvas.create_image(30,670,anchor=NW,image=img2)


canvas.create_text(30, 670, text=f'{int(ma//1)}° / {int(mi//1)}°', font=("bold 12"))

canvas.create_text(150, 690, text=f'{int(temp_current//1)}°', font=("bold 12"))

canvas.create_text(52, 760, text=description, font=('bold 15'))



# ↑ current status
##############################################################################################################################################
# ↓ next days


weather[6] = ImageTk.PhotoImage(Image.open(f"C:\\KantinenTv\\KantinenTV-1\\Icon\\{weather[6]}@2x.png"))
canvas.create_image(320,760,anchor=NW,image=weather[6])

max_min_temp = Label(root, text=f'{int(ma1//1)}° / {int(mi1//1)}°', font=("bold", 12))
max_min_temp.config(background='#00d1e8')
max_min_temp.place(x = 420, y = 800)


weather[6] = ImageTk.PhotoImage(Image.open(f"C:\\KantinenTv\\KantinenTV-1\\Icon\\{weather[9]}@2x.png"))
canvas.create_image(570,760,anchor=NW,image=weather[9])


max_min_temp = Label(root, text=f'{int(ma2//1)}° / {int(mi2//1)}°', font=("bold", 12))
max_min_temp.config(background='#00d1e8')
max_min_temp.place(x = 670, y = 800)


weather[12] = ImageTk.PhotoImage(Image.open(f"C:\\KantinenTv\\KantinenTV-1\\Icon\\{weather[12]}@2x.png"))
canvas.create_image(820,760,anchor=NW,image=weather[12])


max_min_temp = Label(root, text=f'{int(ma3//1)}° / {int(mi3//1)}°', font=("bold", 12))
max_min_temp.config(background='#00d1e8')
max_min_temp.place(x = 920, y = 800)


weather[15] = ImageTk.PhotoImage(Image.open(f"C:\\KantinenTv\\KantinenTV-1\\Icon\\{weather[15]}@2x.png"))
canvas.create_image(1070,760,anchor=NW,image=weather[15])


max_min_temp = Label(root, text=f'{int(ma4//1)}° / {int(mi4//1)}°', font=("bold", 12))
max_min_temp.config(background='#00d1e8')
max_min_temp.place(x = 1170, y = 800)

weather[18] = ImageTk.PhotoImage(Image.open(f"C:\\KantinenTv\\KantinenTV-1\\Icon\\{weather[18]}@2x.png"))
canvas.create_image(1320,760,anchor=NW,image=weather[18])


max_min_temp = Label(root, text=f'{int(ma5//1)}° / {int(mi5//1)}°', font=("bold", 12))
max_min_temp.config(background='#00d1e8')
max_min_temp.place(x = 1420, y = 800)


#################################################################################################################################
# ↓ clock

def update_clock():
    hours = time.strftime("%H")
    minutes = time.strftime("%M")
    time_text = hours + ":" + minutes
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)


digital_clock_lbl = Label(text="00:00", font=("bold 12"))
digital_clock_lbl.config(bg="#00d1e8")
digital_clock_lbl.place(x = 30, y = 830)

update_clock()

#####################################################################################################################################
# ↓ date


heute = Label(text="Heute:", font=("bold, 15"))
heute.config(bg='#00d1e8')
heute.place(x = 90, y = 660)

morgen = Label(text="Morgen:", font=("bold, 15"))
morgen.config(bg='#00d1e8')
morgen.place(x = 365, y =750)

def get_date():
    time.sleep(1)
    result = requests.get(url, verify=False)
    if result:
        json = json_.loads(result.text)
        # Datum
        date = json['daily'][2]['dt']
        date1 = json['daily'][3]['dt']
        date2 = json['daily'][4]['dt']
        date3 = json['daily'][5]['dt']
        i = [date, date1, date2, date3]
        return i
    else:
        return None 

ts = get_date()
datum = ts[0]
datum2 = ts[1]
datum3 = ts[2]
datum4 = ts[3]

ts = int(datum)
datum1 = datetime.utcfromtimestamp(ts).strftime('%d.%m')
ts = int(datum2)
datum2 = datetime.utcfromtimestamp(ts).strftime('%d.%m')
ts = int(datum3)
datum3 = datetime.utcfromtimestamp(ts).strftime('%d.%m')
ts = int(datum4)
datum4 = datetime.utcfromtimestamp(ts).strftime('%d.%m')

date = Label(root, text=f'{datum1}:', font=("bold", 15))
date.config(background='#00d1e8')
date.place(x = 620, y = 750)
date = Label(root, text=f'{datum2}:', font=("bold", 15))
date.config(background='#00d1e8')
date.place(x = 870, y = 750)
date = Label(root, text=f'{datum3}:', font=("bold", 15))
date.config(background='#00d1e8')
date.place(x = 1120, y = 750)
date = Label(root, text=f'{datum4}:', font=("bold", 15))
date.config(background='#00d1e8')
date.place(x = 1370, y = 750)


canvas.config(background='gray')
root.attributes('-fullscreen', True)
root.mainloop()