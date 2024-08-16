# write to file
import json
from objects.MenuItem import *
from utils import *
from hcRootMI import *
import inspect

testsub = rootTest0
testmode = True
#print(testsub.menuName)
# FROM THAT HARDCODE TEST ----> autoprocess underlines and separators (key thing for this stage is at least the separators)
# and write to file
###############################################################
###############################################################
###############################################################
###############################################################


#
#
# what the hell feels wrong about this???  
# who fucking knows ¯\_(ツ)_/¯
#
#
#
# SHOULD PROBABLY make inserting separators a separate task.
#
# can also consider making a bag of "lost menu items" for when a cascade/group are deleted, so those buttons aren't lost forever
#
#
#
# what the hell is going here and why????????
# type isn't printing
# order is weird but that's ok
# I dont have any separation between menuobjects in a sub menu (my fault definitely) 
# still need brackets AND COMMAS actually, 
# besides that, everything is fine. Still need to process out menu groups and insert separators
#
# Don't forget commas where appropriate
# current test is coming from 
# lets archive this and start from scratch to follow my own logic

#OK I somehow fixed type and menuname, but WHY DO I HAVE EMPTY MENUNAME AND SUBMENU IN CHILDREN? Bc I'm not calling things right am I?
# OHHHHHHHHHHHHHHHHHH for tags I should really be just recursing again, right? that's how I'm getting no thats not it
# I am not checking in that LAST print if empty


# FINALLY. Ok, now lets parse out menuitems with {} and add commas!
#
#
#
#
#
#
indent="    "


def printoutItems(mi, l=0):
    for n, v in vars(mi).items(): 
        if isinstance(v, list) and len(v)>0: 
            print(f"{indent * l}'subMenu': [")
            for i in v:
                printoutItems(i,l+1) 
            print(f"{indent * (l)}]")
        elif isinstance(v, dict) and n=='tags':
            for kk, vv in v.items():
                if isinstance(vv, int):
                    print(f"{indent * l}'{kk}':{vv}") 
                else:
                    print(f"{indent * l}'{kk}':'{vv}'")
        elif v != None and v != []:
            print(f"{indent * l}'{n}':'{v}'")
            
            
            
            
def v3bakprintoutItems(mi, l=0):
    for n, v in vars(mi).items(): 
        if isinstance(v, list) and len(v)>0: 
            print(f"{indent * l}'subMenu': [")
            for i in v:
                v3bakprintoutItems(i,l+1) 
            print(f"{indent * (l)}]")
        elif isinstance(v, dict) and n=='tags':
            for kk, vv in v.items():
                if isinstance(vv, int):
                    print(f"{indent * l}'{kk}':{vv}") 
                else:
                    print(f"{indent * l}'{kk}':'{vv}'")
        elif v != None and v != []:
            print(f"{indent * l}'{n}':'{v}'")



def v2printoutItems(mi, l=0): # start with a menu item, and what level it's on (more for indentations)
    for n, v in vars(mi).items(): #navigate through each variable/attr/item of the MenuItem, with name:value pairs
        if isinstance(v, list) and len(v)>0: #if the value is a list, it should be a submenu, and I only want to process nondefaultedempty
            print(f"{indent * l}'subMenu': [") # just adding indents here #we KNOW it's a submenu bc ln45
            #NOW WE NEED TO PARSE THE SUBMENU (but why is this at top? bc else is just print the n:v pair)
            for i in v: #for each item in the submenu
                v2printoutItems(i,l+1) #just recurse it back
            print(f"{indent * (l)}]")#we need to close that submenu bracket!
            #ok submenu done (in theory, now lets handle everything else in the menuitem)
        #now what do we do if it's not a submenu? Well what if it's tags?
        elif isinstance(v, dict) and n=='tags': #ITS TAGS LETS DO IT
            for kk, vv in v.items(): #just navigate through the key:value pairs buddy
                #now what if that value is an int?
                if isinstance(vv, int):
                    print(f"{indent * l}'{kk}':{vv}") #don't forget that indent
                else:
                    print(f"{indent * l}'{kk}':'{vv}'")
            #OK TAGS ARE DONE,  but what aobut the rest???
        else: #this is the rest ie, menuName and Type
            if v != None and v != []:
                print(f"{indent * l}'{n}':'{v}'")
    

def OLDprintoutItems(mi, l=0):
    for n, v in vars(mi).items():
        if isinstance(v, list)and len(v)>0: # if the submenu is populated, and not the default empty list // Need similar line for tag parsing
            for _ in range (l):
                print(f"    {l}.1",end="")
            print(f"'subMenu': [")
            for i in v:
                OLDprintoutItems(i,l+1)
            for _ in range (l):
                print(f"    {l}.2",end="")
            print(f']')
        else:
            # if statement or tags, these need to be parsed
            if isinstance(v, dict) and n == 'tags':
                for kk, vv in v.items():
                    for _ in range (l): #I had it set to l-1, which was the problem
                        print(f"    {l}.4",end="")
                    if isinstance(vv, int):
                        print(f"'{kk}': {vv}") # FIXED
                    else:
                        print(f"'{kk}': '{vv}'") # FIXED
                    
            #else: # NEED TO REMOVE SUBMENU FORM THESE PRINTS OR IF MENUNAME=NONE
            elif (n == 'menuName' and v != None) or (n == 'subMenu' and len(v)>0):
                for _ in range (l):
                    print(f"    {l}.3",end="")
                if isinstance(v,int):
                    print(f"'{n}': {v}")
                else:
                    print(f"'{n}': '{v}'")
    return


###############################################################
###############################################################
###############################################################
###############################################################

def MItoJson(MI):
    
    # For each item in vars, that is NOT submenu, return key, value
    # if submenu, create list of dicts
        #also if group, and followed w/ a group, add sep
        
    return {
        
        "type": MI.type
    }
    
def main():
    if testmode:
        #ln(2,vars(testsub))
        print("this should be it:")
        #for n, v in inspect.getmembers(testsub,lambda o: not inspect.ismethod(o)):
        #    if not n.startswith("__"):
        #        print(f"{n}:{v}")
        #ln()
        ln(1,"lets try this then????:")
        printoutItems(testsub)
    ln(3)
    rootTest = json.dumps(MItoJson(testsub))
    print(f"goal output:   {testDict}\n")
    ln(3)
    print(f"actual output: {rootTest}\n")
    
    
"""
class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

def person_to_json(person):
    return {
        "name": person.name,
        "age": person.age,
        "address": {
            "street": person.address.street,
            "city": person.address.city
        }
    }

person = Person("Bob", 25, Address("123 Main St", "Anytown"))
person_json = json.dumps(person_to_json(person))
print(person_json)
"""
if __name__ == '__main__':
    main()