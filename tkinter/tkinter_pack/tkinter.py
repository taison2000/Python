#!/usr/bin/python
# Comment start with #



import sys
import tkinter as tk
from tkinter import messagebox as msgBox  #import tkMessageBox

top = tk.Tk()

CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()
# defined subclasses Variable : StringVar, IntVar, DoubleVar, and BooleanVar. 
#   To read the current value of such a variable, call the get() method on it, 
#   to change its value you call the set() method

chk1 = tk.Checkbutton (top, text="Music", variable=CheckVar1, \
               onvalue=1, offvalue=0, height=5, width=20)

chk2 = tk.Checkbutton (top, text="Video", variable=CheckVar2, \
               onvalue=1, offvalue=0, height=5, width=20)

chk1.pack()
chk2.pack()               

# Label
lbl1 = tk.Label(None, text='This is a label #1')
lbl2 = tk.Label(None, text=' Magneto Bold' , bg="gray", height=10, width=15, \
         font=("Magneto Bold", 36), fg="green", cursor=("Arrow"))

lbl1.pack()
lbl2.pack()
              


              
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


"""
#------------------------------------------------------------------------------
tkinter has following method and properties:
  - ACTIVE
  - ALL
  - ANCHOR
  - ARC
  - BASELINE
  - BEVEL
  - BOTH
  - BOTTOM
  - BROWSE
  - BUTT
  - BaseWidget
  - BitmapImage
  - BooleanVal
  - Button
  - CASCADE
  - CENTER
  - CHAR
  - CHECKBUTTON
  - CHORD
  - COMMAND
  - CURRENT
  - CallWrapper
  - Canvas
  - Checkbutton
  - DISABLED
  - DOTBOX
  - DoubleVar
  - E
  - END
  - EW
  - EXCEPTION
  - EXTENDED
  - Entry
  - Event
  - FALSE
  - FIRST
  - FLAT
  - Frame
  - GROOVE
  - Grid
  - HIDDEN
  - HORIZONTAL
  - INSERT
  - INSIDE
  - Image
  - IntVar
  - LAST
  - LEFT
  - Label
  - LabelFrame
  - Listbox
  - MITER
  - MOVETO
  - MULTIPLE
  - Menu
  - Menubutton
  - Message
  - Misc
  - N
  - NE
  - NO
  - NONE
  - NORMAL
  - NS
  - NSEW
  - NUMERIC
  - NW
  - NoDefaultRoot
  - OFF
  - ON
  - OUTSIDE
  - OptionMenu
  - PAGES
  - PIESLICE
  - PROJECTING
  - Pack
  - PanedWindow
  - PhotoImage
  - Place
  - RADIOBUTTON
  - RAISED
  - READABLE
  - RIDGE
  - RIGHT
  - ROUND
  - Radiobutton
  - S
  - SCROLL
  - SE
  - SEL
  - SEL_FIRST
  - SEL_LAST
  - SEPARATOR
  - SINGLE
  - SOLID
  - SUNKEN
  - SW
  - Scale
  - Scrollbar
  - Spinbox
  - StringVar
  - Studbutton
  - TOP
  - TRUE
  - Tcl
  - TclError
  - TclVersion
  - Text
  - Tk
  - TkVersion
  - Toplevel
  - Tributton
  - UNDERLINE
  - UNITS
  - VERTICAL
  - Variable
  - W
  - WORD
  - WRITABLE
  - Widget
  - Wm
  - X
  - XView
  - Y
  - Yes
  - YView
  - __builtins__
  - __cached__
  - __doc__
  - __file__
  - __loader__
  - __name__
  - __package__
  - __path__
  - __spec__
  - _cnfmerge
  - _default_root
  - _exit
  - _fix
  - _flatten
  - _join
  - _magic_re
  - _setit
  - _space_re
  - _splitdict
  - _stringify
  - _support_default_root
  - _test
  - _tkerror
  - _tkinter
  - _varnum
  - colorchoose
  - commondialog
  - constants
  - dialog
  - filedialog
  - font
  - getboolean
  - getdouble
  - getint
  - image_names
  - image_types
  - mainloop
  - messagebox
  - re
  - simpledialog
  - sys
  - wantobjects
#------------------------------------------------------------------------------
