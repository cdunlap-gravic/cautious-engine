####################################################################
#
# - will refactor this as MenuItem.py
# - forzensets should be abstracted out of here, if not for flexiblity,
# then at least on principle. MenuItems need them, but they aren't
# entirely standalone to MenuItems. MFJ uses these lists, too
#
# - will also need to include error handling and typehinting x-out
#
# Ok, but what do I want to do /TODAY/?
# - refactoring will be later, but I could/should abstract those sets sooner than later.
# lets leave them here for now and continue working on the MenuObj (MenuItem). I want to have the functions set to
# actually rearrange the order, AND I want to write a conversion of OBJ->JSON script. And I'll need a JSON->OBJ script.
# I currently have JSON->MENUBAR, but need to fill out the rest of the steps:
# 
# yeah lets do the actual relational management functions:
# - add group memeber
# - switch order etc
# - drop 
# - rename
# - edit tags
#
# INI->OBJ ///Actually, INI's should be redundant. I wouldn't need it
# JSON->OBJ
# OBJ->JSON ///Ideally, I should also have an OBJ->MENUBAR script which would mirror the json file. Json here would only be a saved config file.
# JSON->MENUBAR
#
####################################################################


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
        
        ###
        #OK SO BASE OBJECT IS MADE. Once things are added to it, we need to be running a check on the memebers of a submenu if there is one
        # /and there certainly is one in root and it's first child/ and we need to run that check WHEN members are added. 
        
        ###
        if self.type == 'group':
            #TODO insert separators between groups
            # NOPE. NOT IF GROUP. IF ALL SUBMENU OBJECTS FIRST LEVEL OF CHILDREN ARE OF TYPE MENU THEN ITS A GROUP,
            # SO ADD SEPARATORS
            # ok, maybe this shouldn't be here, but in a management script, but still
            pass
        
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
    
    #Tag functions which I will need like underline maybe here?
    
    #TODO ...
    
    # submenu functions 
    
    #TODO ....   
    #TODO should add a get all items with names/labels for print mode, and actual object modes
    
    def listSubMenuItems(self, mode: str = "Print"): # THIS IS SUBPAR BUT IT WORKS FOR NOW  ¯\_(ツ)_/¯
        if mode == "Print":
            print(self.subMenu)
        else:
            pass
        
    def addSubMenuItem(self, item: "MenuObj", bypass: bool = False):
        #adds item to end of submenu (was menuGroup)
        #TODO validate item if it exists, and if so, let user know, w/ bypass
        if not bypass:
            pass
        self.subMenu.append(item)
        pass
    
    def dropSubMenuItem(self, item: "MenuObj", bypass: bool = False):
        #removes item from submenu (was menuGroup)
        #check if item exists first
        #and maybe do a confirmation mode?
        #should also have a bypass bool to skip confirmation
        if not bypass:
            pass
        self.subMenu.remove(item)
    
    def insertSubMenuItem(self, item: "MenuObj", index: int):
        #inserts item into submenu as position (was menuGroup)
        pass
        
    def moveSubMenuItemUp(self, index):
        """
          Simple Swap up function
        """
        if index <= 0 or index >= len(self.subMenu):
            raise IndexError(f"""Invalid index for {self.menuName}'s subMenu item initial position""") #need to verify if this will work for name 
            # Maybe label would work better?
        self.subMenu[index - 1], self.subMenu[index] = self.subMenu[index], self.subMenu[index - 1]
        
    def moveSubMenuItemDown(self, index):
        """
          Simple Swap down function
        """
        if index < 0 or index >= len(self.subMenu) - 1:
            raise IndexError(f"""Invalid index for {self.menuName}'s subMenu item initial position""")
        self.subMenu[index + 1], self.subMenu[index] = self.subMenu[index], self.subMenu[index + 1]
    
    def find_menu_obj():
        pass
    
    def insert_mult():
        pass
    
    def remove_mult():
        pass
    
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
    
    
def invalid_keys(kwargs:dict) -> set:
    invalid_keys = set(kwargs.keys()) - allowed_keys
    return invalid_keys

# I can probably load json to obj by now...
# LETS DO ONE QUICK HARDCODE TO TEST
#AHA this is NOT interchangable yet. If I convert to Json, I have to kill the group menuname bits, since 
# those are only used for calculating separators and underlines
# I WILL ALSO have to consider the reverse, with loading from json to obj, and kill separators and take 
# underlines as a suggestion from the json file

# HARDCODE TEST
rootMenu = MenuObj(
    type='menu',
    menuName='root',
    subMenu=[
        MenuObj(
            type='menu',
            menuName='fileMenu',
            label='File',
            underline=0,
            subMenu=[
                MenuObj(
                    type='menu',
                    menuName='group',
                    subMenu=[
                        MenuObj( 
                            type="command",
                            label="[Edit Cascade]",
                            background="#FFCC66",
                            underline= 0,
                            command="lambda: MBM.EditCascade(root)"
                        ),
                        MenuObj(
                            type="command",
                            label="[Delete Cascade]",
                            background="#FF6666",
                            underline=0,
                            command="lambda: MBM.SubmitWin(root)"
                        )       
                    ]
                ),
                MenuObj(
                    type='menu',
                    menuName='group2',
                    subMenu=[
                        MenuObj( 
                            type="command",
                            label="[Edit Menu Group]",
                            background="#FFCC66",
                            underline= 0,
                            command="lambda: MBM.EditCascade(root)"
                        ),
                        MenuObj(
                            type= "command",
                            label= "Open...",
                            underline= 0,
                            command= "lambda: print('Opening file...')"
                        ),
                        MenuObj(
                            type= "command",
                            label= "Save As...",
                            underline= 0,
                            command= "lambda: print('Opening file...')"
                        )          
                    ]
                ),
                MenuObj(
                    type='menu',
                    menuName='group3',
                    subMenu=[
                        MenuObj( 
                            type="command",
                            label="[Edit Menu Group]",
                            background="#FFCC66",
                            underline= 0,
                            command="lambda: MBM.EditCascade(root)"
                        ),
                        MenuObj(
                            type= "command",
                            label= "Auto Save",
                            underline= 0,
                            command= "lambda: print('Opening file...')"
                        ),
                        MenuObj(
                            type= "menu",
                            label= "Preferences",
                            underline= 0,
                            subMenu=[
                                MenuObj( 
                                    type="menu",
                                    menuName="subgroup",
                                    subMenu=[
                                        MenuObj(
                                            type="command",
                                            label="[Edit Menu Group]",
                                            background="#FFCC66",
                                            underline= 0,
                                            command="lambda: MBM.EditCascade(root)"
                                        ),
                                        MenuObj(
                                            type= "command",
                                            label= "Open...",
                                            underline= 0,
                                            command= "lambda: print('Opening file...')"
                                        ),
                                        MenuObj(
                                            type= "command",
                                            label= "Save As...",
                                            underline= 0,
                                            command= "lambda: print('Opening file...')"
                                        )
                                    ]
                                )          
                            ]
                        )          
                    ]
                )
            ]
        ),
        MenuObj(
            type="menu",
            menuName="addMenu",
            label="+",
            underline=0,
            subMenu=[
                MenuObj(
                    type="command",
                    label="[Add Cascade]",
                    background="#66ff66",
                    underline= 0,
                    command="lambda: print('Opening file...')"
                )
            ]    
        )
    ]
    
)

print(rootMenu.subMenu[0].subMenu[1].tags)
print('test')