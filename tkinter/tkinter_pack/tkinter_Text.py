#!/usr/bin/python
# Comment start with #


"""
#------------------------------------------------------------------------------
Text Widgets:
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
   - delete( startIndex [, endIndex] )
   - get( startIndex [, endIndex] )
   - index( index )
   - insert( index [, string] )
   - see( index )
   Bookmark
   - index( mark )
   - mark_gravity( mark [, gravity] )
   - mark_names()
   - mark_set( mark, index )
   - mark_unset( mark, index )
   Tab (Tag?)
   - tag_add( tagName, startIndex [, endIndex] )
   - tag_config ( ... )
   - tag_delete( tagName )
   - tag_remove( tagName [, startIndex [, endIndex]] )
#------------------------------------------------------------------------------
"""

'''
NOTE:
 - Text (multiple lines); Entry (One line)
 - no ttk.Text ??
'''

## ----------------------------------------------------------------------------
# Text:
#  - 
#  - 
#


import tkinter as tk
from tkinter import *
from tkinter import ttk

# -----------------------------------------------------------------------------
'''-------------------------------------------------------------------------'''
def onclick():
  pass
  

root = Tk()

text = ttk.Text(root)
text.insert( INSERT, "First ....." )
text.insert( END, "Bye Bye .....\n" )
text.insert( END, "This will be 2nd line .....\n" )
text.insert( END, "Line 3 : Set tag from 3.8 to 3.14, background color to RED foreground color not change\n")
text.insert( END, "This is the Fourth line\n")
text.insert( END, "This is the Fifth line\n")
text.pack()

text.tag_add( "here", "1.0", "1.4" )  # tagname=="here", startindex=1.0, [endindex]=1.4
text.tag_add( "start", "1.8", "1.13" )  # 1.8==(line-1, index=8)
text.tag_config( "here", background="yellow", foreground="blue" )
text.tag_config( "start", background="black", foreground="green" )

text.tag_add( "line3", "3.8", "3.14")
text.tag_config( "line3", background='red')

# tag_delete(tagname)
#text.tag_delete("start")

# tag_remove( tagname [, startindex [, endindex]] )
text.tag_remove( "start", '1.11' )

text.tag_add('2nd_line', '2.8', '2.15')
text.tag_config('2nd_line', background='black', foreground='red' )

text.tag_add('crossLine_1_2', '1.15', '2.3')
text.tag_config('crossLine_1_2', background='cyan', foreground='brown' )

root.title( "Widget: Text" )

root.mainloop()


## ----------------------------------------------------------------------------
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
