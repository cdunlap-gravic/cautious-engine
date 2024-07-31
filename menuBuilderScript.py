#####################################
#
# TODO: Build the prototype NOW
#    - Doesn't have to be good code, just needs to work
#    GOALS:
#      - Menu bar that has buttons to add sections
#      - each cascade has separate items at the top than can be used for formatting the head
#      - "compile" button that saves changes and gets you out of building mode (kills the plus buttons and other stuff)
# 
#####################################

import tkinter as tk 
from tkinter import ttk
from ttkthemes import ThemedTk

def renameMenu(menu):
    #open rename popup field
    #set new name
    #rebuild menu
    #These menu objects are probably critical to this whole menubuilding
    return

def addCommand():
    return

#can use a pop up with a radio button for what kind of object to add
def addMenu():
    new_window = tk.Toplevel(root)
    new_window.title("New Menu Name?")
    
    def submit_text():
        text_input = text_entry.get()
        #ADD CASCASE HERE
        #MMMMMMMMMMMMACTUALLY this SHOULD just affect the objects, and let the menubuilder
        # reprocess menu generation over and over again. 
        print(text_input)
        new_window.destroy()
    
    text_label = tk.Label(new_window, text='Enter text:')    
    text_label.pack()
    
    text_entry = tk.Entry(new_window)
    text_entry.pack()
    
    submit_button = tk.Button(new_window, text='letsdoit', command=submit_text)
    submit_button.pack()
    
WIN_TITLE = 'Test Script - MenuBar Generation Test 001'
WIN_SIZE = (800, 600)
jsonFile = "./genFiles/menu.json"
root = ThemedTk(theme='black')
root.title(WIN_TITLE)
root.geometry(f'{WIN_SIZE[0]}x{WIN_SIZE[1]}')

menuBar = tk.Menu(root)
root.config(menu=menuBar)

casc1 = tk.Menu(menuBar, tearoff=False)
menuBar.add_cascade(label = '[Rename Me!]', menu = casc1)
casc1.add_command(label = 'rename menu')
casc1.add_separator()
# This should open up a popup with fields for name and command selection/write in field
# and any other tags, ie font or quick commands
casc1.add_command(label = '+', command=lambda:addMenu())


casc2 = tk.Menu(menuBar, tearoff=False)
# THIS ONE should add to the root menu obj
# I don't know if I can add a command here????
menuBar.add_cascade(label = '+', menu = casc2)


frame = ttk.Frame(root, width=WIN_SIZE[0], height=WIN_SIZE[1])
frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
