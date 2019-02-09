#!/usr/bin/python

from tkinter import *
#from tkFileDialog import askopenfilename

def NewFile():
  print ("New File")
  
def OpenFile():
  name = askopenfilename()
  print (name)

def accMenu():
  pass

def SetGlobal():
  pass

def GetGlobal():
  pass

def HeartBeat():
  pass
  
def Undo():
  pass
  
def About():
  print ("This is a example of menu")
  
root = Tk()
root.title("ACC of Auto")
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
#filemenu.add_command(label="Exit", command=root.quit())
filemenu.add_command(label="Exit", command=root.destroy)

editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo...", command=Undo)

## -- ACC cmd menu --
accMenu = Menu(menu)
menu.add_cascade(label="ACC", menu=accMenu)
accMenu.add_command(label="Set Global (0x01)", command = SetGlobal)
accMenu.add_command(label="Get Global (0x02)", command = GetGlobal)
accMenu.add_command(label="HeartBeat (0x05)", command = HeartBeat)


helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)


mainloop()
