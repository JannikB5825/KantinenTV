from tkinter import *
from configparser import ConfigParser
import json as json_
import requests



url = 'https://api.openweathermap.org/data/2.5/onecall?lat=50.59&lon=8.95&lang=de&exclude=current,minutely,hourly,alerts&units=metric&appid=013c319d6be43d6ff15ca9d6325c8fb2'

def get_weather():
    result = requests.get(url, verify=False)
    if result:
        json = json_.loads(result.text)
        # Stadt, Land, Temperatur, icon, Wetter
        max_temp = json['daily'][0]['temp']["max"]
        min_temp = json['daily'][0]['temp']["min"]
        icon = json['daily'][0]['weather'][0]['icon']
        weahter = json['daily'][0]['weather'][0]['description']
        final = (max_temp, min_temp, icon, weahter)
        return final
    else:
        return None

print(get_weather())


def search():
    pass

app = Tk()
app.title("Wetter API")
app.geometry('700x350')

city_text = StringVar()
city_entry = Entry(app, textvariable = city_text)
city_entry.pack()

search_btn = Button(app, text='Suche Wetter', width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text='Standort', font=('bold', 20))
location_lbl.pack()

image = Label(app, bitmap='')
image.pack()

temp_lbl = Label(app, text='Temperatur')
temp_lbl.pack()


app.mainloop()