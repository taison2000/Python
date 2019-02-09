#!/usr/bin/python

#from tkinter import *
import tkinter as tk
from tkinter import ttk
#from myWidgets import Widget1, Widget2, Widget3

"""
def enableTabs(notebook):
  tabs = notebook.tabs()
  for i, item in enumerates(tabs):
    item['state'] = 'enabled' # This doesn't work
    item.configure(state='enabled') # Doesn't work either
"""

def enableTabs(notebook):
  tabs = notebook.tabs()
  for i, item in enumerates(tabs):
    notebook.tab(item, state = 'normal') # This doesn't work
    

if __name__=="__main__":
  root = tk.Tk()
  root.geometry("450x250")
  root.title("Notebook example")
  
  notebook = ttk.Notebook(root)
  notebook.pack(fill=tk.BOTH)
  """
  #w1 = Widget1()
  #w2 = Widget2()
  #w3 = Widget3()
  
  notebook.add(w1, text='tab1', state='disabled')
  notebook.add(w2, text='tab2', state='disabled')
  notebook.add(w3, text='tab3', state='disabled')
  """
  
  # Add frames inside notebook
  frame1 = ttk.Frame(notebook, name='ta1')
  frame2 = ttk.Frame(notebook, name='ta2')
  frame3 = ttk.Frame(notebook, name='ta3')
  notebook.add(frame1, text="Tab 1")
  notebook.add(frame2, text="Tab 2")
  notebook.add(frame3, text="Tab 3")
  
  
  #ttk.Label(frame1, text='tab1', state='disabled')
  #ttk.Label(frame1, text='tab1', state='normal')
  ttk.Label(frame1, text='Labe in tab1').pack(side=tk.LEFT)
  tk.Label(frame2, text='Label for tab2', state='disabled').pack()
  tk.Label(frame3, text='Label for tab #3', state='disabled').pack(side = tk.RIGHT)
  """
  notebook.add(tk.Label, text='tab1', state='disabled')
  notebook.add(tk.Label, text='tab2', state='disabled')
  notebook.add(tk.Label, text='tab3', state='disabled')
  """
  
  #enableTabs(notebook)  # Should be called in certain events in real append
  root.mainloop()
  
