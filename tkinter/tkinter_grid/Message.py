#!/usr/bin/python
# Comment start with #


"""
#------------------------------------------------------------------------------
tkinter Widgets:
  - BitmapImage
  - Button
  - Canvas
  - Checkbutton
  - Entry
  - Frame
  - Label
  - LabelFrame
  - Listbox
  - Menu
  - Menubutton
  - Message
  - OptionMenu
  - PanedWindow
  - PhotoImage
  - Radiobutton
  - Scale
  - Scrollbar
  - Text
  - Toplevel
  - scrolledtext  <- ?
  - Spinbox
  - tkMessageBox <- not in 3.x ?
#------------------------------------------------------------------------------
"""

##-----------------------------------------------------------------------------
# Note:
#  <Message> widget is a variant of the <Label>, designed to display multiline
#  message. The message widget can wrap text, and adjust its width to maintain
#  a given aspect ratio.
#

"""
#------------------------------------------------------------------------------
messagebox Widgets:
Messag Widgets:
  Parameters
   - bg
   - bd
   - cursor
   - exportselection
   - font
   - fg
   - height
   - highlightbackground
   - highlightcolor
   - highligtthickness
   - insertbackground
   - insertborderwidth
   - insertofftime
   - insertontime
   - insertwidth
   - padx
   - pady
   - relief
   - selectbackgroud
   - selectborderwidth
   - spacing1 
   - spacing2 
   - spacing3 
   - state
   - tabs
   - width
   - wrap
   - xscrollcommand
   - yscrollcommand

   
  
  Methods
   - showinfo()
   - showwaring()
   - showerror()
   - askquestion()
   - askokcance()
   - askyesno()
   - askretrycancel()
   - 
#------------------------------------------------------------------------------
"""
  

import tkinter as tk
from tkinter import *

# -----------------------------------------------------------------------------
root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.geometry("500x300-0+0")

var = StringVar()
label = Message( root, textvariable=var, relief=RAISED )
label['bg']='red' 
label['bg']='green'
#label = Message( root, textvariable=var, relief='raised' )

var.set("Hey! How are you doing?")
label.grid(sticky=W+E+N+S)
#label.grid(sticky=E+W)
#label.grid(sticky=(W+N+E+S))


root.title("Widget: Message")
root.mainloop()

"""
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
"""




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


##-----------------------------------------------------------------------------
## tkinter Widgets:
"""
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
  - PaneWindow
  - Radiobutton
  - Scale
  - Scrollbar
  - Spinbox
  - Text
  - Toplevel
#------------------------------------------------------------------------------
"""
