#!/usr/bin/python
# Comment start with #



import tkinter as tkWin
from tkinter import messagebox as msgBox  #import tkMessageBox

top = tkWin.Tk()
# Code to add widgets will go here ...

CheckVar1 = tkWin.IntVar()
CheckVar2 = tkWin.IntVar()
# defined subclasses Variable : StringVar, IntVar, DoubleVar, and BooleanVar. 
#   To read the current value of such a variable, call the get() method on it, 
#   to change its value you call the set() method

chk1 = tkWin.Checkbutton (top, text="Music", variable=CheckVar1, \
               onvalue=1, offvalue=0, height=5, width=20)

chk2 = tkWin.Checkbutton (top, text="Video", variable=CheckVar2, \
               onvalue=1, offvalue=0, height=5, width=20)
                              
chk1.pack()
chk2.pack()               
               
top.mainloop()



# -----------------------------------------------------------------------------
# Resources
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# 
