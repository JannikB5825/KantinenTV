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
import fetcher
import math
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

weatherColors={
    2 : "gewitter.jpg", #Gewitter 
    3 : "regen.jpg", #Nisel regen
    5 : "regen.jpg", #Regen 
    6 : "schnee.jpg", #Schnee
    7 : "nebel.jpg", #Nebel
    8 : "sonnig.jpg", #Sonnig
    9 : "wolcken.jpg" #Wolken
}

changeSpeed = 3000

app = QApplication(sys.argv)
screen = app.screens()[0]
dpi = screen.physicalDotsPerInch()
app.quit()

normalScreenDPI = 157.74020756611984
faktor = normalScreenDPI / dpi
font17 = int(math.ceil(17*faktor))
font18 = int(math.ceil(18*faktor))
font20 = int(math.ceil(20*faktor))
font25 = int(math.ceil(25*faktor))
font40 = int(math.ceil(40*faktor))
font100 = int(math.ceil(100*faktor))

#Create an instance of tkinter frame
root = Tk()
root.tk.call('tk', 'scaling', '-displayof', '.', dpi/72.0)
root.geometry(screensize)


#Create a canvas
canvas= Canvas(root,width=root.winfo_screenwidth(),height=root.winfo_screenheight())
canvas.place(x =0, y = 0)
aplicacion = stockticker.AplicationTkinter(root,faktor)


#Load an image in the script
wetter = canvas.create_image(358,900,anchor="e",image=ImageTk.PhotoImage(Image.open(osPath + "Wetter\\sonnig.jpg")))
newWetterBild = Image.open(osPath + "Wetter\\sonnig.jpg")
bg_img= ImageTk.PhotoImage(Image.open(osPath + "Icon\\Black_Bars.png"))
bg = canvas.create_image(0,0,anchor=NW,image=bg_img)
titel = canvas.create_text(1030,450, text="", font=(f'bold {font17}'), anchor='w')
newNewsImage = ImageTk.PhotoImage(Image.open(osPath + "Icon\\Download.png"))
newsImage = canvas.create_image(700,450,anchor=CENTER,image=newNewsImage)

#Loads Football table
distance = 22
heightOfRow = 18


def getTeams():
    tableTeams = []
    for x in range(0,18):
        temp = 110+(distance * x + heightOfRow * x)
        tableTeams.append(canvas.create_text(50,temp, text="123", font=f'bold {font18}', anchor='w', fill="white"))
    return tableTeams


def getPoints():
    tablePoints = []
    for x in range(0,18):
        temp = 110+(distance * x + heightOfRow * x)
        tablePoints.append(canvas.create_text(350,temp, text="1", font=f'bold {font18}', anchor='e', fill="white"))
    return tablePoints


def getLogos():
    logos = []
    tableLogos = []
    for x in range(0,18):
        temp = 110+(distance * x + heightOfRow * x)
        baseheight = 30
        logos.append(Image.open(osPath + "Wappen\\Augsburg.png"))
        hpercent = (baseheight/float(logos[x].size[1]))
        wsize = int((float(logos[x].size[0])*float(hpercent)))
        logos[x] = logos[x].resize((wsize,baseheight), Image.ANTIALIAS)
        logos[x]= ImageTk.PhotoImage(logos[x])
        tableLogos.append(canvas.create_image(24,temp,anchor=CENTER, image=logos[x]))
    return logos, tableLogos


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
        x = [json["weather"][0]["description"], json["weather"][0]["icon"],json["main"]["temp"],int(json["weather"][0]["id"])]
        return x
    else:
        return None


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
        return final
    else:
        return None 


def update_clock():
    time_text = time.strftime("%H") + ":" + time.strftime("%M")
    canvas.itemconfigure(clock, text=time_text)
    digital_clock_lbl.after(1000, update_clock)


def get_all_article():
    url = 'https://newsapi.org/v2/top-headlines?country=de&apiKey=cc1ce8c5d19b4a198fcd040fcbb47a6a'
    result = requests.get(url, verify=False)        
    if result:
        json = json_.loads(result.text)
        articles = []
        for x in json["articles"]:
            if x["urlToImage"] != "null":
                articles.append([x["title"],
                                 x["description"],
                                 x["author"],
                                 x["publishedAt"],
                                 x["urlToImage"],
                ])
        return articles


