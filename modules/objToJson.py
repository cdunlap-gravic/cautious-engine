# write to file
import json
from objects.MenuItem import *
from utils import *
from hcRootMI import *
import inspect

testsub = rootTest0

# FROM THAT HARDCODE TEST ----> autoprocess underlines and separators (key thing for this stage is at least the separators)
##################################################################

# still need to parse out groups and insert separators
def ParseOutGroups(mi):
    # ok, so how are we gonna do this?
    # 
    # whenever there is a group (and not the first) add a separator at the top. (actually, groups are helpful for menu builder... maybe I should just process it in menufromjson instead??? actually lets test this first conversion)
    # 
    # 
    # 
    # 
    pass


##################################################################
# and write to file

# This one actually worked!!!! Let's kill the chicken scratch notes and failed attempts!
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