import os; print(f"cwd is: {os.getcwd()}")


# Import(s)
from modules.config import keytags; print(keytags.MY_KEYS)
#rom ..config import keytags; print(keytags.MY_KEYS)
#from config import keytags as KT

###########################################################
####################################################################################################
#
# Object(s)
#
####################################################################################################
###########################################################

###############################
#
# MenuItem
#
###############################

class MenuItem:
    
    def __init__(self, type:str, **kwargs:dict) -> None:
        if type not in KT.MENU_TYPES:
            raise ValueError(f"""Invalid type: {type}. Must be one of: {KT.MENU_TYPES}""")
        self.type = type
        
        #TODO: WWERE IS THIS COMING FROM??? invalid keys needs to be moved out
        if KT.invalidKeyCheck(kwargs):
            raise ValueError(f"""Invalid keys: {KT.invalidKeyCheck(kwargs)}""")
        
        self.tags = {k: v for k, v in kwargs.items() if k not in KT.MY_KEYS}
        self.menuName = kwargs.get('menuName', None)
        self.subMenu = kwargs.get('subMenu', [])
        
    ####################################################################################################
    # Setters
    ####################################################################################################
    
    def setType(self, type:str) -> None:
        if type not in KT.MENU_TYPES:
            raise ValueError(f"""Invalid type: {type}. Must be one of: {KT.MENU_TYPES}""")
        self.type = type
        
        
    #######################################################################
    #######################################################################   
   
    def setTags(self, **kwargs:dict) -> None:
        if KT.invalidKeyCheck(kwargs):
            raise ValueError(f"""Invalid keys: {KT.invalidKeyCheck(kwargs)}""")
        self.tags = {k: v for k, v in kwargs.items() if k not in KT.MY_KEYS}
        
        
    #######################################################################
    #######################################################################
    
    def setMenuName(self, menuName:str) -> None:
        self.menuName = menuName
        
        
    ####################################################################################################
    # Getters
    ####################################################################################################
    
    def getType(self) -> str:
        return self.type
    
    
    #######################################################################
    #######################################################################
    
    #TODO should probably validate that the tag ISNT MYKEY
    def getTag(self, tag:str) -> any:
        try:
            return self.tags.get(tag)
        except KeyError:
            raise KeyError(f"""Tag '{tag}' not found in MenuItem""")


    #######################################################################
    #######################################################################    
    
    def getMenuName(self) -> str:
        try:
            return self.menuName
        except AttributeError:
            raise AttributeError(f"""MenuItem does not have a menuName""")
    

    ####################################################################################################
    # subMenu Functions
    ####################################################################################################
   
    def listSubMenuItems(self, mode: str = "Print"): # THIS IS SUBPAR BUT IT WORKS FOR NOW  ¯\_(ツ)_/¯
        if mode == "Print":
            print(self.subMenu)
        else:
            pass
        
    #######################################################################
    #######################################################################         
    
    def addSubMenuItem(self, item: "MenuItem", bypass: bool = False):
        #adds item to end of submenu (was menuGroup)
        #TODO validate item if it exists, and if so, let user know, w/ bypass
        if not bypass:
            pass
        self.subMenu.append(item)
        pass
    
    
    #######################################################################
    ####################################################################### 
    
    def dropSubMenuItem(self, item: "MenuItem", bypass: bool = False):
        #removes item from submenu (was menuGroup)
        #check if item exists first
        #and maybe do a confirmation mode?
        #should also have a bypass bool to skip confirmation
        if not bypass:
            pass
        self.subMenu.remove(item)
    
    
    #######################################################################
    #######################################################################     
    
    def insertSubMenuItem(self, item: "MenuItem", index: int):
        #inserts item into submenu as position (was menuGroup)
        pass


    #######################################################################
    #######################################################################         
    
    def moveSubMenuItemUp(self, index):
        """
          Simple Swap up function
        """
        if index <= 0 or index >= len(self.subMenu):
            raise IndexError(f"""Invalid index for {self.menuName}'s subMenu item initial position""") #need to verify if this will work for name 
            # Maybe label would work better?
        self.subMenu[index - 1], self.subMenu[index] = self.subMenu[index], self.subMenu[index - 1]


    #######################################################################
    #######################################################################          

    def moveSubMenuItemDown(self, index):
        """
          Simple Swap down function
        """
        if index < 0 or index >= len(self.subMenu) - 1:
            raise IndexError(f"""Invalid index for {self.menuName}'s subMenu item initial position""")
        self.subMenu[index + 1], self.subMenu[index] = self.subMenu[index], self.subMenu[index + 1]
    
    
    #######################################################################
    #######################################################################     

    def findMenuItem():
        pass
    
    
    #######################################################################
    #######################################################################     

    def insertMult():
        pass


    #######################################################################
    #######################################################################     

    def removeMult():
        pass
    

    
    #######################################################################
    #######################################################################     

    #TODO: Other Funcs
    def defineUnderlines(self): # sorts out all underlines in the topmost layer. This func should also call itself on specific children objects for each cascade layer; This should also be automatically called whenever changes are made to the whole cascade/menubar
        pass

    #TODO rearange functions
    
    #TODO drop functions
    
    #TODO rename objects functions
    


