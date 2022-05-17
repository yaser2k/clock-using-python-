import time
from tkinter import *
import time

def digital():
    d=time.strftime("%H:%M:%S")
    clock.config(text=d)
    clock.after(200,digital)
root=Tk()
root.title("Digital Clock - quartz")
clock=Label(root,font=("times",100,"bold"),bg="white")
clock.grid()
clock.pack(anchor='center')
digital()
root.mainloop()
