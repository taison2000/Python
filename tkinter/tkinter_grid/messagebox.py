#!/usr/bin/python

# Comment start with #
# No multiple line comment

   
import tkinter as tk
from tkinter import messagebox as msgBox  #import tkMessageBox
## tkMessageBox no longer available in Python 3. Replace with 'messagebox'

"""
#------------------------------------------------------------------------------
messagebox Widgets:
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

#------------------------------------------------------------------------------
"""

top = tk.Tk()

def helloCallBack():
  ret = msgBox.showinfo ("Title Python", "Message : Hello")
  # ret => 'ok'
  print( "You click : ", ret )
  return;

def InfoCallBack():
  ret = msgBox.showinfo ("Information", "This is info Only")
  # ret => 'ok'
  print( "You click : ", ret ) 
  return;
   
def ShowWaring():
  ret = msgBox.showwarning ("showwarning", "Show Warning")
  # ret => 'ok'
  print( "You click : ", ret )
  return;

def ShowError():
  ret = msgBox.showerror ("showerror", "Show Error")
  # ret => 'ok'
  print( "You click : ", ret )
  return;
  
def AskQuestion():
  ret = msgBox.askquestion ("askquestion", "Ask Question")
  # ret => 'yes' or 'no'
  print( "You click : ", ret )
  return;
  
def AskOkCancel():
  ret = msgBox.askokcancel ("askokcancel", "Ask OK/Cancel")
  # OK=>True, Calcel=>False
  print( "You click : ", ret )  
  return;
  
def AskYesNo():
  ret = msgBox.askyesno ("askyesno", "Ask Yes/No ")
  print( "You click : ", ret )
  # Yes=>True, No=>False
  return;
  
def AskRetryCancel():
  ret = msgBox.askretrycancel ("askretrycancel", "Ask Yes/No ")
  # Retry=>True, Cancel=>False
  print( "You click : ", ret )
  return;
  
colorBG = "#0000f0"   # notice color must be 6 hex digits (#123abc)
btnHello = tk.Button (top, text = "Hello", command = helloCallBack, fg="gray", highlightcolor="red")
#btnInfo = tk.Button (top, text = " Info ", command = InfoCallBack, fg="Green", bg="gray")
btnInfo = tk.Button (top, text = " Info ", command = InfoCallBack, fg="#ff0000", bg=colorBG, justify="right", width=20)

btnShowWaring = tk.Button( top, text="Show Warning", command=ShowWaring, width=15 )
btnShowError = tk.Button( top, text="Show Error", command=ShowError, width=15 )
btnAskQuestion = tk.Button( top, text="Ask Question", command=AskQuestion, width=15 )
btnAskOkCancel = tk.Button( top, text="Ask OK/Cancel", command=AskOkCancel, width=15 )
btnAskYesNo = tk.Button( top, text="Ask Yes/No ", command=AskYesNo, width=15 )
btnAskRetryCancel = tk.Button( top, text="Ask Retry/Cancel", command=AskRetryCancel, width=15 )

#btnHello.pack(side="left")
#btnInfo.pack()
#btnInfo.pack(fill=BOTH, expand=1)
#btnInfo.pack( expand=1 )
#btnInfo.pack()

btnHello.grid()
btnInfo.grid()
btnShowWaring.grid()
btnShowError.grid()
btnAskQuestion.grid()
btnAskOkCancel.grid()
btnAskYesNo.grid()
btnAskRetryCancel.grid()

top.mainloop() 


# NOTE:
# https://mail.python.org/pipermail//tkinter-discuss/2011-August/002916.html
#  - tkMessageBox has been renamed to messagebox in Python 3.x.
#  - Module is not available in tkinter
#  - code : from tkinter import messagebox

# http://www.tutorialspoint.com/python/tk_button.htm
# http://www.tutorialspoint.com/python/python_gui_programming.htm    # GUI Programming
#
# http://www.tutorialspoint.com/python/tk_colors.htm
#


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
