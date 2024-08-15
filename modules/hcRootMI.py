from objects.MenuItem import *


rootTest0 = MenuItem(
    type='menu',
    menuName='rootTest0',
    subMenu=[
        MenuItem(
            type='menu',
            menuName='fileMenu',
            label='File',
            underline=0,
            subMenu=[
                MenuItem(
                    type='menu',
                    menuName='group',
                    subMenu=[
                        MenuItem( 
                            type="command",
                            label="[Edit Cascade]",
                            background="#FFCC66",
                            underline= 0,
                            command="lambda: MBM.EditCascade(root)"
                        ),
                        MenuItem(
                            type="command",
                            label="[Delete Cascade]",
                            background="#FF6666",
                            underline=0,
                            command="lambda: MBM.SubmitWin(root)"
                        )       
                    ]
                ),
                MenuItem(
                    type='menu',
                    menuName='group2',
                    subMenu=[
                        MenuItem( 
                            type="command",
                            label="[Edit Menu Group]",
                            background="#FFCC66",
                            underline= 0,
                            command="lambda: print('Opening file...')"
                        ),
                        MenuItem(
                            type= "command",
                            label= "Open...",
                            underline= 0,
                            command= "lambda: print('Opening file...')"
                        ),
                        MenuItem(
                            type= "command",
                            label= "Save As...",
                            underline= 0,
                            command= "lambda: print('Opening file...')"
                        )          
                    ]
                ),
                MenuItem(
                    type='menu',
                    menuName='group3',
                    subMenu=[
                        MenuItem( 
                            type="command",
                            label="[Edit Menu Group]",
                            background="#FFCC66",
                            underline= 0,
                            command="lambda: MBM.EditCascade(root)"
                        ),
                        MenuItem(
                            type= "command",
                            label= "Auto Save",
                            underline= 0,
                            command= "lambda: print('Opening file...')"
                        ),
                        MenuItem(
                            type= "menu",
                            menuName="prefMenu",
                            label= "Preferences",
                            underline= 0,
                            subMenu=[
                                MenuItem( 
                                    type="menu",
                                    menuName="subgroup",
                                    subMenu=[
                                        MenuItem( 
                                            type="command",
                                            label="[Edit Cascade]",
                                            background="#FFCC66",
                                            underline= 0,
                                            command="lambda: MBM.EditCascade(root)"
                                        ),
                                        MenuItem(
                                            type="command",
                                            label="[Delete Cascade]",
                                            background="#FF6666",
                                            underline=0,
                                            command="lambda: MBM.SubmitWin(root)"
                                        )
                                    ]
                                ),
                                MenuItem(
                                    type="menu",
                                    menuName="subgroup",
                                    subMenu=[
                                        MenuItem( 
                                            type="command",
                                            label="[Edit Menu Group]",
                                            background="#FFCC66",
                                            underline= 0,
                                            command="lambda: print('Opening file...')"
                                        ),
                                        MenuItem(
                                            type= "command",
                                            label= "Settings",
                                            underline= 0,
                                            command= "lambda: print('Opening file...')"
                                        ),
                                        MenuItem(
                                            type= "command",
                                            label= "Themes",
                                            underline= 0,
                                            command= "lambda: print('Opening file...')"
                                        )
                                    ]
                                ),
                                MenuItem(
                                    type="menu",
                                    menuName="subgroup",
                                    subMenu=[
                                        MenuItem(
                                            type="command",
                                            label="[Add Group]",
                                            background="#66ff66",
                                            underline= 0,
                                            command="lambda: print('Opening file...')"
                                        )
                                    ]
                                )          
                            ]
                        )          
                    ]
                ),
                MenuItem(
                    type="menu",
                    menuName="subgroup",
                    subMenu=[
                        MenuItem(
                            type="command",
                            label="[Add Group]",
                            background="#66ff66",
                            underline= 0,
                            command="lambda: print('Opening file...')"
                        )
                    ]
                )
            ]
        ),
        MenuItem(
            type="menu",
            menuName="addMenu",
            label="+",
            underline=0,
            subMenu=[
                MenuItem(
                    type="command",
                    label="[Add Cascade]",
                    background="#66ff66",
                    underline= 0,
                    command="lambda: print('Opening file...')"
                )
            ]    
        )
    ]
)


