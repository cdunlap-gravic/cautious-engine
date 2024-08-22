from MenuItem import *

# NOTE
# 
# This whole section can be used for regularly established items, like a file open and should be made flexibly to allow for customizeablity 
#  when adding prefabs, but this will mostly include the builder prefabs
# 






COL_YLW = '#FFCC66'
COL_RED = '#FF6666'
COL_GRN = '#66FF66'
# Prefab Menu Items
CascEdit = MenuItem(type='command', label='[Edit Cascade]', background=COL_YLW, command='lambda: MBM.EditCascade(root)')
CascDelete = MenuItem(type='command', label='[Delete Cascade]', background=COL_RED, command='lambda: MBM.DeleteCascade(root)')
CascAdd = MenuItem(type='command', label='[Add Cascade]', background=COL_GRN, command='lambda: MBM.EditCascade(root)')

GroupAdd =  MenuItem(type='command', label='[Add Group]', background=COL_GRN, command='lambda: MBM.EditCascade(root)')

# Prefab Menu Groups
CascEditGrp = MenuItem(type='group', menuName='CascEditGroup', subMenu=[CascEdit, CascDelete])
CascAddGrp = MenuItem(type='group', menuName='CascAddGroup', subMenu=CascAdd)
GroupAddGrp = MenuItem(type='group', menuName='GroupAddGroup', subMenu=GroupAdd)
