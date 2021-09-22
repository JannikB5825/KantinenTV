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
        discription = json['daily'][0]['weather'][0]['description']
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
        max_temp4 = json['daily'][5]['temp']["max"]
        min_temp4 = json['daily'][5]['temp']["min"]
        icon4 = json['daily'][5]['weather'][0]['icon']
        final = [max_temp, min_temp, icon, discription, max_temp1, min_temp1, icon1, max_temp2, min_temp2, icon2, max_temp3, min_temp3, icon3, max_temp4, min_temp4, icon4]
        return final
    else:
        return None

weather = get_weather()
dis = weather[3]
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

root = Tk()
root.title("Wetter API")
root.geometry('750x400')

location_lbl = Label(root, text='Grünberg', font=('bold', 20))
location_lbl.config(background='#00d1e8')
location_lbl.pack()

weather[2] = ImageTk.PhotoImage(Image.open(f"C:\\KantinenTv\\KantinenTV-1\\Icon\\{weather[2]}@2x.png"))
image = Label(root, image=weather[2])
image.config(background='#00d1e8')
image.pack()

status = Label(root, text=dis, font=('bold', 15))
status.config(background='#00d1e8')
status.pack()

max_min_temp = Label(root, text=f'{int(ma//1)}° / {int(mi//1)}°', font=("bold", 12))
max_min_temp.config(background='#00d1e8')
max_min_temp.pack()


weather[6] = ImageTk.PhotoImage(Image.open(f"C:\\KantinenTv\\KantinenTV-1\\Icon\\{weather[6]}@2x.png"))
image = Label(root, image=weather[6])
image.config(background='#00d1e8')
image.pack()

max_min_temp = Label(root, text=f'{int(ma1//1)}° / {int(mi1//1)}°', font=("bold", 12))
max_min_temp.config(background='#00d1e8')
max_min_temp.pack()


weather[9] = ImageTk.PhotoImage(Image.open(f"C:\\KantinenTv\\KantinenTV-1\\Icon\\{weather[9]}@2x.png"))
image = Label(root, image=weather[9])
image.config(background='#00d1e8')
image.pack()

max_min_temp = Label(root, text=f'{int(ma2//1)}° / {int(mi2//1)}°', font=("bold", 12))
max_min_temp.config(background='#00d1e8')
max_min_temp.pack()


weather[12] = ImageTk.PhotoImage(Image.open(f"C:\\KantinenTv\\KantinenTV-1\\Icon\\{weather[12]}@2x.png"))
image = Label(root, image=weather[12])
image.config(background='#00d1e8')
image.pack()

max_min_temp = Label(root, text=f'{int(ma3//1)}° / {int(mi3//1)}°', font=("bold", 12))
max_min_temp.config(background='#00d1e8')
max_min_temp.pack()


weather[15] = ImageTk.PhotoImage(Image.open(f"C:\\KantinenTv\\KantinenTV-1\\Icon\\{weather[15]}@2x.png"))
image = Label(root, image=weather[15])
image.config(background='#00d1e8')
image.pack()

max_min_temp = Label(root, text=f'{int(ma4//1)}° / {int(mi4//1)}°', font=("bold", 12))
max_min_temp.config(background='#00d1e8')
max_min_temp.pack()


root.attributes('-fullscreen', True)
root.configure(background='#00d1e8')

root.mainloop()