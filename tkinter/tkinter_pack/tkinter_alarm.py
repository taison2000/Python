#!/usr/bin/python
# Comment start with #


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

# # String index
# text="String Index"
# # text[0]==S text[1]==t text[2]==r text[3]==i text[4]==n
# # text[-1]==x text[-2]==e text[-3]==d text[-4]==n text[-5]==I
# print(text)
# print("Negative index")
# Length=len(text)
# print(Length)
# for i in range(Length):
   # print(text[-i-1], -i-1)
   

import tkinter as tk

class Alarm(tk.Frame):
  def closeApp(self):
    self.stopper.destry
    #tk.Frame.destry
    
  #def __init__(self, master=None):
  def __init__(self, master=tk.Frame):
      tk.Frame.__init__(self)
      self.msecs = 1000
      self.pack()
      #self.stopper = tk.Button(self, text='Stop the beeps!', command = self.quit)
      self.stopper = tk.Button(self, text='Stop the beeps!', command = self.destroy)
      #self.stopper = tk.Button(self, text='Stop the beeps!', command = Alarm.closeApp)
      
      self.stopper.pack()
      self.stopper.config(bg='navy', fg='white', bd=8)
      #self.stopper = stopper
      self.repeater()
      
      
  def repeater(self):
    self.bell()
    self.after(self.msecs, self.repeater)
    

# root = tk.Tk()

if __name__ == '__main__':
  Alarm().master.title('Alarm Demo')
  Alarm().mainloop()
  tk.Frame.destroy
  

