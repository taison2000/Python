#!/usr/bin/python
# Comment start with #




import time
from tkinter import *
import tkinter.messagebox as msgBox



##-----------------------------------------------------------------------------

import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):

   ReliefState = 0
   
   def __init__(self, master=None):
      tk.Frame.__init__(self, master)
      self.grid()
      self.createWidgets()
      
   def createWidgets(self):
      # FLAT
      self.btnFlat = tk.Button(self)
      self.btnFlat["text"] = "FLAT"
      self.btnFlat["relief"] = tk.FLAT
      self.btnFlat['width'] = 20
      self.btnFlat['height'] = 5
      self.btnFlat.grid(row=0, column=0)
      # RIDGE
      self.btnRidge = tk.Button(self)
      self.btnRidge["text"] = "RIDGE"
      self.btnRidge["relief"] = tk.RIDGE
      self.btnRidge['width'] = 20
      self.btnRidge['height'] = 5
      self.btnRidge.grid(row=1, column=0)
      # RAISED
      self.btnRaised = tk.Button(self)
      self.btnRaised["text"] = "RAISED"
      self.btnRaised["relief"] = tk.RAISED
      self.btnRaised['width'] = 20
      self.btnRaised['height'] = 5
      self.btnRaised.grid(row=2, column=0)
      # SUNKEN
      self.btnSunken = tk.Button(self)
      self.btnSunken["text"] = "SUNKEN"
      self.btnSunken["relief"] = tk.SUNKEN
      self.btnSunken['width'] = 20
      self.btnSunken['height'] = 5
      self.btnSunken.grid(row=3, column=0)
      # GROOVE
      self.btnGroove = tk.Button(self)
      self.btnGroove["text"] = "GROOVE"
      self.btnGroove["relief"] = tk.GROOVE
      self.btnGroove['width'] = 20
      self.btnGroove['height'] = 5
      self.btnGroove.grid(row=4, column=0)

      self.btnRelief = tk.Button(self)
      self.btnRelief["command"] = self.ReliefUpdate
      self.btnRelief['text'] = "Click Me"
      self.btnRelief['width'] = 20
      self.btnRelief['height'] = 5
      self.btnRelief.grid(row=2, column=1)
      
      self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy, padx=20, pady=20)
      self.QUIT['width'] = 40
      self.QUIT['height'] = 5
      #self.QUIT['relief'] = "sunken"  # <-- Work
      #self.QUIT['relief'] = tk.SUNKEN  # <-- Work tkinter.(SUNKEN/FLAT/RAISED/GROOVE/RIDGE)
      #self.QUIT['relief'] = tk.RAISED
      #self.QUIT['relief'] = tk.RIDGE
      
      #self.QUIT = ttk.Button(self, text="QUIT", command=root.destroy)
      
      self.QUIT.grid(row=0, column=1)
      
   def ReliefUpdate(self):
      if (self.ReliefState%5==0):
         self.btnRelief['relief'] = 'flat'
         self.btnRelief['text'] = 'FLAT'
      elif (self.ReliefState%5==1):
         self.btnRelief['relief'] = 'raised'
         self.btnRelief['text'] = 'RAISED'
      elif (self.ReliefState%5==2):
         self.btnRelief['relief'] = 'sunken'
         self.btnRelief['text'] = 'SUNKEN'
      elif (self.ReliefState%5==3):
         self.btnRelief['relief'] = 'groove'
         self.btnRelief['text'] = 'GROOVE'
      else:
         self.btnRelief['relief'] = 'ridge'
         self.btnRelief['text'] = 'RIDGE'

      self.ReliefState = (self.ReliefState+1)%5
      return
   
root = tk.Tk()
app = Application(master=root)
root.title("Relief")
#app.title("Relief")  #<- Not this

app.mainloop()


