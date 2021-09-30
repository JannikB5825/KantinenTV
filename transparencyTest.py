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
import ctypes
import os
import stockticker

user32 = ctypes.windll.user32
screensize = str(user32.GetSystemMetrics(0)) + "x" + str(user32.GetSystemMetrics(1))
osPath = os.path.dirname(os.path.abspath(__file__)).replace("/","\\")
osPath = osPath.replace("\\","\\")+"\\"

kuerzel ={
    "Monday" : "Mo.",
    "Tuesday" : "Di.",
    "Wednesday" : "Mi.",
    "Thursday" : "Do.",
    "Friday" : "Fr.",
    "Saturday" : "Sa.",
    "Sunday" : "So."
}


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
aplicacion = stockticker.AplicationTkinter(root)


#Load an image in the script
img= ImageTk.PhotoImage(Image.open(osPath + "Icon\\Black_Bars.png"))
canvas.create_image(0,0,anchor=NW,image=img)


def get_weather():
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=50.59&lon=8.95&lang=de&exclude=current,minutely,hourly,alerts&units=metric&appid=013c319d6be43d6ff15ca9d6325c8fb2'
    result = requests.get(url, verify=False)
    if result:
        json = json_.loads(result.text)
        final = [json['daily'][0]['temp']["max"],json['daily'][0]['temp']["min"],json['daily'][0]['weather'][0]['icon'],json['daily'][0]['weather'][0]['description']]
        for x in range(1,6):
            final.append(json['daily'][x]['temp']["max"])
            final.append(json['daily'][x]['temp']["min"])
            final.append(json['daily'][x]['weather'][0]['icon'])
        return final
    else:
        return None


def get_current():
    time.sleep(1)
    url = 'https://api.openweathermap.org/data/2.5/weather?q=gruenberg&lang=de&units=metric&appid=013c319d6be43d6ff15ca9d6325c8fb2'
    result = requests.get(url, verify=False)
    if result:
        json = json_.loads(result.text)
        x = [json["weather"][0]["description"], json["weather"][0]["icon"],json["main"]["temp"]]
        return x
    else:
        return None
    
weather = get_weather()
currentWeather = get_current()

img2 = ImageTk.PhotoImage(Image.open(osPath + f"Icon\\{currentWeather[1]}@2x.png"))
canvas.create_image(65,850,anchor=NW,image=img2)
canvas.create_text(260, 880, text=f'{int(currentWeather[2]//1)}°', font=("bold 15"))
canvas.create_text(175, 980, text=currentWeather[0], font=('bold 12'))
canvas.create_text(165, 1050, text='Grünberg', font='bold, 12')
canvas.create_text(250, 930, text=f'{int(weather[0]//1)}° / {int(weather[1]//1)}°', font=("bold", 12))

# ↑ current status
##############################################################################################################################################
# ↓ next days

weather[6] = ImageTk.PhotoImage(Image.open(osPath + f"Icon\\{weather[6]}@2x.png"))
canvas.create_image(400,950,anchor=NW,image=weather[6])
canvas.create_text(550, 1000, text=f'{int(weather[4]//1)}° / {int(weather[5]//1)}°', font=("bold", 12))


weather[9] = ImageTk.PhotoImage(Image.open(osPath + f"Icon\\{weather[9]}@2x.png"))
canvas.create_image(720,950,anchor=NW,image=weather[9])
canvas.create_text(870, 1000, text=f'{int(weather[7]//1)}° / {int(weather[8]//1)}°', font=("bold", 12))


weather[12] = ImageTk.PhotoImage(Image.open(osPath + f"Icon\\{weather[12]}@2x.png"))
canvas.create_image(1050,950,anchor=NW,image=weather[12])
canvas.create_text(1200, 1000, text=f'{int(weather[10]//1)}° / {int(weather[11]//1)}°', font=("bold", 12))

weather[15] = ImageTk.PhotoImage(Image.open(osPath + f"Icon\\{weather[15]}@2x.png"))
canvas.create_image(1350,950,anchor=NW,image=weather[15])
canvas.create_text(1500, 1000, text=f'{int(weather[13]//1)}° / {int(weather[14]//1)}°', font=("bold", 12))

weather[18] = ImageTk.PhotoImage(Image.open(osPath + f"Icon\\{weather[18]}@2x.png"))
canvas.create_image(1650,950,anchor=NW,image=weather[18])
canvas.create_text(1800, 1000, text=f'{int(weather[16]//1)}° / {int(weather[17]//1)}°', font=("bold", 12))

#################################################################################################################################
# ↓ clock

def update_clock():
    time_text = time.strftime("%H") + ":" + time.strftime("%M")
    canvas.itemconfigure(clock, text=time_text)
    digital_clock_lbl.after(1000, update_clock)


digital_clock_lbl = Label(text="00:00", font=("bold 12"))
clock = canvas.create_text(55, 1050, text=digital_clock_lbl["text"], font=("bold", 12))

update_clock()

#####################################################################################################################################
# ↓ date


canvas.create_text(140, 835, text="Heute:", font=("bold, 15"))
canvas.create_text(500, 945, text="Morgen:", font=("bold, 15"))

def get_date():
    global kuerzel
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=50.59&lon=8.95&lang=de&exclude=current,minutely,hourly,alerts&units=metric&appid=013c319d6be43d6ff15ca9d6325c8fb2'
    time.sleep(1)
    result = requests.get(url, verify=False)
    if result:
        json = json_.loads(result.text)
        final = []
        for x in range(2,6):
            final.append(kuerzel[datetime.utcfromtimestamp(int(json['daily'][x]['dt'])).strftime('%A')] + 
                         " " + 
                         datetime.utcfromtimestamp(int(json['daily'][x]['dt'])).strftime('%d.%m'))
        i = final
        return i
    else:
        return None 

dateWeather = get_date()

canvas.create_text(820, 945, text=f'{dateWeather[0]}:', font=("bold", 15))
canvas.create_text(1150, 945, text=f'{dateWeather[1]}:', font=("bold", 15))
canvas.create_text(1450, 945, text=f'{dateWeather[2]}:', font=("bold", 15))
canvas.create_text(1750, 945, text=f'{dateWeather[3]}:', font=("bold", 15))

canvas.config(background='gray')
root.attributes('-fullscreen', True)
root.mainloop()