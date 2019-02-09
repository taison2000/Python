#!/usr/bin/python

from tkinter import *
#from tkFileDialog import askopenfilename
##-----------------------------------------------------------------------------
def NewFile():
    print ("New File")

def OpenFile():
    name = askopenfilename()
    print (name)

def About():
    print ("This is a example of menu")

root = Tk()
menu = Menu(root)
root.config(menu=menu)

## ----- Get rid of menubar dash line -----
root.option_add( '*tearOff', False)

# File menu
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

# Help menu
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()
