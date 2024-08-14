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

crashed = False
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
                            command="lambda: print('Opening file...')"
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
                            menuName="prefMenu",
                            label= "Preferences",
                            underline= 0,
                            subMenu=[
                                MenuObj( 
                                    type="menu",
                                    menuName="subgroup",
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
                                    type="menu",
                                    menuName="subgroup",
                                    subMenu=[
                                        MenuObj( 
                                            type="command",
                                            label="[Edit Menu Group]",
                                            background="#FFCC66",
                                            underline= 0,
                                            command="lambda: print('Opening file...')"
                                        ),
                                        MenuObj(
                                            type= "command",
                                            label= "Settings",
                                            underline= 0,
                                            command= "lambda: print('Opening file...')"
                                        ),
                                        MenuObj(
                                            type= "command",
                                            label= "Themes",
                                            underline= 0,
                                            command= "lambda: print('Opening file...')"
                                        )
                                    ]
                                ),
                                MenuObj(
                                    type="menu",
                                    menuName="subgroup",
                                    subMenu=[
                                        MenuObj(
                                            type="command",
                                            label="[Add Group]",
                                            background="#66ff66",
                                            underline= 0,
                                            command="lambda: print('Opening file...')"
                                        )
                                    ]
                                )          
                            ]
                        )          
                    ]
                ),
                MenuObj(
                    type="menu",
                    menuName="subgroup",
                    subMenu=[
                        MenuObj(
                            type="command",
                            label="[Add Group]",
                            background="#66ff66",
                            underline= 0,
                            command="lambda: print('Opening file...')"
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

#NOTE This version is the very basic version of the whole root menu of sketch.json
# // I SHOULD BE ABLE TO POPULATE ALL THE OTHER FIELDS THROUGH THIS SCRIPT //
# // This version is for testing my add and calculate commands, especially the unerline function. //
rootMenuBasic = MenuObj(
    type='menu',
    menuName='root',
    subMenu=[
        MenuObj(
            type='menu',
            menuName='fileMenu',
            label='File',
            subMenu=[
                MenuObj(
                    type='menu',
                    menuName='group',
                    subMenu=[
                        MenuObj( 
                            type="command",
                            label="[Edit Cascade]"),
                        MenuObj(
                            type="command",
                            label="[Delete Cascade]")]),
                MenuObj(
                    type='menu',
                    menuName='group2',
                    subMenu=[
                        MenuObj( 
                            type="command",
                            label="[Edit Menu Group]"),
                        MenuObj(
                            type= "command",
                            label= "Open..."),
                        MenuObj(
                            type= "command",
                            label= "Save As...")]),
                MenuObj(
                    type='menu',
                    menuName='group3',
                    subMenu=[
                        MenuObj( 
                            type="command",
                            label="[Edit Menu Group]"),
                        MenuObj(
                            type= "command",
                            label= "Auto Save"),
                        MenuObj(
                            type= "menu",
                            menuName="prefMenu",
                            label= "Preferences",
                            subMenu=[
                                MenuObj( 
                                    type="menu",
                                    menuName="subgroup",
                                    subMenu=[
                                        MenuObj( 
                                            type="command",
                                            label="[Edit Cascade]"),
                                        MenuObj(
                                            type="command",
                                            label="[Delete Cascade]")]),
                                MenuObj(
                                    type="menu",
                                    menuName="subgroup",
                                    subMenu=[
                                        MenuObj( 
                                            type="command",
                                            label="[Edit Menu Group]"),
                                        MenuObj(
                                            type= "command",
                                            label= "Settings"),
                                        MenuObj(
                                            type= "command",
                                            label= "Themes")]),
                                MenuObj(
                                    type="menu",
                                    menuName="subgroup",
                                    subMenu=[
                                        MenuObj(
                                            type="command",
                                            label="[Add Group]")])])]),
                MenuObj(
                    type="menu",
                    menuName="subgroup",
                    subMenu=[
                        MenuObj(
                            type="command",
                            label="[Add Group]")])]),
        MenuObj(
            type="menu",
            menuName="addMenu",
            label="+",
            underline=0,
            subMenu=[
                MenuObj(
                    type="command",
                    label="[Add Cascade]")])])



# OK, I want to a print of EVERY item in its heirarchy
# output should look like this:
"""
        root
            fileMenu - 'File'
                M0G0
                    'edit cascade'
                    'delete cascade'
                M0G1
                    'edit menu group'
                    'open'
                    'save as'
                M0G2
                    'edit menu group'
                    'auto save'
                    PrefMenu - 'Preferences'
                        M0S0G0
                            'edit cascade'
                            'delete cascade'
                        M0S0G1
                            'edit menu group'
                            'settings'
                            'themes'
                        M0S0G2
                            'add group'
                M0G3
                    'add group'
            addMenu - '+'
                M1G0
                    'add cascade'
"""  
def print_menu_structure(menu_obj, level=0):
    #NEed to refactor this to auto set the menu group IDs, and print a before and after. That'll give me a good test of my functions
    indent = "  " * level
    if menu_obj.menuName:
        if menu_obj.get_tag('label'):
            print(f"""{indent}{menu_obj.type}: {menu_obj.menuName} - '{menu_obj.get_tag('label')}'""")
        else:
            print(f"""{indent}{menu_obj.type}: {menu_obj.menuName}""")
    else:
        print(f"""{indent}{menu_obj.type}: {menu_obj.get_tag('label')}""")
    for subMenu in menu_obj.subMenu:
        print_menu_structure(subMenu, level + 1)
    

def convert_to_json(menu_obj):
    #TODO now we need to actually convert this object to json for the live load loop
    # NOTE also need a build mode that adds in the edit groups
    # ACTUALLY, lets make the offical menuItem.py script, and make a backup copy of ALL OF THIS yeah lets do that
    # we need to calculate underlines based on level in a group. Basically underlines only matter if they're in a group of groups, or a childless group.
    # when there is a group, we need to pull its children out and make them direct children/siblings to the group/of the group's parents, after adding a separator, then kill the empty group.
    # then we can write to file
    pass


# do I even want to work on this right now? I just wanna go home and not struggle iwth acid reflux. And maybe play video games.

    
rootMenu.subMenu[0].listSubMenuItems()


print_menu_structure(rootMenuBasic)
print('#################################################')
print('#################################################')
print('#################################################')
print('#################################################')
print('#################################################')
rootMenuBasic.subMenu[0].moveSubMenuItemDown(0)
rootMenuBasic.moveSubMenuItemDown(0)

print_menu_structure(rootMenuBasic)




if not crashed:
    cr='DID NOT CRASH! YAY!'
else:
    cr='Utter Failure. How did you get this message to print anyway???!!!!'
print(f"""Crash Test Result: {cr}""")
