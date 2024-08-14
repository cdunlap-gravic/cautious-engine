import tkinter as tk
from abc import ABC, abstractmethod

#TODO move this to modules/objects/
class BaseMenu(ABC):
    def __init__(self): 
        pass
        
    def openWindow(self):
        self.window = tk.Toplevel(self.rootMenu)
        self.window.title(self.title)
        
    @abstractmethod    
    def closeWindow(self):
        pass
    
    
class EditCascade(BaseMenu):
    def __init__(self, root):
        self.title = 'Edit Cascade'
        self.rootMenu = root
        super().openWindow()
        
        textLabel = tk.Label(self.window, text='test label')
        textLabel.pack()

    def closeWindow(self):
        self.window.destroy()

class SubmitWin(BaseMenu):
    def __init__(self, root):
        self.title = 'Test Submit Menu'
        self.rootMenu = root
        super().openWindow()
        
        textLabel = tk.Label(self.window, text='Enter text:')
        textLabel.pack()
        
        self.textEntry = tk.Entry(self.window)
        self.textEntry.pack()
    
        submitButton = tk.Button(self.window, text='Submit', command=self.closeWindow)
        submitButton.pack()
        
    def closeWindow(self):
        textInput = self.textEntry.get()
        print(textInput)
        self.window.destroy()


    