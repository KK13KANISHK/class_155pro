# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 17:33:51 2023

@author: kanis
"""

from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Adding_bg_using_dictinary")

dictionary = {"colour": ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1","deep pink","cyan"]}

def bg_change():
    change = random.randint(0,7)  
    print(dictionary["colour"][change])
    root.configure(background= dictionary["colour"][change])

btn = Button(root, text = "change colour", command= bg_change)
btn.place(relx = 0.5, rely= 0.5 , anchor = CENTER)

root.mainloop()