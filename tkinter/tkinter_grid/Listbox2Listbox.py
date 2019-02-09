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
import tkinter.messagebox as msgBox

def dialog():
  msgBox.showinfo('Selection', 'Your Choice : ' +\
    lbxSrc.get(lbxSrc.curselection()))

def AddTest():
  #lbxDst.insert( 1, lbxSrc.get(lbxSrc.curselection()) )
  lbxDst.insert( lbxDst.size(), lbxSrc.get(lbxSrc.curselection()) )

def RemoveTest():
  lbxDst.delete( lbxDst.curselection() )

def RunTests():
  # Loop through the listbox and run each test
  for l in lbxDst.get(0, lbxDst.size()):
    print (l)

window = Tk()
window.title( 'ACC Tests' )
  
frame = Frame( window )

lbxSrc = Listbox( frame )
lbxSrc.insert(1, 'HTML5 in easy steps')
lbxSrc.insert(2, 'CSS3 in easy steps')
lbxSrc.insert(3, "JavaScript in easy steps")

lbxDst = Listbox( frame )

btnAdd = Button(frame, text='  Add => ', width=10, command=AddTest)
btnRem = Button(frame, text='<= Remove', width=10, command=RemoveTest)
btnRun = Button(frame, text='Run Test', width=15, height=3, relief=RAISED, command=RunTests)

frame.grid( row=0, column=0 )
#frame.grid(  )
lbxSrc.grid( row=0, column=0, rowspan=12 )
btnAdd.grid( row=2, column=1 )
btnRem.grid( row=4, column=1 )
lbxDst.grid( row=0, column=2, rowspan=12 )
btnRun.grid( row=9, column=0, columnspan=3 )

window.mainloop()


"""
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
      self.hi_there.grid(side="top")
      
      self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
      self.QUIT.grid(side="bottom")
      
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
