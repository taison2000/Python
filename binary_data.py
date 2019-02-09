#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  Python
  ~~~~~~~~~~~

"""

import os
import time

byteNothing = b''   # not 'None', just b''

def binaryDataCompare():
    data1 = b'\xFF\xFF\xFF\x3C\xC3\x88\x00\xA9\x01\x00\x01\x00\x02\xF7\xB2'
    # type(data1)    #<class 'bytes'>
     
    data2 = [0xFF]
    data2.append(0xFF)
    data2.append(0xFF)
    data2.append(0x3C)
    data2.append(0xC3)
    data2.append(0x88)
    data2.append(0x00)
    data2.append(0xA9)
    data2.append(0x01)
    data2.append(0x00)
    data2.append(0x01)
    data2.append(0x00)
    data2.append(0x02)
    data2.append(0xF7)
    data2.append(0xB2)
    # data2 == [255, 255, 255, 60, 195, 136, 0, 169, 1, 0, 1, 0, 2, 247, 178]
    
    dataLen = len(data2)    # 15
    print ("Data Length : %02d" % dataLen)
    #for i in range (0, dataLen):
        #print ("data[%d] : 0x%02X" % (i, data2[i]))

    """
    data2 = [b'\xFF']
    data2.append(b'\xFF')
    data2.append(b'\xFF')
    data2.append(b'\x3C')
    data2.append(b'\xC3')
    data2.append(b'\x88')
    data2.append(b'\x00')
    data2.append(b'\xA9')
    data2.append(b'\x01')
    data2.append(b'\x00')
    data2.append(b'\x01')
    data2.append(b'\x00')
    data2.append(b'\x02')
    data2.append(b'\xF7')
    data2.append(b'\xB2')


    data2[0] = [0xFF]
    data2[1] = 0xFF
    data2[2] = 0xFF
    data2[3] = 0x3C
    data2[4] = 0xC3
    data2[5] = 0x88
    data2[6] = 0x00
    data2[7] = 0xA9
    data2[8] = 0x01
    data2[9] = 0x00
    data2[10] = 0x01
    data2[11] = 0x00
    data2[12] = 0x02
    data2[13] = 0xF7
    data2[14] = 0xB2
    """
    print(data1)
    print(data2)
    
    if data1 == data2:  # False, not equal. data1 is bytes type, data2 is a list
        print ("data1 and data2 are equal")
    else:
        print ("data1 and data2 are NOT equal")

def byteObjectManipulation():
    data = b'\xFF\xFF\xFF\x3C\xC3\x88\x00\xA9\x01\x00\x01\x00\x02\xF7\xB2'
    dataLen = len(data)
    print ("Data Length : %02d" %dataLen)
    for i in range (0, dataLen):
        print ("data[%d] : 0x%02X" % (i, data[i]))
    print(data)
    #data[9] = 0x9 # TypeError: 'bytes' object does not support item assignment
    #data[10] = 0x10 # TypeError: 'bytes' object does not support item assignment
    #data[10] = b'\x10'# TypeError: 'bytes' object does not support item assignment
    print (data)

# ------------------------------------------------------------------------------
# Main program
# ------------------------------------------------------------------------------
def main():
    byteObjectManipulation()

    data = b'\xFF\xFF\xFF\x3C\xC3\x88\x00\xA9\x01\x00\x01\x00\x02\xF7\xB2'
    dataLen = len(data)
    print ("Data Length : %02d" %dataLen)
    for i in range (0, dataLen):
        print ("data[%d] : 0x%02X" % (i, data[i]))

    binaryDataCompare()

# ------------------------------------------------------------------------------
# Code entry
# ------------------------------------------------------------------------------      
if __name__ == "__main__":
    main()
    #msg = main()
    #print(msg)
    #mainloop()


"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))


"""


# ------------------------------------------------------------------------------
# Why (  if __name__ == "__main__":  )
# ------------------------------------------------------------------------------      
"""
http://stackoverflow.com/questions/419163/what-does-if-name-main-do

  When the Python interpreter reads a source file, it executes all of the code
  found in it. Before executing the code, it will define a few special variables. 
  For example, if the python interpreter is running that module (the source file)
  as the main program, it sets the special __name__ variable to have a value
  "__main__". If this file is being imported from another module, 
  __name__ will be set to the module's name.

  In the case of your script, let's assume that it's executing as the main 
  function, e.g. you said something like python threading_example.py on the 
  command line. After setting up the special variables, 
  it will execute the import statement and load those modules. 
  It will then evaluate the def block, creating a function object and 
  creating a variable called myfunction that points to the function object.
  It will then read the if statement and see that __name__ does equal 
  "__main__", so it will execute the block shown there.

  One of the reasons for doing this is that sometimes you write a module 
  (a .py file) where it can be executed directly. Alternatively, it can also
  be imported and used in another module. By doing the main check, 
  you can have that code only execute when you want to run the module as 
  a program and not have it execute when someone just wants to import 
  your module and call your functions themselves.

"""