#!/usr/bin/python
# Comment start with #



import sys
import tkinter as tk
#from tkinter import messagebox as msgBox  #import tkMessageBox

top = tk.Tk()

lbl1 = tk.Label(None, text='This is a label #1')
lbl2 = tk.Label(None, text=' label #2', bg="light green")
lbl3 = tk.Label(None, text=' Font=Harrington Size=16', bg="gray", height=5, width=25, \
         font=("Harrington", 16), fg="green", cursor='cross')


lbl1.pack()
lbl2.pack()
lbl3.pack()
              
lbl1.mainloop()


"""
#------------------------------------------------------------------------------
Label Widgets:

lb = tk.Label (parent, option, ...)

 Options
  - activebackground
  - activeforeground
  - anchor
  - bg / background
  - bitmap
  - bd / borderwidth
  - compound
  - cursor
  - disabledforground
  - font
  - fg / foreground
  - height
  - highlightbackground
  - highlightcolor
  - highlightthickness
  - image
  - justify
  - padx
  - pady
  - relief
  - state
  - takefocus
  - text
  - textvariable
  - underline
  - width
  - wraplength
#------------------------------------------------------------------------------
"""

# -----------------------------------------------------------------------------
# Resources
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# 
# https://docs.python.org/3.4/tutorial/modules.html

# http://www.tutorialspoint.com/python/tk_label.htm <-- Label
# http://www.tutorialspoint.com/python/tk_cursors.htm <-- cursor names
# http://effbot.org/tkinterbook/label.htm  <-- Label
#
