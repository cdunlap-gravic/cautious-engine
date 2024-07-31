import tkinter as tk

def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("New Window")
    # Add content to the new window here

def main():
    root = tk.Tk()
    root.title("Main Window")

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(label="Open")
    file_menu.add_command(label="Save")


    edit_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut")
    edit_menu.add_command(label="Copy")
    edit_menu.add_command(label="Paste")


    tools_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Tools", menu=tools_menu)
    tools_menu.add_command(label="Options")
    tools_menu.add_command(label="Customize")

    help_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About")

    view_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="View", menu=view_menu)
    view_menu.add_command(label="New Window", command=open_new_window)

    root.mainloop()

if __name__ == "__main__":
    main()