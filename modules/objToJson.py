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


def printoutItems(mi, l=0):
    for n, v in vars(mi).items():
        if isinstance(v, list)and len(v)>0:
            for _ in range (l):
                print("    ",end="")
            print(f"subMenu: [")
            for i in v:
                printoutItems(i,l+1)
            for _ in range (l):
                print("    ",end="")
            print(f']')
        else:
            for _ in range (l):
                print("    ",end="")
            # if statement or tags, these need to be parsed
            
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
        print(vars(testsub))
        ln()
        ln()
        print("this should be it:")
        for n, v in inspect.getmembers(testsub,lambda o: not inspect.ismethod(o)):
            if not n.startswith("__"):
                print(f"{n}:{v}")
        
        ln()
        print("lets try this then????:")
        printoutItems(testsub)
        

    rootTest = json.dumps(MItoJson(testsub))
    print(f"goal output:   {testDict}\n")
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