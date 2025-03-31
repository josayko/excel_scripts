import os

os.environ["PYTHON_WARNINGS"] = "ignore::UserWarning"

import tkinter as tk
from tkinter import TOP, Checkbutton, Entry, IntVar, StringVar
from tkinterdnd2 import TkinterDnD, DND_FILES

from matrix_parser import parser


def get_path(event):
    if lb.size() >= 2:
        lb.delete(1, lb.size() - 1)

    temp = event.data
    tokens = temp.split("} {")
    lb.insert(tk.END, event.data)
    printToFile = ""

    # for path in tokens:
    #     var = StringVar()
    #     results = parser.parse(path, "typ")
    #     formatted = ""
    #     for result in results.items():
    #         formatted = formatted + "\n" + result[0] + "\n" + result[1] + "\n"
    #     var.set(formatted)
    #     resultsWidget.configure(textvariable=var)
    #     printToFile = (
    #         printToFile + "\n------------------------------\n" + path + var.get()
    #     )
    #     print(path, var.get())

    with open("results.txt", "w") as f:
        f.write(printToFile)
    # Open the file in macos
    os.system("open results.txt")


window = TkinterDnD.Tk()
window.geometry("500x300")
window.title("SOFYA tools - Matrix reader")

nameVar = StringVar()

lb = tk.Listbox(window)
lb.insert(1, "Drag and drop your file here : ")
lb.pack(side=TOP, padx=5, pady=5)

var = StringVar()
var.set("Some text")
resultsWidget = Entry(window, state="readonly", width=100)
resultsWidget.pack(side=TOP)

var1 = IntVar(value=1)
c1 = Checkbutton(window, text="typ", variable=var1, onvalue=1, offvalue=0)
c1.pack()

lb.drop_target_register(DND_FILES)  # type: ignore
lb.dnd_bind("<<Drop>>", lambda e: get_path(e))  # type: ignore

# entryWidget.drop_target_register(DND_ALL)  # type: ignore
# entryWidget.dnd_bind("<<Drop>>", get_path)  # type: ignore

window.mainloop()
