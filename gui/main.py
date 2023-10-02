#!/usr/bin/env python

from tkinter import TOP, Entry, Label, StringVar
from tkinterdnd2 import *

def get_path(event):
    pathLabel.configure(text = event.data)
    temp = event.data[1:-1]
    tokens = temp.split("} {")
    print("DEBUG: ", tokens)

root = TkinterDnD.Tk()
root.geometry("350x100")
root.title("SOFYA tools - Matrix reader")

nameVar = StringVar()

entryWidget = Entry(root)
entryWidget.pack(side=TOP, padx=5, pady=5)

pathLabel = Label(root, text="Drag and drop files in the entry box")
pathLabel.pack(side=TOP)

entryWidget.drop_target_register(DND_ALL)
entryWidget.dnd_bind("<<Drop>>", get_path)

root.mainloop()

