import modules.menuFromJson as MJ
import tkinter as tk 
from tkinter import ttk
from ttkthemes import ThemedTk
from threading import Thread
import testscripts.geminihelpme as gem

import sdl2
import sdl2.ext
import sdl2.sdlimage
import pyboy

# Global variables
WIN_TITLE = 'Test Script - Menu Builder layout'
WIN_SIZE = (800, 600)
jsonFile = "./genFiles/sketch.json"
root = ThemedTk(theme='black')
root.title(WIN_TITLE)
root.geometry(f'{WIN_SIZE[0]}x{WIN_SIZE[1]}')

menuBar = tk.Menu(root)
root.config(menu=menuBar)
MJ.loadMenuFromJson(jsonFile, menuBar, root)

frame = ttk.Frame(root, width=WIN_SIZE[0], height=WIN_SIZE[1])
frame.pack(fill=tk.BOTH, expand=True)
#print(MJ.recLoadMenuFromJson.__doc__)
#print(dir(MJ))
#print(help(MJ.recLoadMenuFromJson))

t1 = Thread(target = root.mainloop())
t2 = Thread(target = ...)

t1.start()
t2.start()
