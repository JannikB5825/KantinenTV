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
    

for x in get_all_article():
    print(x)