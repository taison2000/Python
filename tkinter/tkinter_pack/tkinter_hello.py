#!/usr/bin/python
# Comment start with #


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

