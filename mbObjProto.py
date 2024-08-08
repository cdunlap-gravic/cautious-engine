
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
        self.subMenu = kwargs.get('subMenu', None) # this will be a list of dicts
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
    


class MenuGroup:
    def __init__(self, name=None, **kwargs) -> None:
        self.name = name
        #need to repeat some of that stuff from MenuObj
        self.menu_objects = kwargs
    def add_menu_object(self, menu_object):
        self.menu_objects.append(menu_object)

    #TODO rearange functions
    
    #TODO drop functions
    
    #TODO rename objects functions
    
# Do I actually currently have support for a full menubar and all its parameters yet? Let's test it?


# I ALSO NEED TO WRITE THESE OBJECTS TO FILE / vars() will be helpful, but I will need to parse them properly
rootMenu = MenuObj(type='menu',menuName='root', subMenu=[{'type':'menu', 'menuName':'fileMenu'}]) 
#roo2Menu = MenuObj(type='menu',menuName='root', subMenu=MenuGroup(name='fileMenu', {'type':'menu', 'menuName':'fileMenu'}))
print(vars(rootMenu))
#print(vars(roo2Menu.subMenu))