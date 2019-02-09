#!/usr/bin/python

# Comment start with #
# No multiple line comment

##-----------------------------------------------------------------------------
# Access options (Button=btnName)
#   btnName['state']=DISABLE/NORMAL
#   btnName['text']="Name of Button"



import tkinter as tk
from tkinter import messagebox as msgBox  #import tkMessageBox

def helloCallBack():
  msgBox.showinfo ("Title Python", "Message : Hello")
  print ('state : ', btnHello['state'])
  print ('text :', btnHello['text'])
  return;

def InfoCallBack():
  msgBox.showinfo ("Information", "This is info Only")
  return;

top = tk.Tk()
top.title('Button widget')
top.geometry('400x200')

colorBG = "#0000f0"   # notice color must be 6 hex digits (#123abc)
btnHello = tk.Button (top, text = "Hello", command = helloCallBack, fg="gray", highlightcolor="red")
#btnInfo = tk.Button (top, text = " Info ", command = InfoCallBack, fg="Green", bg="gray")
btnInfo = tk.Button (top, text = " Info ", command = InfoCallBack, fg="#ff0000", bg=colorBG, justify="right", width=20)

btnHello.grid()
btnInfo.grid()

imagePhp = tk.PhotoImage(file='php.gif')
imageStop = tk.PhotoImage(file='stop.gif')
#btn1 = tk.Button (top, text="New Button")
#btn1 = tk.Button (top, image=imageStop)
btn1 = tk.Button (top, image=imagePhp)
btn1 = tk.Button (top)
btn1['image']=imageStop
#btn1['image']=imagePhp
btn1['image']=''
btn1['text']="Image"
btn1.grid()

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
