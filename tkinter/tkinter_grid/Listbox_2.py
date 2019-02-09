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
  - bbox( index )
  - curselection
  - delete( startIndex [, endIndex=None] )
  - get()
  - 
  - 
  - insert (index, str)
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
import tkinter.messagebox as msgBox

window = Tk()
window.title( 'Listbox widget' )
  
frame = Frame( window )

listbox = Listbox( frame )
listbox.insert(1, 'HTML5 in easy steps')
listbox.insert(2, 'CSS3 in easy steps')
listbox.insert(3, "JavaScript in easy steps")


def dialog():
  msgBox.showinfo('Selection', 'Your Choice : ' +\
  listbox.get(listbox.curselection()))

btn = Button(frame, text='Choose', command=dialog)

btn.grid( row=1, column=20 )
listbox.grid( row=6, column=2 )
frame.grid( row=0, column=0 )
#frame.grid(  )

window.mainloop()


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
      self.hi_there.grid(side="top")
      
      self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
      self.QUIT.grid(side="bottom")
      
   def say_hi(self):
      print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)

app.mainloop()
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
