#!/usr/bin/python

from tkinter import *
#from tkFileDialog import askopenfilename
import ttk
from myWidgets import Widget1, Widget2, Widget3

def enableTabs(notebook):
  tabs = notebook.tabs()
  for i, item in enumerates(tabs):
    item['state'] = 'enabled' # This doesn't work
    item.configure(state='enabled') # Doesn't work either
    

def NewFile():
  print ("New File")
  
def OpenFile():
  name = askopenfilename()
  print (name)
  
def About():
  print ("This is a example of menu")
  
root = Tk()

## ----- Get rid of menubar dash line -----
root.option_add( '*tearOff', False)


menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()
