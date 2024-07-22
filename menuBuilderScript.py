#####################################
#
#
#
#
#
#####################################

import tkinter as tk 
from tkinter import ttk
from ttkthemes import ThemedTk


WIN_TITLE = 'Test Script - MenuBar Generation Test 001'
WIN_SIZE = (800, 600)
jsonFile = "./genFiles/menu.json"
root = ThemedTk(theme='black')
root.title(WIN_TITLE)
root.geometry(f'{WIN_SIZE[0]}x{WIN_SIZE[1]}')

menuBar = tk.Menu(root)
root.config(menu=menuBar)

frame = ttk.Frame(root, width=WIN_SIZE[0], height=WIN_SIZE[1])
frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
