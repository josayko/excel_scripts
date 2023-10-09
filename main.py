from tkinter import TOP, BOTTOM, Entry, Label, Text, StringVar
from tkinterdnd2 import *
from matrix_parser import parser


def get_path(event):
    temp = event.data[1:-1]
    tokens = temp.split("} {")
    label.configure(text=tokens)
    for path in tokens:
        var = StringVar()
        sheetName, result = parser.parse(path, "typ")
        var.set(sheetName + "\n" + result + "\n")
        resultsWidget.configure(textvariable=var)
        print(var.get())


window = TkinterDnD.Tk()
window.geometry("350x100")
window.title("SOFYA tools - Matrix reader")

nameVar = StringVar()

entryWidget = Entry(window)
entryWidget.pack(side=TOP, padx=5, pady=5)

label = Label(window, text="Drag and drop files in the entry box")
label.pack(side=TOP)

var = StringVar()
var.set("Some text")
resultsWidget = Entry(window, state="readonly", width=100)
resultsWidget.pack(side=TOP)


entryWidget.drop_target_register(DND_ALL)
entryWidget.dnd_bind("<<Drop>>", get_path)

window.mainloop()