def setTeams():
    url3 = "https://api.openligadb.de/getbltable/bl1/2021"
    time.sleep(1)
    result = requests.get(url3, verify=False)
    tableTeams = getTeams()
    if result:
        json = json_.loads(result.text)
        for i in range(0,18):
            canvas.itemconfig(tableTeams[i], text = json[i]["shortName"])


def setPoints():
    url3 = "https://api.openligadb.de/getbltable/bl1/2021"
    time.sleep(1)
    result = requests.get(url3, verify=False)
    tablePoints = getPoints()
    if result:
        json = json_.loads(result.text)
        for i in range(0,18):
            canvas.itemconfig(tablePoints[i], text = json[i]["points"])


def setLogos():
    url3 = "https://api.openligadb.de/getbltable/bl1/2021"
    time.sleep(1)
    result = requests.get(url3, verify=False)
    if result:
        json = json_.loads(result.text)
        for i in range(0,18):
            baseheight = 32
            logoName = json[i]["shortName"]
            logos[i] = Image.open(osPath + f"Wappen\\{logoName}.png")
            wpercent = (baseheight/float(logos[i].size[1]))
            hsize = int((float(logos[i].size[0])*float(wpercent)))
            logos[i] = logos[i].resize((hsize,baseheight), Image.ANTIALIAS)
            logos[i]= ImageTk.PhotoImage(logos[i])
            canvas.itemconfig(tableLogos[i], image = logos[i])


def addLineBreaks(title, desc, date, publisher):
    titleArr = title.split()
    descArr = desc.split()
    back = ""
    temp = ""
    for x in titleArr:
        if len(temp+x) > 50:
            back += temp + "\n"
            temp = x + " "
        else:
            temp += x + " "
    back += temp + "\n\n"
    temp = ""
    for x in descArr:
        if len(temp+x) > 50:
            back += temp + "\n"
            temp = x + " "
        else:
            temp += x + " "
    back += temp + "\n\n-" + publisher + " " + date[:10].replace("-",".")
    return back


def show_articles(articles):
    global newNewsImage, changeSpeed
    configWeather()
    nowArticle = articles.pop(0)
    articles.append(nowArticle)
    if nowArticle[2] == "Bender123":
        nowArticle[2] = "Bender"
    if 'None' in nowArticle or None in nowArticle:
        root.after(0,lambda: show_articles(articles))
    elif "Bender123" in nowArticle[4]:
        try:
            basewidth = 600
            newNewsImage = Image.open(osPath + "//Icon//myBender.jpg")
            wpercent = (basewidth/float(newNewsImage.size[0]))
            hsize = int((float(newNewsImage.size[1])*float(wpercent)))
            newNewsImage = newNewsImage.resize((basewidth,hsize), Image.ANTIALIAS)
            newNewsImage= ImageTk.PhotoImage(newNewsImage)
            canvas.itemconfig(newsImage, image = newNewsImage)
            canvas.itemconfig(titel, text = addLineBreaks(nowArticle[0],nowArticle[1],nowArticle[3],nowArticle[2]))
        except:
            None
        root.after(changeSpeed,lambda: show_articles(articles))
    elif "intra.mybender" in nowArticle[4]:
        try:
            raw_data = fetcher.send_request(nowArticle[4]).content
            basewidth = 600
            newNewsImage = Image.open(io.BytesIO(raw_data))
            wpercent = (basewidth/float(newNewsImage.size[0]))
            hsize = int((float(newNewsImage.size[1])*float(wpercent)))
            newNewsImage = newNewsImage.resize((basewidth,hsize), Image.ANTIALIAS)
            newNewsImage= ImageTk.PhotoImage(newNewsImage)
            canvas.itemconfig(newsImage, image = newNewsImage)
            canvas.itemconfig(titel, text = addLineBreaks(nowArticle[0],nowArticle[1],nowArticle[3],nowArticle[2]))
        except:
            print(nowArticle)
            print("fail")
        root.after(changeSpeed,lambda: show_articles(articles))
    else:
        try:
            raw_data = urllib.request.urlopen(nowArticle[4]).read()
            basewidth = 600
            newNewsImage = Image.open(io.BytesIO(raw_data))
            wpercent = (basewidth/float(newNewsImage.size[0]))
            hsize = int((float(newNewsImage.size[1])*float(wpercent)))
            newNewsImage = newNewsImage.resize((basewidth,hsize), Image.ANTIALIAS)
            newNewsImage= ImageTk.PhotoImage(newNewsImage)
            canvas.itemconfig(newsImage, image = newNewsImage)
            canvas.itemconfig(titel, text = addLineBreaks(nowArticle[0],nowArticle[1],nowArticle[3],nowArticle[2]))
        except:
            print(nowArticle)
            print("fail")
        root.after(changeSpeed,lambda: show_articles(articles))


