import tkinter as tk

def rename_menu(parent_menu):
    global popup
    def rename_callback():
        new_name = entry.get()
        parent_menu.entryconfig(0, label=new_name)
        popup.destroy()

    popup = tk.Toplevel()
    popup.title("Rename Menu")

    label = tk.Label(popup, text="Enter new name:")
    label.pack()

    entry = tk.Entry(popup)
    entry.pack()

    rename_button = tk.Button(popup, text="Rename", command=rename_callback)
    rename_button.pack()

def on_right_click(event):
    popup.post(event.x_root, event.y_root)

root = tk.Tk()

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open") 

file_menu.add_command(label="Save")

file_menu.add_separator()
file_menu.add_command(label="Rename", 
 command=lambda:rename_menu(file_menu))

file_menu.bind("<Button-3>", on_right_click)

root.mainloop()