from Tkinter import *
import tkFileDialog
import json
root = Tk()

def load(box):
    with open("config.json") as conf_file:
        conf = json.load(conf_file)["directories"]
    box.delete(0, END)
    [box.insert(END, i) for i in conf]

def addfold():
    global box
    fold = tkFileDialog.askdirectory(initialdir='.', title='Choose a directory')
    box.insert(END, fold)

def rmfold():
    global box
    box.delete(box.curselection()[0], box.curselection()[0])

def shrek():
    global box
    shrekt = json.dumps({"directories": box.get(0, END)})
    with open("config.json", "w") as conf_file:
        conf_file.write(shrekt)

global box
box = Listbox(root)
box.pack(fill=BOTH, expand=1, side=TOP)
fr = Frame(root)
fr.pack(side=BOTTOM)
Button(fr, text="Delete selected", command=rmfold).pack(side=LEFT, expand=1, fill=X)
Button(fr, text="Save", command=shrek).pack(side=RIGHT, expand=1, fill=X)
Button(fr, text="Add folder", command=addfold).pack(side=RIGHT, expand=1, fill=X)
load(box)
root.mainloop()
