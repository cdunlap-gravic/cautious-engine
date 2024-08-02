# Imports
import json
import tkinter as tk
import sys
import modules.menuBuilderMenus as MBM

# Global Variables
optArg = {}
root = None # I don't know why I need to instantiate this here, but I do ¯\_(ツ)_/¯

#####################################################################################################
# Functions: 
#####################################################################################################

def loadMenuFromJson(filePath, parentMenu, tkroot):
    #global rooroo
    """
     Base function for loading a menu from a JSON file
        
     @param filePath - path to the JSON file
     @param parentMenu - menu to adhere any commmands or sub menus
    """
    root = tkroot # Why the heck isn't this enough??
    with open(filePath) as file:
        data = json.load(file)
        for key, value in data.items():
            if key == "subMenu":
                recLoadMenuFromJson(value, parentMenu)


#######################################################################
#######################################################################
def recLoadMenuFromJson(dataList, parentMenu):
    """
     Recursive function for loading a menu from a JSON file to handle actual menu generation, and self terminate to root menu
    
    NOTE: This recursive function will need heavy rework and additions. Current logic may not be efficient and I like to remove any overhead if possible
        Also, there are other menu generation options that are not currently supported, i.e. checked values etc.
    
    NOTE: Please see example JSON file provided for expected structure
    
     @param dataList - list object containing an array of commands and/or sub menus
     @param parentMenu - menu to adhere any commmands or sub menus. Key object for recursive functionality
    """
    #global rooroo
    #rooroo = roo
    for item in dataList:
        if isinstance(item, dict):
            for key, value in item.items():
                if key == "type":  
                    dictType = value
                elif key == "menuName":
                    subMenu = tk.Menu(parentMenu, tearoff=0)
                elif isinstance(value, list): 
                    if dictType == "menu":
                        parentMenu.add_cascade(**optArg, menu = subMenu)
                        optArg.clear()
                        recLoadMenuFromJson(value, subMenu)
                elif key == (list(item)[-1]):
                    if dictType == "command": 
                        parentMenu.add_command(**optArg, command = eval(value))
                        optArg.clear()
                    elif dictType == "separator":
                        parentMenu.add_separator()
                        optArg.clear()
                    elif dictType == "iterator":
                        optArg.update({key: value})
                        iters = optArg.get('iterations')
                        optArg.pop('iterations')
                        optArgCP = optArg.copy()
                        for i in range(iters):
                            for fixKey, fixValue in optArg.items():
                                optArgCP.update({fixKey: f'{str(fixValue)}{i+1}'})
                            parentMenu.add_command(**optArgCP)
                        optArg.clear()
                        optArgCP.clear()
                else: 
                    optArg.update({key: value})


#######################################################################
#######################################################################