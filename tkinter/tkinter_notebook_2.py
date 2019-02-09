import tkinter
from tkinter import ttk
##-----------------------------------------------------------------------------

mainWindow = tkinter.Tk()
mainWindow.title("Notebook widget")
mainWindow.geometry('500x300')

mainFrame = tkinter.Frame(mainWindow, name = 'main-frame')
mainFrame.pack(fill = tkinter.BOTH) # fill both sides of the parent

nb = ttk.Notebook(mainFrame, name = 'nb')
nb.pack(fill = tkinter.BOTH, padx=2, pady=3) # fill "master" but pad sides

# add a tab
tab1Frame = tkinter.Frame(nb, name = 'serialcom') # why 'name' has to be all lower case?
nb.add(tab1Frame, text = 'Serial COM ')
tkinter.Label(tab1Frame, text = 'this is tab for COM setup').pack(side = tkinter.LEFT)

# add a tab
tab2Frame = tkinter.Frame(nb, name = 'tab2') # add fram under notebook
nb.add(tab2Frame, text = 'tab 2')
tkinter.Label(tab2Frame, text = 'this is tab 2').pack(side = tkinter.LEFT)

nb.select(tab2Frame) # <-- here's what you're looking for

mainWindow.mainloop()

##-----------------------------------------------------------------------------
# http://stackoverflow.com/questions/28088153/python-focus-on-ttk-notebook-tabs?rq=1


