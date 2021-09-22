import tkinter as ui
import time

window = ui.Tk()


def update_clock():
    hours = time.strftime("%H")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " "
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)


digital_clock_lbl = ui.Label(window, text="00:00:00", font="Helvetica 72 bold")
digital_clock_lbl.config(foreground="yellow")
digital_clock_lbl.config(bg="darkgreen")
digital_clock_lbl.pack()

update_clock()
window.config(background="")
window.mainloop()