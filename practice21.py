## creating a graphical button in python
from tkinter import *
master = Tk()

def callback():
    print("You Clicked the button")

btn= Button(master, text="OK", command=callback())
btn.pack()
mainloop()