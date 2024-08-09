
# THIS STUFF IS MORE FOR VALIDATION TESTING BEFORE RUNNING MFJ.PY, BUT CAN ALSO BE USED TO LIST/VALIDATE OPTIONS IN MBMs. This architecture could also be used for the lic builder, listing all the options. I should probably consider  building a configuration set file to load these from, and/or a table
menu_types = {'menu', 'command', 'iterator', 'separator'}

tkinter_args = {'accelerator', 'activebackground', 'activeforeground', 'background', 'bitmap', 'columnbreak', 'command', 'compound', 'font', 'foreground', 'hidemargin', 'image', 'label', 'menu', 'offvalue', 'onvalue', 'selectcolor', 'selectimage', 'state', 'underline', 'value', 'variable'}

my_keys = {'type', 'menuName', 'subMenu'}

currently_known_not_supported = {'font'}
# I probably should get these from a written file


# I WILL need a way to validate that the KEYS in menu.json either match tkinter_args OR matches my KEYS
class MenuObj:
    def __init__(self, type, **kwargs) -> None:
        # I'll also need to somehow convert these objects into my json objects, and vice versa. NOTE working on that
        # through the MenuObj/MenuGroup object relationship
        self.type = type
        self.tags = {k: v for k, v in kwargs.items() if k != 'subMenu'}
        self.subMenu = kwargs.get('subMenu', []) # this will be a list of dicts
        # OK BUT, k:v stuff, every item in the submenu should be a menuobj that could hold a menugroup. so submenu IS a menu group?
        # ok but if this is the case, then I should only get one item back and that will be a menugroup object.
        # THIS SUBMENU SHOULD TECHINCALLY BE A MENU GROUP RIGHT?
        
    
    #TODO: SETTERS
    def set_tag(self, tag: dict): #expecting single dict item, needs verification that it is an accepted tkinter_args, or my_keys
        pass
    
    #TODO: GETTERS
    def get_tag(self, tag: str): # returns value of a specific tag, OR, return that the tag has not yet been set (not found)
        pass
    
    #TODO: Other Funcs
    def defineUnderlines(self): # sorts out all underlines in the topmost layer. This func should also call itself on specific children objects for each cascade layer; This should also be automatically called whenever changes are made to the whole cascade/menubar
        pass
    
class MenuObjV2:
    def __init__(self, type, **kwargs) -> None:
        self.type = type
        self.tags = {k: v for k, v in kwargs.items() if k != 'subMenu'}
        self.subMenu = kwargs.get('subMenu', None) # this will be a LIST[] THAT:S ARELADY FREAKIN ORDERED. JUST FUCKING REARANGE THEM.
        # techincally subMenu is a list of dicts, not a list of MenuObjs straight from the json, so we will have to figure out how to treat them here I CAN KILL THIS
        # ACTUALLY, I should probably separate tags from mykeys. If it has a menu name

class MenuGroup():
    def __init__(self, topObj:MenuObj=None, **kwargs) -> None:
    #def __init__(self, **kwargs): # ITS ALREADY A FUCKING GROUP. IF IT IS OF TYPE MENU IT IS A FUCKING MENUGROUP ALREADY, AND IN TURN, MENUGROUPS ARE ALREADY MENU OBJECTS, THEY JUST HAVE CHILDREN. I PROBABLY DONT NEED A MENUGROUP OBJECT, JUST A FUCKING REORDER ABUILITY
        self.topObj = topObj
        #need to repeat some of that stuff from MenuObj
        #NO, it should havea TOP OBJECT, and then the last arg would be a set of menuobjs
        self.menu_objects = kwargs # 
    def add_menu_object(self, menu_object):
        self.menu_objects.append(menu_object)

    #TODO rearange functions
    
    #TODO drop functions
    
    #TODO rename objects functions
    
# Do I actually currently have support for a full menubar and all its parameters yet? Let's test it?


# I ALSO NEED TO WRITE THESE OBJECTS TO FILE / vars() will be helpful, but I will need to parse them properly
rootMenu = MenuObj(type='menu',menuName='root', subMenu=[MenuObj(type='menu', menuName='fileMenu')]) 
roo2Menu = MenuGroup(MenuObj(type='menu',menuName='root',subMenu=MenuGroup(MenuObj)))
print(vars(rootMenu))
print((roo2Menu.menu_objects))




##### CURRENTLY I AM WORKING ON GETTING A STATICLY/HARDCODED/ STORED FULL MENUBAR TO MAKE SURE EVERYTHING IS STRUCTURED RIGHT