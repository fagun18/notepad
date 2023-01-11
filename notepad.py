import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Personal Notepad")

text = tk.Text(root)
text.pack()

def save_as():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    text_input = text.get("1.0", 'end-1c')
    file.write(text_input)
    file.close()

def open_file():
    file = filedialog.askopenfile(mode='r', defaultextension=".txt")
    text_input = file.read()
    text.insert('end', text_input)
    file.close()

menubar = tk.Menu(root)
file = tk.Menu(menubar, tearoff=0)
file.add_command(label="Open", command=open_file)
file.add_command(label="Save As", command=save_as)
menubar.add_cascade(label="File", menu=file)
root.config(menu=menubar)
root.mainloop()
