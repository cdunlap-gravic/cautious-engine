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