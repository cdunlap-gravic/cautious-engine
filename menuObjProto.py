from enum import Enum


    
class menuObj:
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