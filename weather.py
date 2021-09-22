from tkinter import *
from tkinter import messagebox 
from configparser import ConfigParser
import json as json_
import requests
import time
from PIL import ImageTk,Image  



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
        weahter = json['daily'][0]['weather'][0]['description']
        final = [max_temp, min_temp, icon, weahter]
        print(final)
        return final
    else:
        return None

weather = get_weather()



root = Tk()
root.title("Wetter API")
root.geometry('700x350')

location_lbl = Label(root, text='Grünberg', font=('bold', 20))
location_lbl.pack()

weather[2] = ImageTk.PhotoImage(Image.open(f"C:\\KantinenTv\\KantinenTV-1\\Icon\\{weather[2]}@2x.png"))
image = Label(root, image=weather[2])
image.pack()

max_min_temp = Label(root, text='Temperatur')
max_min_temp.pack()


root.mainloop()