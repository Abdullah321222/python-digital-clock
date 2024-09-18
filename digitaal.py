from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(2000,time)

label = Label(root, font=("DS-DIGI.TTF",80),background="PINK",foreground="cyan")
label.pack(anchor='center')
time()

mainloop()