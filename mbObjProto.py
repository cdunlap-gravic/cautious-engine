from enum import Enum
from abc import ABC, abstractmethod


class MenuType(Enum):
    MENU = 'menu'
    COMD = 'command'
    ITER = 'iterator'
    SEPR = 'separator'

class MenuTags(Enum):
    #Maybe enums aren't the best way to go with so many tags?
    ACCEL = 'accelerator'
    ACTVBG = 'activebackground'
    ACTVFG = 'activeforeground'
    BG = 'background'
    FG = 'foreground'
    BMP = 'bitmap'
    COLBRK = 'columnbreak'
    CMD = 'command'
    COMP = 'compound'
    FONT = 'font'
    HDMRG = 'hidemargin'
    IMG = 'image'
    LBL = 'label'
    MENU = 'menu'
    ONVAL = 'onvalue'
    OFFVAL = 'offvalue'
    SELCLR = 'selectcolor'
    SELIMG = 'selectimage'
    STATE = 'state'
    UNDRL = 'underline'
    VAL = 'value'
    VAR = 'variable'
   
class MenuObj:
    def __init__(self) -> None:
        # When an object is instantiated, what needs to exist? Lists need to exist, and variables should
        # probably exist. I'll also need setters and getters.
        # I'll also need to somehow convert these objects into my json objects, and vice versa.
        # All those tags need to go somewhere too. They *can* go into a dict like the json, but
        # I want some amount of validation. But I also don't want to set 100 parameters that aren't
        # touched by half the objects. Perhaps setting up an Enum with all of the tags would work?
        # then I can validate if the list dict even has valid keys. 
        # I can also use enums for the type key values, to validate the menu types
        # and in doing all of THIS, I'll be able to document and possibly dynamically set the enums based
        # on what actually is handled by MFJ.py. I can also have THAT list be generated in another module
        # [{x:x,...,x:[{x:x,...,x:x},...,{x:x,...,x:x}]},...,{x:x,...,x:x}] 
        #
        self.blank = None
        pass
    
class OLDmenuObj:
    # technically I should never have this object instantiated directly. Let's turn this into an ABC
    # actually, maybe not. I would insntatiated these
    def __init__(self):
        self._thing = None
        self.tags = []
        self.type = Enum('MenuType', ['menu','command','iterator','separator'])
        self.underline = None
        self.groups = []
    
    def addGroup(group):
        groups = []
        
        """
        or do I want these tags in a dict list?
        I should probably keep the tags in a dict list so I can use the same navigation logic, AND so that this is able to store commands and menus.
        
        Key issue here is I need to organize things in groups.
        A set of groups will make up a single cascade
        and separators will be defined between groups.
        
        underlines are defined after all commands/submenus are orgainzed and will follow certain rules
        
        first letter of first word, if first word is common, first of second for those groups of words, and if need be, shift letters.
        
        CERTAIN WORDS have priority, ie Close, Exit, etc
        
        this tool is here to FIX the man made decisions of underlines, and adding separators
        
        AFTER THIS WHOLE SCRIPT IS DONE BUILDING THE OBJECTS, we push and write it to a json file.
        """
    
class menuGroup:
    def __init__(self):
        self.members = []
        
        
"""
    Let's work backwards with the process and we'll be able to figure out what is needed from that:
    
    WILL HAVE TO WALK THROUGH EVERYTHING TWICE
    once to calculate underlines etc
    second to actually build the json file
    (I don't want to have the first instance of 'Open X type file' to have 'Open' underlined, but the X, or the next letter of it, so I need to catalog the names of all commands and parse them out before fully generating the json file)

########
##########
if the menu object has a groups field, it is of type "menu"


ok what do I actually need to get done here?
I need to have a menu object that can hold the info of THAT json file over there  ----------> 

these objects should have all that info, and THEN, I populate the underlines through total picture analysis

from enum import StrEnum
class menuType(StrEnum):
    MENU = "MENU"
    COMMAND = "COMMAND"
    ITERATOR = "ITERATOR"
    
class menuObj:
    
    def __init__(self, menu_type: menuType):
        self.menu_type = menu_type
        self.tags = []
    
    # SETTERS
    def set_menu_type(self, menu_type: menuType):
        self.menu_type = menu_type
    
    def add_tag(self, dict)
    # GETTERS    
    def get_menu_type(self):
        return self.menu_type
    
    def get_tags(self):
        return self.tags
        
    # OTHER FUNCS
    def processUnderlines(self):
        return
        

##########
########




    underline creation:
        walk through main menus
            add each label to list
        GOT THE LIST
        parse the list
            assign underline value to unique letter in that SET
            underline values only have to be unique to the menu set, not including submenus.
            
    
    walk through main menu object
        walk through children objects
            add cascade to parent
            go through groups
                begin walking through group
                    add each command and pop tags
                if not last group:
                    add separator
            
        add first child (file menu)
        add cascade
    convert all to json




"""
