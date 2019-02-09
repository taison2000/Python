#!/usr/bin/python

from tkinter import *
##-----------------------------------------------------------------------------
root = Tk()
root.title("config")

rb = Radiobutton(root)
rb.grid()

configOptions = rb.config()
for key in configOptions:
  print("%-20s"%key, configOptions[key])
print()

rb.config(bg="green")
val = rb['bg']
print (val)

print('disabledforeground -> ', rb['disabledforeground'])

mainloop()

##-----------------------------------------------------------------------------
"""
Source:
 - http://stackoverflow.com/questions/8707039/difference-between-pack-and-configure-for-widgets-in-tkinter

"""
