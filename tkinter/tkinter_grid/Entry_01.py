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
Entry Widget:
  Methods
  - delete(first, last=None)
  - get()
  - icursor(index)
  - index (index)
  - insert (index, s)
  - select_adjust(index)
  - select_clear()
  - select_from(index)
  - select_present()
  - select_range(start, end)
  - select_to (index)
  - xview(index)
  - xview_Scroll(number, what)
#------------------------------------------------------------------------------
"""

from tkinter import *

def mHello():
  mtext = ment.get()
  mlabel2 = Label(mGui, text=mtext ).grid()
  return;


##-----------------------------------------------------------------------------
mGui = Tk()
mGui.title ("Entry widget")
mGui.geometry("450x450+500+300")

ment = StringVar()

# Label    
mlabel = Label(mGui, text="My Label")
mlabel.grid ()

# Button
mbutton = Button( mGui, text='OK', command=mHello, fg='red', bg='blue' )
mbutton.grid()

## Entry
mentry = Entry(mGui, bd=5, textvariable=ment )

s = mentry.get()
print( s )
mentry.grid()

#------------------------------------------------------------------------------
## --- Entry with Scrollbar ---
def __scrollHandler( *L ):
  op, howMany = L[0], L[1]
  
  if op == 'scroll':
    units = L[2]
    ety1.xview_scroll( howMany, units )
  elif op=='moveto':
    ety1.xview_moveto( howMany )
    
  return;

s1 = StringVar()
ety1 = Entry( mGui, bd=10, textvariable=s1 )
ety1.grid()
scb1 = Scrollbar( mGui, orient=HORIZONTAL, command=__scrollHandler )
scb1.grid( sticky=E+W )
#------------------------------------------------------------------------------


mGui.mainloop()

""""
import tkinter as tk

class Application(tk.Frame):
   def __init__(self, master=None):
      tk.Frame.__init__(self, master)
      self.grid()
      self.createWidgets()
      
   def createWidgets(self):
      self.hi_there = tk.Button(self)
      self.hi_there["text"] = "Hello World\n(click me)"
      self.hi_there["command"] = self.say_hi
      self.hi_there.grid()
      
      self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
      self.QUIT.grid()
      
   def say_hi(self):
      print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)

app.mainloop()
"""


##-----------------------------------------------------------------------------
"""
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

##-----------------------------------------------------------------------------
"""
Sources:
 - 
 
"""
