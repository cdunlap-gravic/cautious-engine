# write to file
import json
from objects.MenuItem import *
from utils import *
from hcRootMI import *
import inspect

testsub = rootTest3

# FROM THAT HARDCODE TEST ----> autoprocess underlines and separators (key thing for this stage is at least the separators)
##################################################################

# still need to parse out groups and insert separators
## SUCK IT! We'll just handle root separately, and the rest can be recursive after
# * SO IN HERE, I NEED TO MAKE SURE IT RECURSEIVELY RUNS PARSE OUT GROUPS ON EACH CHILD, AND IN HERE I COULD PROBABLY RUN PARSE UNDERLINES
def ParseOutGroupsFromRoot(root):
    ln(2, f"""Begin Processing of groups under '{root.menuName}':""")
    for header in root.subMenu:
        ParseOutGroups(header)
        ln(0, '')
    ln(1, f"""Parsing all groups under '{root.menuName}': Done!""")    
    

def ParseOutGroups(mi): #or, def degroupify(mi):
    # ok, so how are we gonna do this?
    # 
    # whenever there is a group (and not the first) add a separator at the top. (actually, groups are helpful for menu builder... maybe I should just process it in menufromjson instead??? actually lets test this first conversion)
    # 
    # 
    # ASSUMING HARDCODED VERSION W GROUPS, WE ARE JUST focused on separators
    # ! Alright, I know I have to rework a lot of shit to accomodate this, but I DO need this...
    # ! Let's add type='group'
    
    
    for child in mi.subMenu[:]:
        if child.type == 'group':
            order = 0
            for grandchild in child.subMenu:
                mi.insertSubMenuItem(grandchild, mi.subMenu.index(child) + order)
                order+=1
            if mi.subMenu.index(child) != len(mi.subMenu)-1:
                mi.addSeparator(mi.subMenu.index(child)+order)
            mi.dropSubMenuItem(child)
        if child.type == 'menu' or 'group':
            ParseOutGroups(child)
                
                
"""
    if all(child.type == 'menu' and not all(grandchild.type == 'menu') for child in mi.subMenu):

        FUUUUUUUUUUCK I need to do a rewrite of a couple scirpts and account for MenuItem.type == 'group'
        for child in mi.subMenu:
        
        I could also simply add a tag called group, 
        actually that should be the solution but I don't want to rebuild old code
        
        if all children are ALSO menus, then they HAVE to be groups
            
            , and all one level down children are menus, then that is a menu of groups

         
    now, we need to go down another level
    
    ok, now we need to check (this should be a separte function probably to recurse  thourgh to the lowest levels, and I should have a plugin point for other tasks)
    pass
"""

##################################################################
# and write to file

# ? This one actually worked!!!! Let's kill the chicken scratch notes and failed attempts!
def ObjToJson(mi):
    values = {}
    for n, v in vars(mi).items():
        if isinstance(v, dict) and n=='tags':
            for kk, vv in v.items():
                values[kk]=vv
        elif isinstance(v, list) and len(v)>0:
            values['subMenu']=[]
            for i in v:
                values['subMenu'].append(ObjToJson(i))
        elif v != None and v != []:
            values[n]=v
    return values


##################################################################

def main():
    ln(2)
    #rootTest = json.dumps(printJson(rootTest0))
    ln(2,f"goal output:   {testDict}")

    ln(2,ObjToJson(testsub))


if __name__ == '__main__':
    main()