rootTest1 = MenuItem(
    type='menu',
    menuName='rootTest1',
    subMenu=[
        MenuItem(
            type='menu',
            menuName='fileMenu',
            label='File',
            subMenu=[
                MenuItem(
                    type='menu',
                    menuName='group',
                    subMenu=[
                        MenuItem( 
                            type="command",
                            label="[Edit Cascade]"),
                        MenuItem(
                            type="command",
                            label="[Delete Cascade]")]),
                MenuItem(
                    type='menu',
                    menuName='group2',
                    subMenu=[
                        MenuItem( 
                            type="command",
                            label="[Edit Menu Group]"),
                        MenuItem(
                            type= "command",
                            label= "Open..."),
                        MenuItem(
                            type= "command",
                            label= "Save As...")]),
                MenuItem(
                    type='menu',
                    menuName='group3',
                    subMenu=[
                        MenuItem( 
                            type="command",
                            label="[Edit Menu Group]"),
                        MenuItem(
                            type= "command",
                            label= "Auto Save"),
                        MenuItem(
                            type= "menu",
                            menuName="prefMenu",
                            label= "Preferences",
                            subMenu=[
                                MenuItem( 
                                    type="menu",
                                    menuName="subgroup",
                                    subMenu=[
                                        MenuItem( 
                                            type="command",
                                            label="[Edit Cascade]"),
                                        MenuItem(
                                            type="command",
                                            label="[Delete Cascade]")]),
                                MenuItem(
                                    type="menu",
                                    menuName="subgroup",
                                    subMenu=[
                                        MenuItem( 
                                            type="command",
                                            label="[Edit Menu Group]"),
                                        MenuItem(
                                            type= "command",
                                            label= "Settings"),
                                        MenuItem(
                                            type= "command",
                                            label= "Themes")]),
                                MenuItem(
                                    type="menu",
                                    menuName="subgroup",
                                    subMenu=[
                                        MenuItem(
                                            type="command",
                                            label="[Add Group]")])])]),
                MenuItem(
                    type="menu",
                    menuName="subgroup",
                    subMenu=[
                        MenuItem(
                            type="command",
                            label="[Add Group]")])]),
        MenuItem(
            type="menu",
            menuName="addMenu",
            label="+",
            underline=0,
            subMenu=[
                MenuItem(
                    type="command",
                    label="[Add Cascade]")])])


testDict = {
    "type": "menu",
    "menuName": "root",
    "subMenu": [
        {
            "type": "menu",
            "menuName": "fileMenu",
            "label": "File",
            "underline": 0,
            "subMenu": [
                {
                    "type": "command",
                    "label": "[Edit Cascade]",
                    "background": "#FFCC66",
                    "underline": 0,
                    "command": "lambda: MBM.EditCascade(root)"
                },
                {
                    "type": "command",
                    "label": "[Delete Cascade]",
                    "background": "#FF6666",
                    "underline": 0,
                    "command": "lambda: MBM.SubmitWin(root)"
                },
                {
                    "type": "separator",
                    "label": ""
                },
                {
                    "type": "command",
                    "label": "[Edit Menu Group]",
                    "background": "#FFCC66",
                    "underline": 0,
                    "command": "lambda: print('Opening file...')"
                },
                {
                    "type": "command",
                    "label": "Open...",
                    "underline": 0,
                    "command": "lambda: print('Opening file...')"
                },
                {
                    "type": "command",
                    "label": "Save As...",
                    "underline": 0,
                    "command": "lambda: print('Opening file...')"
                },
                {
                    "type": "separator",
                    "label": ""
                },
                {
                    "type": "command",
                    "label": "[Edit Menu Group]",
                    "background": "#FFCC66",
                    "underline": 0,
                    "command": "lambda: print('Opening file...')"
                },
                {
                    "type": "command",
                    "label": "Auto Save",
                    "underline": 0,
                    "command": "lambda: print('Opening file...')"
                },
                {
                    "type": "menu",
                    "menuName": "prefMenu",
                    "label": "Preferences",
                    "underline": 0,
                    "subMenu": [
                        {
                            "type": "command",
                            "label": "[Edit Cascade]",
                            "background": "#FFCC66",
                            "underline": 0,
                            "command": "lambda: print('Opening file...')"
                        },
                        {
                            "type": "command",
                            "label": "[Delete Cascade]",
                            "background": "#FF6666",
                            "underline": 0,
                            "command": "lambda: print('Opening file...')"
                        },
                        {
                            "type": "separator",
                            "label": ""
                        },
                        {
                            "type": "command",
                            "label": "[Edit Menu Group]",
                            "background": "#FFCC66",
                            "underline": 0,
                            "command": "lambda: print('Opening file...')"
                        },
                        {
                            "type": "command",
                            "label": "Settings",
                            "underline": 0,
                            "command": "lambda: print('Opening file...')"
                        },
                        {
                            "type": "command",
                            "label": "Themes",
                            "underline": 0,
                            "command": "lambda: print('Opening file...')"
                        },
                        {
                            "type": "separator",
                            "label": ""
                        },
                        {
                            "type": "command",
                            "label": "[Add Group]",
                            "background": "#66ff66",
                            "underline": 0,
                            "command": "lambda: print('Opening file...')"
                        }
                    ]
                },
                {
                    "type": "separator",
                    "label": ""
                },
                {
                    "type": "command",
                    "label": "[Add Group]",
                    "background": "#66ff66",
                    "underline": 0,
                    "command": "lambda: print('Opening file...')"
                }
            ]
        },
        {
            "type": "menu",
            "menuName": "addMenu",
            "label": "+",
            "underline": 0,
            "subMenu": [
                {
                    "type": "command",
                    "label": "[Add Cascade]",
                    "background": "#66ff66",
                    "underline": 0,
                    "command": "lambda: print('Opening file...')"
                }
            ]
        }
    ]
}