def drawTable():
    setPoints()
    setTeams()
    canvas.create_rectangle(4,90,45,810,width = 4)
    canvas.create_rectangle(45,810,300,90,width = 4)
    canvas.create_rectangle(300,90,357,810,width = 4)


def configWeather():
    currentWeather = get_current()
    canvas.itemconfig(currentWeatherArray[0], text= f'{int(currentWeather[2]//1)}°')
    canvas.itemconfig(currentWeatherArray[1], text= currentWeather[0])
    setWeatherPicture()


def setWeatherPicture():
    global newWetterBild, wetter
    if currentWeather[3]//100 == 8 and currentWeather[3]%100 != 0:
        basewidth = 700
        newWetterBild = Image.open(osPath + "Wetter//" + weatherColors[9])
        wpercent = (basewidth/float(newWetterBild.size[0]))
        hsize = int((float(newWetterBild.size[1])*float(wpercent)))
        newWetterBild = newWetterBild.resize((basewidth,hsize), Image.ANTIALIAS)
        newWetterBild= ImageTk.PhotoImage(newWetterBild)
        canvas.itemconfig(wetter,image=newWetterBild)
    else:
        basewidth = 700
        newWetterBild = Image.open(osPath + "Wetter//" + weatherColors[currentWeather[3]//100])
        wpercent = (basewidth/float(newWetterBild.size[0]))
        hsize = int((float(newWetterBild.size[1])*float(wpercent)))
        newWetterBild = newWetterBild.resize((basewidth,hsize), Image.ANTIALIAS)
        newWetterBild= ImageTk.PhotoImage(newWetterBild)
        canvas.itemconfig(wetter,image=newWetterBild)


weather = get_weather()
dateWeather = get_date()
benderNews = fetcher.getBothDates()
articles = get_all_article()
spacing = len(articles) / len(benderNews)

for x in range(1,len(benderNews)+1):
    articles.insert(int(x*spacing)+x, benderNews[x-1])

image = Image.open(osPath + "Wappen\\Feld.jpg")
image = image.resize((354, 720), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
canvas.create_image(4,90, image=my_img, anchor=NW)
logos, tableLogos = getLogos()
setLogos()
drawTable()
currentWeather = get_current()

currentWeatherArray = [
    canvas.create_text(165, 920, text=f'{int(currentWeather[2]//1)}°', font=f'bold {font40}', anchor=CENTER),
    canvas.create_text(165, 1050, text=currentWeather[0], font=f'bold {font18}', anchor=CENTER),
    canvas.create_text(165, 1000, text=f'{int(weather[0]//1)}° / {int(weather[1]//1)}°', font=f'bold {font25}', anchor=CENTER)
]
setWeatherPicture()


for x in range(2,7):
    abstand = (x-2) * 313
    weather[x*3] = ImageTk.PhotoImage(Image.open(osPath + f"Icon\\{weather[x*3]}@2x.png"))
    canvas.create_image(365 + abstand, 960,anchor=NW,image=weather[x*3])
    canvas.create_text(560 + abstand, 1010, text=f'{int(weather[x*3 - 2]//1)}° / {int(weather[x*3 - 1]//1)}°', font=f'bold {font20}', anchor=CENTER)


digital_clock_lbl = Label(text="00:00")
clock = canvas.create_text(1900, 0, text=digital_clock_lbl["text"], font=f'ds-digital {font100}', anchor=NE)
update_clock()


canvas.create_text(178, 40, text="Bundesliga:", font=f'bold {font25}', anchor=CENTER)
canvas.create_text(165, 835, text="Heute:", font=f'bold {font20}', anchor=CENTER)
canvas.create_text(515, 945, text="Morgen:", font=f'bold {font20}', anchor=CENTER)
canvas.create_text(828, 945, text=f'{dateWeather[0]}:', font=f'bold {font20}')
canvas.create_text(1142, 945, text=f'{dateWeather[1]}:', font=f'bold {font20}')
canvas.create_text(1455, 945, text=f'{dateWeather[2]}:', font=f'bold {font20}')
canvas.create_text(1763, 945, text=f'{dateWeather[3]}:', font=f'bold {font20}')

canvas.config(background="#18c8db")


root.attributes('-fullscreen', True)
root.after(5000,lambda: show_articles(articles))
root.mainloop()
