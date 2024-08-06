import tkinter as tk
from tkinter import messagebox

class _BaseMenu(object):
    # Why do I need to intiallize anything? maybe a base resolution based on screen size? MAYBE? 
    # Techincally you should NEVER see the title 'Title' anywhere
    # NEED TO RESTRUCTURE THIS AS AN ABC
    def __init__(self): #pass
        self.title = 'Title'
        self.root_menu = None
        
    def openWindow(self):
        self.window = tk.Toplevel(self.root_menu)
        self.window.title(self.title)
        
    def closeWindow(self):
        self.window.destroy()
    

class EditCascade(_BaseMenu):
    def __init__(self, root):
        self.title = 'Edit Cascade'
        self.root_menu = root
        super().openWindow()
        
        text_label = tk.Label(self.window, text='test label')
        text_label.pack()
        # I think I'm getting too convoluted and confusing myself... should take a step back with this but I think I'm on the right track. I just need to decide WHERE I want to call/initialize values and where I want to put my functions, either in the child or in the parent. I think this last line is correct though. 
        #### STOPPED HERE FOR VIV1 TMF MAINTENANCE #####
        # ok, each child object should define its own title and root could be assumed. But the question is do I want to build these menus out of a gui builder too? Or should I just design it by hand anyway? For now, let's just focus on building the menubar builder, and any subsequent windows should be "hardcoded" to the degree of good coding, but not fully futureproofed. radio switches should be dynamic in design, but layout can be programed on a scalability factor and dynamic in number of spaces in the grid can be dynamic, but this feature doesn't have to come from a parent object. If I need that level of detail, I can work on that LATER as a future feature, and work towards building that as a possible design feature now, but not implement it 


def open_new_window(rootMenu):
    new_window = tk.Toplevel(rootMenu)
    new_window.title("Enter Text")

    def submit_text():
        text_input = text_entry.get()
        # Do something with the text input
        print(text_input)
        new_window.destroy()

    text_label = tk.Label(new_window, text="Enter text:")
    text_label.pack()
 
    text_entry = tk.Entry(new_window)
    text_entry.pack()

    submit_button = tk.Button(new_window, text="Submit", command=submit_text)
    submit_button.pack()
    # Add content to the new window here


# Basic window example with a close button
def baseWindow(rootMenu):
    new_window = tk.Toplevel(rootMenu)
    new_window.title("New Window")
    def closeWindow():
        new_window.destroy()
    textLabel = tk.Label(new_window, text="Test window.")
    textLabel.pack()

    closeButton = tk.Button(new_window, text="Close", command=closeWindow)
    closeButton.pack()
    
def deleteCasc(rootMenu):
    ## Or, do I actually want to build my own here? Pretty sure I would rather build my own. I don't really need this to be a modal, and if I do, then I should convert all of these windows to modals
    new_window = messagebox.askyesno(message='Ya sure?', icon='question', title='DELETE DELETE DELETE')
    
#TODO: Ok, WHAT MENUS DO I ACTUALLY NEED? Let's at least build
# a quick skeleton with window opening and their names

def _(rootMenu):
    new_window = tk.Toplevel(rootMenu)
    new_window.title("_")
    def closeWindow():
        #probably throw a save prompt here, or autosave
        new_window.destroy()
    