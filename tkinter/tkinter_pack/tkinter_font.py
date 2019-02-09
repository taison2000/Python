#!/usr/bin/python
# Comment start with #



import sys
import tkinter as tk
#from tkinter import messagebox as msgBox  
## tkMessageBox (v2.x) ==> messagebox (v3.x)

top = tk.Tk()

lbl1 = tk.Label(None, text='This is a label #1')
lbl2 = tk.Label(None, text=' label #2', bg="light green")
lbl3 = tk.Label(None, text='ABCDEFHJIJKLMNOPQRSTUVWXYZ', bg="gray", height=3, width=30, \
         font=("Harlow", 35), fg="green", cursor='cross', underline=(15))


lbl1.pack()
lbl2.pack()
lbl3.pack()
              
top.mainloop()



# -----------------------------------------------------------------------------
# Resources
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# 
# https://docs.python.org/3.4/tutorial/modules.html

# http://www.tutorialspoint.com/python/tk_label.htm <-- Label
# http://www.tutorialspoint.com/python/tk_cursors.htm <-- cursor names
# http://effbot.org/tkinterbook/label.htm  <-- Label
#
# Windows - Font
#  - "Control Panel" -> "Appearance and Personalization" -> "Fonts"
#  - "Control Panel" -> "Fonts"
#
#     * Arial
#     * Forte
#     * Forte
#     * Gungsuh
#     * Harrington
#
