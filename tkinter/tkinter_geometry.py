#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Python GUI using grid method
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import time
#import tkinter as tk  # import module tkinter, reference it as tk
from tkinter import *


##-----------------------------------------------------------------------------
root = Tk()
#root.geometry('500x300')
root.geometry('500x300+0+0')  # Top Left
#root.geometry('500x300+0-0')  # Buttom Left
#root.geometry('500x300-0+0')  # Top Right
#root.geometry('500x300-0-0')  # Buttom Right


root.title('tkinter geometry')
root.mainloop()

##-----------------------------------------------------------------------------
"""
Source:
http://stackoverflow.com/questions/8683217/when-do-i-need-to-call-mainloop-in-a-tkinter-application
"""
