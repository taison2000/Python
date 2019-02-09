#!/usr/bin/python
# Comment start with #
## double "pound" sign has different color


import sys
import tkinter as tk
from tkinter import messagebox as msgBox  #import tkMessageBox

top = tk.Tk()


top.title('App Title')


tk.Label(text="Label One").pack()

##-----------------------------------------------------------------------------
''' --- separator --- '''
separator = tk.Frame(height=2, bd=1, relief='raised')
separator.pack(fill='x', padx=5, pady=5)

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