import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod


class BaseMenu(ABC):
    def __init__(self): 
        pass
        
    def openWindow(self):
        self.window = tk.Toplevel(self.root_menu)
        self.window.title(self.title)
        
    @abstractmethod    
    def closeWindow(self):
        pass
    
    
class EditCascade(BaseMenu):
    def __init__(self, root):
        self.title = 'Edit Cascade'
        self.root_menu = root
        super().openWindow()
        
        text_label = tk.Label(self.window, text='test label')
        text_label.pack()

    def closeWindow(self):
        self.window.destroy()

class SubmitWin(BaseMenu):
    def __init__(self, root):
        self.title = 'Test Submit Menu'
        self.root_menu = root
        super().openWindow()
        
        text_label = tk.Label(self.window, text='Enter text:')
        text_label.pack()
        
        self.text_entry = tk.Entry(self.window)
        self.text_entry.pack()
    
        submit_button = tk.Button(self.window, text='Submit', command=self.closeWindow)
        submit_button.pack()
        
    def closeWindow(self):
        text_input = self.text_entry.get()
        print(text_input)
        self.window.destroy()


    