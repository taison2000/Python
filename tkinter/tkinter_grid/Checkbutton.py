#!/usr/bin/python
# Comment start with #

##-----------------------------------------------------------------------------
## Options
"""
# chkBtn = Checkbutton (master, option, ...)
# chkBtn = Checkbutton (parent, option, ...)
#   Parameters:
#     * master : represents the parent window
#     * options: 
#
#   --- Options ---
#     - activebackground
#     - activeforeground
#     - anchor
#     - bg/background   : background color
#     - bitmap
#     - bd/borderwidth  : border size
#     - command         : A procedure to be called when 
#     - compound
#     - cursor
#     - disabledforeground
#     - font
#     - fg/foreground
#     - height
#     - highlightbackground
#     - highlightcolor
#     - highlightthickness
#     - image
#     - indicatoron
#     - justify
#     - offrelief
#     - offvalue
#     - onvalue
#     - overrelief
#     - padx
#     - pady
#     - relief
#     - selectcolor
#     - selectimage
#     - state
#     - takefocus
#     - text
#     - textvariable
#     - underline
#     - variable
#     - width
#     - araplength
#------------------------------------------------------------------------------
"""

##-----------------------------------------------------------------------------
## Methods
"""
Checkbutton Widgets:
  Methods
  - deselect()
  - flash()
  - invoke()
  - select()
  - toggle()
#------------------------------------------------------------------------------
"""

import tkinter as tkWin
from tkinter import messagebox as msgBox  # "messagebox" replace "tkMessageBox" in v3.x

top = tkWin.Tk()

CheckVar1 = tkWin.IntVar()
CheckVar2 = tkWin.IntVar()
# defined subclasses Variable : StringVar, IntVar, DoubleVar, and BooleanVar. 
#   To read the current value of such a variable, call the get() method on it, 
#   to change its value you call the set() method

chk1 = tkWin.Checkbutton (top, text="Music", variable=CheckVar1, \
               onvalue=1, offvalue=0, height=5, width=20)

chk2 = tkWin.Checkbutton (top, text="Video", variable=CheckVar2, \
               onvalue=1, offvalue=0, height=5, width=20)
                              
#chk1.pack()
#chk2.pack()
chk1.grid()
chk2.grid()
               
top.mainloop()


"""
#------------------------------------------------------------------------------
tkinter Widgets:
  - Button
  - Canvas
  - Checkbutton
  - Entry
  - Frame
  - Label
  - LabelFrame
  - Listbox
  - Menubutton
  - Menu
  - Message
  - OptionMenu
  - PaneWindow
  - Radiobutton
  - Scale
  - Scrollbar
  - Spinbox
  - Text
  - Toplevel
  - messagebox  (v2.x : tkMessageBox)
#------------------------------------------------------------------------------
"""


# -----------------------------------------------------------------------------
# Resources
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# 
## double
'''
Hello world
'''

"""
Hello world
"""
