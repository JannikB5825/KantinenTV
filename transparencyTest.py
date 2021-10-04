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

#Bilder nochmal überschauen
weatherColors={
    2 : "gewitter.jpg", #Gewitter 
    3 : "regen.jpg", #Nisel regen
    5 : "regen.jpg", #Regen 
    6 : "schnee.jpg", #Schnee
    7 : "nebel.jpg", #Nebel
    8 : "sonnig.jpg", #Sonnig
    9 : "wolcken.jpg" #Wolken
}




app = QApplication(sys.argv)
screen = app.screens()[0]
dpi = screen.physicalDotsPerInch()
app.quit()


#Create an instance of tkinter frame
root = Tk()
root.tk.call('tk', 'scaling', '-displayof', '.', dpi/72.0)
root.geometry(screensize)

#Create a canvas
canvas= Canvas(root,width=root.winfo_screenwidth(),height=root.winfo_screenheight())
canvas.place(x =0, y = 0)
aplicacion = stockticker.AplicationTkinter(root)


#Load an image in the script
wetter = canvas.create_image(360,900,anchor="e",image=ImageTk.PhotoImage(Image.open(osPath + "Icon\\Download.png")))
bg_img= ImageTk.PhotoImage(Image.open(osPath + "Icon\\Black_Bars.png"))
bg = canvas.create_image(0,0,anchor=NW,image=bg_img)
titel = canvas.create_text(1130,450, text="", font=('bold 12'), anchor='w')
newNewsImage = ImageTk.PhotoImage(Image.open(osPath + "Icon\\Download.png"))
newsImage = canvas.create_image(750,450,anchor=CENTER,image=newNewsImage)

#Loads Football table
distance = 22
heightOfRow = 20
tableTeams = []
for x in range(0,18):
    temp = 50+(distance * x + heightOfRow * x)
    tableTeams.append(canvas.create_text(50,temp, text="123", font=('bold 20'), anchor='w'))
tablePoints = []
for x in range(0,18):
    temp = 50+(distance * x + heightOfRow * x)
    tablePoints.append(canvas.create_text(355,temp, text="1", font=('bold 20'), anchor='e'))
tableLogos = []
logos = []
for x in range(0,18):
    temp = 50+(distance * x + heightOfRow * x)
    baseheight = 32
    logos.append(Image.open(osPath + "Wappen\\Augsburg.png"))
    hpercent = (baseheight/float(logos[x].size[1]))
    wsize = int((float(logos[x].size[0])*float(hpercent)))
    logos[x] = logos[x].resize((wsize,baseheight), Image.ANTIALIAS)
    logos[x]= ImageTk.PhotoImage(logos[x])
    tableLogos.append(canvas.create_image(21,temp,anchor=CENTER, image=logos[x]))


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
    

def get_team():
    url3 = "https://api.openligadb.de/getbltable/bl1/2021"
    time.sleep(1)
    result = requests.get(url3, verify=False)
    if result:
        json = json_.loads(result.text)
        tabelle = []
        for i in range(0,18):
            canvas.itemconfig(tableTeams[i], text = json[i]["shortName"])


def get_points():
    url3 = "https://api.openligadb.de/getbltable/bl1/2021"
    time.sleep(1)
    result = requests.get(url3, verify=False)
    if result:
        json = json_.loads(result.text)
        points = []
        for i in range(0,18):
            canvas.itemconfig(tablePoints[i], text = json[i]["points"])
            

def get_logos():
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
        if len(temp+x) > 60:
            back += temp + "\n"
            temp = ""
        else:
            temp += x + " "
    temp = ""
    back += "\n"
    for x in descArr:
        if len(temp+x) > 60:
            back += temp + "\n"
            temp = ""
        else:
            temp += x + " "
    back += "\n-" + publisher + " " + date[:10].replace("-",".")
    return back

def show_articles(articles):
    global newNewsImage
    nowArticle = articles.pop(0)
    articles.append(nowArticle)
    if None in nowArticle:
        root.after(0,lambda: show_articles(articles))
    else:
        raw_data = urllib.request.urlopen(nowArticle[4]).read()
        basewidth = 700
        newNewsImage = Image.open(io.BytesIO(raw_data))
        wpercent = (basewidth/float(newNewsImage.size[0]))
        hsize = int((float(newNewsImage.size[1])*float(wpercent)))
        newNewsImage = newNewsImage.resize((basewidth,hsize), Image.ANTIALIAS)
        newNewsImage= ImageTk.PhotoImage(newNewsImage)
        canvas.itemconfig(newsImage, image = newNewsImage)
        canvas.itemconfig(titel, text = addLineBreaks(nowArticle[0],nowArticle[1],nowArticle[3],nowArticle[2]))
        root.after(5000,lambda: show_articles(articles))
    
    
weather = get_weather()
currentWeather = get_current()
dateWeather = get_date()
articles = get_all_article()
get_points()
get_team()
get_logos()

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

digital_clock_lbl = Label(text="00:00", font=("bold 12"))
clock = canvas.create_text(55, 1050, text=digital_clock_lbl["text"], font=("bold", 12))

update_clock()

#####################################################################################################################################
# ↓ date

canvas.create_text(140, 835, text="Heute:", font=("bold, 15"))
canvas.create_text(500, 945, text="Morgen:", font=("bold, 15"))
canvas.create_text(820, 945, text=f'{dateWeather[0]}:', font=("bold", 15))
canvas.create_text(1150, 945, text=f'{dateWeather[1]}:', font=("bold", 15))
canvas.create_text(1450, 945, text=f'{dateWeather[2]}:', font=("bold", 15))
canvas.create_text(1750, 945, text=f'{dateWeather[3]}:', font=("bold", 15))


if currentWeather[3]//100 == 8 and currentWeather[3]%100 != 0:
    canvas.itemconfig(wetter,image=(osPath + "Wetter//" + weatherColors[9]))
else:
    basewidth = 700
    newWetterBild = Image.open(osPath + "Wetter//" + weatherColors[currentWeather[3]//100])
    wpercent = (basewidth/float(newWetterBild.size[0]))
    hsize = int((float(newWetterBild.size[1])*float(wpercent)))
    newWetterBild = newWetterBild.resize((basewidth,hsize), Image.ANTIALIAS)
    newWetterBild= ImageTk.PhotoImage(newWetterBild)
    canvas.itemconfig(wetter,image=newWetterBild)
root.attributes('-fullscreen', True)
root.after(5000,lambda: show_articles(get_all_article()))
root.mainloop()