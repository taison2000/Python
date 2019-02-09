#!/usr/bin/python
# Comment start with #

##-----------------------------------------------------------------------------
# get help from IDLE
#   1. import tkinter
#   2. help(tkinter.Listbox)


#------------------------------------------------------------------------------
# E1 = Entry (master, option, ...)
#   Parameters:
#     * master : represents the parent window
#     * options: 
#
#   --- Options ---
#     - bg : background color
#     - bd : border size
#     - command : A procedure to be called when 
#     - cursor
#     - font
#     - exportselection
#     - fg
#     - highlightcolor
#     - justify
#     - relief
#     - selectbackground
#     - selectforeground
#     - show
#     - state
#     - textvariable
#------------------------------------------------------------------------------


"""
#------------------------------------------------------------------------------
Listbox Widgets:
  Methods
  - activate( index )
  - curselection()
  - delete( startIndex [, endIndex=None] )
  - get( startIndex [, endIndex=None] )
  - index ( i )
  - insert ( index, *element )
  - nearest( y )
  - see( index )
  - size()
  - xview()
  - xview_moveto( fraction )
  - xview_Scroll( number, what )
  - yview()
  - yview_moveto( fraction )
  - yview_Scroll( number, what )
#------------------------------------------------------------------------------
"""


from tkinter import *

def entryChanges():
  print ("Entry has been changed")
  
top = Tk()

top.title ("Listbox widget")


#lb1 = Listbox(top, listvariable=("opt1", 'opt2', 'opt3'), command=entryChanges())
lb1 = Listbox(top, listvariable=("opt1", 'opt2', 'opt3'))
lb1.insert(1, "lb1 opt1")
lb1.insert(2, "lb1 opt2")
lb1.insert(3, "lb1 opt3")
lb1.pack (side = LEFT)

#E1 = Entry(top, bd=5)
#E1.pack(side = RIGHT)

top.mainloop()

""""
import tkinter as tk

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
app = Application(master=root)

app.mainloop()
"""

"""
#------------------------------------------------------------------------------
tkinter Widgets:
  - Button
  - Canvas
  - Checkbutton
  - Entry
  - Frame
  - Label
  - Listbox
  - Menubutton
  - Menu
  - Message
  - Radiobutton
  - Scale
  - Scrollbar
  - Text
  - Toplevel
  - Spinbox
  - PaneWindow
  - LabelFrame
  - tkMessageBox
#------------------------------------------------------------------------------
"""
