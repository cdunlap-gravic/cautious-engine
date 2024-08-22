# write to file
import json
from objects.MenuItem import *
from utils import *
from hcRootMI import *
import inspect

testsub = rootTest3

# FROM THAT HARDCODE TEST ----> autoprocess underlines and separators (key thing for this stage is at least the separators)
##################################################################

def ParseOutGroupsFromRoot(root):
    ln(2, f"""Begin Processing of groups under '{root.menuName}':""")
    for header in root.subMenu:
        ParseOutGroups(header)
        ln(0, '')
    ln(1, f"""Parsing all groups under '{root.menuName}': Done!""")    
    

##################################################################

def ParseOutGroups(mi): #or, def degroupify(mi):
    for child in mi.subMenu[:]:
        if child.type == 'group':
            order = 0
            for grandchild in child.subMenu:
                mi.insertSubMenuItem(grandchild, mi.subMenu.index(child) + order)
                order+=1
            if mi.subMenu.index(child) != len(mi.subMenu)-1:
                mi.addSeparator(mi.subMenu.index(child)+order) # this should be replaced with prefab object calling
            mi.dropSubMenuItem(child)
        if child.type == 'menu' or 'group':
            ParseOutGroups(child)
                

##################################################################

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