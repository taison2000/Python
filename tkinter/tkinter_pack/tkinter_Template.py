#!/usr/bin/python
# Comment start with #

##-----------------------------------------------------------------------------
## tkinter Widgets:
"""
  - BitmapImage
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
  - messagebox (v2.x -> tkMessageBox)
  - OptionMenu
  - PanedWindow
  - PhotoImage
  - Radiobutton
  - Scale
  - Scrollbar
  - Spinbox
  - Text
  - Toplevel
#------------------------------------------------------------------------------
"""


#------------------------------------------------------------------------------

# # String index
# text="String Index"
# # text[0]==S text[1]==t text[2]==r text[3]==i text[4]==n
# # text[-1]==x text[-2]==e text[-3]==d text[-4]==n text[-5]==I
# print(text)
# print("Negative index")
# Length=len(text)
# print(Length)
# for i in range(Length):
   # print(text[-i-1], -i-1)
   

import tkinter as tk

# -----------------------------------------------------------------------------
class Application(tk.Frame):
   def __init__(self, master=None):
      tk.Frame.__init__(self, master)
      self.pack()
      self.createWidgets()
      
   def createWidgets(self):
      self.hi_there = tk.Button(self)
      self.hi_there["text"] = "Hello World\n(click me)"
      self.hi_there["command"] = self.say_hi
      self.hi_there.pack(side="top")
      
      self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
      self.QUIT.pack(side="bottom")
      
   def say_hi(self):
      print("hi there, everyone!")


root = tk.Tk()

#(tk.Tk()).title("App Title again")
root.title("App Title")

app = Application(master=root)

app.mainloop()

## ----------------------------------------------------------------------------
# Resources
#
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
"""
