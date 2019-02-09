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
Entry Widgets:
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
import tkinter.messagebox as box

window = Tk()
window.title( 'Listbox widget' )
  
frame = Frame( window )

listbox = Listbox( frame )
listbox.insert(1, 'HTML5 in easy steps')
listbox.insert(2, 'CSS3 in easy steps')
listbox.insert(3, "JavaScript in easy steps")


def dialog():
  box.showinfo('Selection', 'Your Choice : ' +\
  listbox.get(listbox.curselection()))
# listbox.curselection() - index of the selected element
# listbox.get(startIndex, endIndex=None) - Text of the lines

btn = Button(frame, text='Choose', command=dialog)

btn.pack( side=RIGHT, padx=5 )
listbox.pack( side = LEFT )
frame.pack( padx=30, pady=30 )

window.mainloop()


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
