import modules.menuFromJson as MJ
import tkinter as tk 
from tkinter import ttk
from ttkthemes import ThemedTk
from threading import Thread
import testscripts.geminihelpme as gem
from modules.objects import MenuItem # how this fixes it I don't know. Let's not worry about imports
from modules.hcRootMI import *
from modules.objToJson import *
import json

import sdl2
import sdl2.ext
import sdl2.sdlimage
import pyboy

#print(ObjToJson(testsub))
# Global variables
WIN_TITLE = 'Test Script - Menu Builder layout'
WIN_SIZE = (800, 600)

TESTSRC='obj'
#jsonFile = "./genFiles/sketch.json"

editedtestsub = testsub




root = ThemedTk(theme='black')
root.title(WIN_TITLE)
root.geometry(f'{WIN_SIZE[0]}x{WIN_SIZE[1]}')

menuBar = tk.Menu(root)
root.config(menu=menuBar)

if TESTSRC == 'obj':
    ParseOutGroupsFromRoot(editedtestsub)   
    jsonFile = ObjToJson(editedtestsub)
    MJ.loadMenuFromJsonObj(jsonFile, menuBar, root)
    
    with open('output.json', 'w') as file:
        json.dump(jsonFile, file, indent=4)
else:
    MJ.loadMenuFromJsonFile('output.json', menuBar, root)


frame = ttk.Frame(root, width=WIN_SIZE[0], height=WIN_SIZE[1])
frame.pack(fill=tk.BOTH, expand=True)
#print(MJ.recLoadMenuFromJson.__doc__)
#print(dir(MJ))
#print(help(MJ.recLoadMenuFromJson))

t1 = Thread(target = root.mainloop())
t2 = Thread(target = ...)

t1.start()
t2.start()
