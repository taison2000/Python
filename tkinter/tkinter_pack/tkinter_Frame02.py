#!/usr/bin/python
# Comment start with #
## double "pound" sign has different color


import sys
import tkinter as tk
from tkinter import messagebox as msgBox  #import tkMessageBox

top = tk.Tk()

top.title('App Title')

CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()
# defined subclasses Variable : StringVar, IntVar, DoubleVar, and BooleanVar. 
#   To read the current value of such a variable, call the get() method on it, 
#   to change its value you call the set() method

chk1 = tk.Checkbutton (top, text="Music", variable=CheckVar1, \
               onvalue=1, offvalue=0, height=2, width=20)

chk2 = tk.Checkbutton (top, text="Video", variable=CheckVar2, \
               onvalue=1, offvalue=0, height=2, width=20)

chk1.pack()
chk2.pack()

""""
lbl1 = tk.Label(None, text='This is a label #1')
lbl2 = tk.Label(None, text=' Magneto Bold' , bg="gray", height=5, width=36, \
         font=("Magneto Bold", 16), fg="green", cursor=("Arrow"))
"""

fraMiddle = tk.Frame(height=152, width=15, bd=1, relief='solid', bg='orange')
#fraMiddle.grid_propagate(0)
fraMiddle.pack(fill='x', padx=5, pady=5)
#fraMiddle.pack()
# Label
lbl1 = tk.Label(fraMiddle, text='This is a label #1')
lbl2 = tk.Label(None, text=' Magneto Bold', bg='blue', height=5, width=36, \
         font=("Magneto Bold", 16), fg="green", cursor=("Arrow"))

lbl1.pack()
lbl2.pack()

# -----------------------------------------------------------------------------
# Frame
#separator = tk.Frame(height=2, bd=1, relief='raised')
# separator = tk.Frame(height=2, bd=1, relief="sunken")
# separator = tk.Frame(height=2, bd=1, relief="flat")
#separator = tk.Frame(height=2, bd=1, relief='groove')
#separator = tk.Frame(height=2, bd=1, relief="ridge")
separator = tk.Frame(height=152, width=15, bd=1, relief="sunken", bg='red')
separator.grid_propagate(0) # force widget to be fixed size
separator.pack(fill='x', padx=5, pady=5)

lblFrm = tk.Label(separator, text='Frame as separator')
#lblFrm = tk.Label(None, text='Frame as separator')
lblFrm.grid_propagate(0)
lblFrm.pack()

tk.Label(text="two").pack()


top.mainloop()



# -----------------------------------------------------------------------------
# Resources
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# 
# https://docs.python.org/3.4/tutorial/modules.html
#

# http://www.tutorialspoint.com/python/tk_cursors.htm <-- cursor names
#
#

##-----------------------------------------------------------------------------
# Notes:
#  1. A frame is basically just a container for other widgets.
#