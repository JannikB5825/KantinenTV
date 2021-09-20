import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
 
root = tk.Tk()
img_url = "https://www.bender.de/fileadmin/_processed_/4/5/csm_TN-S-TT-System_Kampagnengrafik_EN_18_014a93065d.jpg"
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
root.mainloop()