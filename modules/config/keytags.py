MY_KEYS = frozenset({'type', 'menuName', 'subMenu'})
MENU_TYPES = frozenset({'menu', 'command', 'iterator', 'separator'})
TKINTER_ARGS = frozenset({'accelerator', 'activebackground', 'activeforeground', 'background', 'bitmap', 'columnbreak', 'command', 'compound', 'font', 'foreground', 'hidemargin', 'image', 'label', 'menu', 'offvalue', 'onvalue', 'selectcolor', 'selectimage', 'state', 'underline', 'value', 'variable'})

currently_known_not_supported = frozenset({'font'})
needs_functions_to_be_a_useful_tag = frozenset({'accelerator'})

ALLOWED_KEYS = frozenset(TKINTER_ARGS | MY_KEYS)