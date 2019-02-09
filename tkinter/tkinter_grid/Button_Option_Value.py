#!/usr/bin/python

# Comment start with #
# No multiple line comment

##-----------------------------------------------------------------------------
# Access options (Button=btnName)
#   btnName['state']=DISABLE/NORMAL
#   btnName['text']="Name of Button"



import tkinter as tk
from tkinter import messagebox as msgBox  #import tkMessageBox

top = tk.Tk()
top.title('Button widget')
top.geometry('400x200')

def helloCallBack():
  msgBox.showinfo ("Title Python", "Message : Hello")
  print ('state : ', btnHello['state'])
  print ('text :', btnHello['text'])
  return;

def InfoCallBack():
  #msgBox.showinfo ("Information", "This is info Only")
  print ('activebackground :', btnInfo['activebackground'])
  print ('activeforeground :', btnInfo['activeforeground'])
  print ('anchor :', btnInfo['anchor'])
  print ('bd :', btnInfo['bd'])
  print ('borderwidth :', btnInfo['borderwidth'])
  print ('bg/background :', btnInfo['background'])
  print ('bitmap :', btnInfo['bitmap'])
  print ('command :', btnInfo['command'])
  print ('cursor :', btnInfo['cursor'])
  print ('default :', btnInfo['default'])
  print ('disabledforeground :', btnInfo['disabledforeground'])
  print ('fg/foreground :', btnInfo['fg'])
  print ('font :', btnInfo['font'])
  print ('height :', btnInfo['height'])
  print ('highlightbackground :', btnInfo['highlightbackground'])
  print ('highlightcolor :', btnInfo['highlightcolor'])
  print ('highlightthickness :', btnInfo['highlightthickness'])
  print ('image :', btnInfo['image'])
  print ('justify :', btnInfo['justify'])
  print ('overrelief :', btnInfo['overrelief'])
  print ('padx :', btnInfo['padx'])
  print ('pady :', btnInfo['pady'])
  print ('relief :', btnInfo['relief'])
  print ('repeatdelay :', btnInfo['repeatdelay'])
  print ('repeatinterval :', btnInfo['repeatinterval'])
  print ('state : ', btnInfo['state'])
  print ('takefocus :', btnInfo['takefocus'])
  print ('text :', btnInfo['text']) 
  print ('textvariable :', btnInfo['textvariable'])
  print ('underline :', btnInfo['underline'])
  print ('width :', btnInfo['width'])
  print ('wraplength :', btnInfo['wraplength'])

  return;
  
colorBG = "#0000f0"   # notice color must be 6 hex digits (#123abc)
btnHello = tk.Button (top, text = "Hello", command = helloCallBack, fg="gray", highlightcolor="red")
btnInfo = tk.Button (top, text = " Info ", command = InfoCallBack, fg="#ff0000", bg=colorBG, justify="right", width=20)

btnHello.grid()
btnInfo.grid()


btn1 = tk.Button (top, text="New Button")
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
