
# THIS STUFF IS MORE FOR VALIDATION TESTING BEFORE RUNNING MFJ.PY, BUT CAN ALSO BE USED TO LIST/VALIDATE OPTIONS IN MBMs. This architecture could also be used for the lic builder, listing all the options. I should probably consider  building a configuration set file to load these from, and/or a table
menu_types = {'menu', 'command', 'iterator', 'separator'}

tkinter_args = {'accelerator', 'activebackground', 'activeforeground', 'background', 'bitmap', 'columnbreak', 'command', 'compound', 'font', 'foreground', 'hidemargin', 'image', 'label', 'menu', 'offvalue', 'onvalue', 'selectcolor', 'selectimage', 'state', 'underline', 'value', 'variable'}

my_keys = {'type', 'menuName', 'subMenu'}

currently_known_not_supported = {'font'}
# I probably should get these from a written file


# I WILL need a way to validate that the KEYS in menu.json either match tkinter_args OR matches my KEYS
class MenuObj:
    def __init__(self, type, **kwargs) -> None:
        # TODO I need setters and getters.
        # I'll also need to somehow convert these objects into my json objects, and vice versa. NOTE working on that
        # through the MenuObj/MenuGroup object relationship
        self.type = type
        self.tags = {k: v for k, v in kwargs.items() if k != 'subMenu'}
        self.subMenu = kwargs.get('subMenu', []) # this will be a list of dicts
    
    def set_tag(self, tag: dict):
        #This function needs to take some sort of argument, validate that it is an acccepted arg, and then set the tag
        # within self.tags
        pass
    

#topmost item will be a MenuObj named root, and it will have a submenu which will comprise of a list of
# menu groups. Each menu group will have menu objs, which could own a list of menu groups (menu groups are
# lists of menu objects) At no point will a menu group have a list of menu groups. There WILL be a parent menu
# object to hold menu groups, otherwise there will be no labels etc

class MenuGroup:
    def __init__(self, name=None) -> None:
        self.name = name
        self.menu_objects = []
        
    def add_menu_object(self, menu_object):
        self.menu_objects.append(menu_object)

    #TODO rearange functions
    
    #TODO drop functions
    
    #TODO rename objects functions
    
    
            
"""
    underlines are defined after all commands/submenus are orgainzed and will follow certain rules
    
    first letter of first word, if first word is common, first of second for those groups of words, and if need be, shift letters.
    
    CERTAIN WORDS have priority, ie Close, Exit, etc
    
    this tool is here to FIX the man made decisions of underlines, and adding separators
    
    AFTER THIS WHOLE SCRIPT IS DONE BUILDING THE OBJECTS, we push and write it to a json file.
###########
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
