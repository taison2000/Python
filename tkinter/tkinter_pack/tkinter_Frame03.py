#!/usr/bin/python
# Comment start with #
## double "pound" sign has different color


import sys
import tkinter as tk
from tkinter import messagebox as msgBox  #import tkMessageBox

top = tk.Tk()
top.title('App Title')


fraMiddle = tk.Frame(top, height=552, width=545, bd=1, relief='solid', bg='orange')
#fraMiddle.grid_propagate(0)
fraMiddle.pack(fill='x', padx=5, pady=5)
#fraMiddle.pack()

# Label
lbl1 = tk.Label(fraMiddle, text='This is a label #1')
lbl1.pack(fill='y', padx=100, pady=200)


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
lblFrm.pack(ipady=200, ipadx=30)

tk.Label(text="two").pack(ipadx=100, ipady=20)


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