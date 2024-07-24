#####################################
#
# 1st: testing if a push from vscode works
# 2nd: need to just flesh out base code
# 3rd, can rework the code later properly, but for now
# lets just work on the base logic on how to generate the 
# menu bar from within itself and go from there
# TEST EDIT ON CB
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

casc1 = tk.Menu(menuBar, tearoff=False)
menuBar.add_cascade(label = 'Main Cascade', menu = casc1)
casc1.add_command(label = 'rename menu')
casc1.add_separator()
casc1.add_command(label = '+')

casc2 = tk.Menu(menuBar, tearoff=False)
menuBar.add_cascade(label = '+', menu = casc2)


frame = ttk.Frame(root, width=WIN_SIZE[0], height=WIN_SIZE[1])
frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
