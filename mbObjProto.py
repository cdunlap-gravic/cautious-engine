
# THIS STUFF IS MORE FOR VALIDATION TESTING BEFORE RUNNING MFJ.PY, BUT CAN ALSO BE USED TO LIST/VALIDATE OPTIONS IN MBMs. This architecture could also be used for the lic builder, listing all the options. I should probably consider  building a configuration set file to load these from, and/or a table
my_keys = frozenset({'type', 'menuName', 'subMenu'})
menu_types = frozenset({'menu', 'command', 'iterator', 'separator'})
tkinter_args = frozenset({'accelerator', 'activebackground', 'activeforeground', 'background', 'bitmap', 'columnbreak', 'command', 'compound', 'font', 'foreground', 'hidemargin', 'image', 'label', 'menu', 'offvalue', 'onvalue', 'selectcolor', 'selectimage', 'state', 'underline', 'value', 'variable'})

currently_known_not_supported = frozenset({'font'})
needs_functions_to_be_a_useful_tag = frozenset({'accelerator'})

allowed_keys = frozenset(tkinter_args | my_keys)
# I probably should get these from a written file


## IN THE MENU EDITOR WINDOWS I WILL NEED TO MAKE A SECOND INSTANCE OF THE MENUOBJ AS A BUFFER BEFORE SAVING THE CHANGE, THAT WAY IF YOU
## CANCEL, NOTHING IS OVERWRITTEN. ACTUALLY I'LL NEED 2: Actual MenuBar, Cached Version, Current Buffer, IF APPLY, THEN WRITE TO Actual MenuBar
# I'll also need to somehow convert these objects into my json objects, and vice versa.
class MenuObj:
    def __init__(self, type:str, **kwargs:dict) -> None:
        if type not in menu_types:
            raise ValueError(f"""Invalid type: {type}. Must be one of: {menu_types}""")
        self.type = type
        
        if invalid_keys(kwargs):
            raise ValueError(f"""Invalid keys: {invalid_keys(kwargs)}""")
        
        self.tags = {k: v for k, v in kwargs.items() if k not in my_keys}
        self.menuName = kwargs.get('menuName', None)
        self.subMenu = kwargs.get('subMenu', [])
        
        #OK SO BASE OBJECT IS MADE. Once things are added to it, we need to be running a check on the memebers of a submenu if there is one
        # /and there certainly is one in root and it's first child/ and we need to run that check WHEN members are added. 
        
    #setters
    
    def set_type(self, type:str) -> None:
        if type not in menu_types:
            raise ValueError(f"""Invalid type: {type}. Must be one of: {menu_types}""")
        self.type = type
        
    def set_tags(self, **kwargs:dict) -> None:
        if invalid_keys(kwargs):
            raise ValueError(f"""Invalid keys: {invalid_keys(kwargs)}""")
        self.tags = {k: v for k, v in kwargs.items() if k not in my_keys}
    
    #Should I even set the menuName without validating if it already has one? This really shouldn't be called without verifying ¯\_(ツ)_/¯
    def set_menuName(self, menuName:str) -> None:
        self.menuName = menuName
        
    #getters
    
    def get_type(self) -> str:
        return self.type
    
    #TODO should probably validate that the tag ISNT MYKEY
    def get_tag(self, tag:str) -> any:
        try:
            return self.tags.get(tag)
        except KeyError:
            raise KeyError(f"""Tag '{tag}' not found in MenuObj""")
    
    def get_menuName(self) -> str:
        try:
            return self.menuName
        except AttributeError:
            raise AttributeError(f"""MenuObj does not have a menuName""")
    
    #type functions if I need any...
    
    #TODO ...
    
    #Tag functions which I will need
    
    #TODO ...
    
    # submenu functions 
    
    #TODO ....    
        
        
        # ALL OBJECTS IN SUBMENU WILL BE A LIST OF MENUOBJS. SOME LISTS MAY ONLY HAVE 1 MEMBER AND THATS OK, BUT OTHERS WILL BE A LIST OF MENUOBJS THAT ONLY HAVE SUBMENUS(other lists) and THATS OK TOO! We'll be INSERTING another MenuObj bewteen MenuObjs that have self.type == 'menu'
        
    #insert separator
    """_'psuedo'_

    def addSeparator(self):
        for i in self.subMenu.items():
        
    
    """

    
    
    
    #TODO: Other Funcs
    def defineUnderlines(self): # sorts out all underlines in the topmost layer. This func should also call itself on specific children objects for each cascade layer; This should also be automatically called whenever changes are made to the whole cascade/menubar
        pass

    #TODO SUBMENU FUNCTIONS
    def add_menu_object(self, menu_object):
        self.menu_objects.append(menu_object)

    #TODO rearange functions
    
    #TODO drop functions
    
    #TODO rename objects functions
    
    
def invalid_keys(**kwargs:dict) -> set:
    invalid_keys = set(kwargs.keys()) - allowed_keys
    return invalid_keys


print('test')