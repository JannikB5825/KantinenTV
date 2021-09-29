#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk
import sys
from PyQt5.QtWidgets import QApplication
app = QApplication(sys.argv)
screen = app.screens()[0]
dpi = screen.physicalDotsPerInch()
app.quit()
#Create an instance of tkinter frame
win = Tk()
win.tk.call('tk', 'scaling', '-displayof', '.', dpi/72.0)
#Set the geometry of tkinter frame
win.geometry("1920x1080")

#Create a canvas
canvas= Canvas(win,width=win.winfo_screenwidth(),height=win.winfo_screenheight())
canvas.pack()


#Load an image in the script
img= ImageTk.PhotoImage(Image.open("C:\\KantinenTv\\KantinenTV-1\\Icon\\Black_Bars.png"))

#Add image to the Canvas Items
canvas.create_image(0,0,anchor=NW,image=img)

canvas.config(background='gray')
win.attributes('-fullscreen', True)
win.mainloop()