import tkinter as tk

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