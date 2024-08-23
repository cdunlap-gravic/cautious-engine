# load from file

from objects.MenuItem import *

from hcRootMI import *

print(rootTest1.menuName)

jsonFile = 'output.json'

with open(jsonFile) as file:
    json = file.read()
    
print(json)


# ! now what to do with <json>

