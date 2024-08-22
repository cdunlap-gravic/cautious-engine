import modules.menuFromJson as MJ
import tkinter as tk 
from tkinter import ttk
from ttkthemes import ThemedTk
from threading import Thread
import testscripts.geminihelpme as gem
from modules.objects import MenuItem # how this fixes it I don't know. Let's not worry about imports
from modules.hcRootMI import *
from modules.objToJson import *

import sdl2
import sdl2.ext
import sdl2.sdlimage
import pyboy

#print(ObjToJson(testsub))
# Global variables
WIN_TITLE = 'Test Script - Menu Builder layout'
WIN_SIZE = (800, 600)
#jsonFile = "./genFiles/sketch.json"

editedtestsub = testsub
# IT:S HARDCODED BUTTTTT IT DOES WORK!!!!!!!!!

# THIS HSOULD NOT BE HARDCODED: instead it should look like this:
ParseOutGroupsFromRoot(editedtestsub)
#editedtestsub.subMenu[0].parentalPurge(editedtestsub.subMenu[0].subMenu[0])
#editedtestsub.subMenu[0].parentalPurge(editedtestsub.subMenu[0].subMenu[0])
#editedtestsub.subMenu[0].parentalPurge(editedtestsub.subMenu[0].subMenu[0])
#editedtestsub.subMenu[0].parentalPurge(editedtestsub.subMenu[0].subMenu[0])
#editedtestsub.subMenu[0].subMenu[9].parentalPurge(editedtestsub.subMenu[0].subMenu[9].subMenu[0])
#editedtestsub.subMenu[0].subMenu[9].parentalPurge(editedtestsub.subMenu[0].subMenu[9].subMenu[0])
#editedtestsub.subMenu[0].subMenu[9].parentalPurge(editedtestsub.subMenu[0].subMenu[9].subMenu[0])

#print(editedtestsub.subMenu[0].subMenu[0].subMenu[0].getTag('label'))
jsonFile = ObjToJson(editedtestsub)
root = ThemedTk(theme='black')
root.title(WIN_TITLE)
root.geometry(f'{WIN_SIZE[0]}x{WIN_SIZE[1]}')

menuBar = tk.Menu(root)
root.config(menu=menuBar)
MJ.loadMenuFromJsonObj(jsonFile, menuBar, root)

frame = ttk.Frame(root, width=WIN_SIZE[0], height=WIN_SIZE[1])
frame.pack(fill=tk.BOTH, expand=True)
#print(MJ.recLoadMenuFromJson.__doc__)
#print(dir(MJ))
#print(help(MJ.recLoadMenuFromJson))

t1 = Thread(target = root.mainloop())
t2 = Thread(target = ...)

t1.start()
t2.start()
