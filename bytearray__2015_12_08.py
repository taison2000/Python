#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  bytes, bytearray

"""

'''bytes''' """vs""" '''bytearray'''
"""
bData = bytes(5) => bData == b'\x00\x00\x00\x00\x00'

"""
import os
import time

## --- bytearray of nothing ---
byteNothing = b''

""""
# -----------------------------------------------------------------------------
# Convert a list of bytes to array of bytes
#  for example, convert 'orgData' to 'modData'
#   orgData = [ 0xFF, 0xFF, 0xC3, 0x88, 0x00, 0xA9,  0x01, 0x02, 0xF7, 0xB2 ]
#   modData = b'\xFF\xFF\xC3\x88\x00\xA9\x01\x02\xF7\xB2'
# -----------------------------------------------------------------------------
"""
def ConvertToByteArray (orgData):
  byteLength = len (orgData)
  newInt = int.from_bytes(orgData, byteorder='big')
  arrayBytes = newInt.to_bytes(byteLength, byteorder='big')
  return (arrayBytes)
# This can be done by using '''bytearray'''

def endian ():
  big = (0x010203).to_bytes(5, byteorder='big')       ##   big  == b'\x00\x00\x01\x02\x03'
  little = (0x010203).to_bytes(5, byteorder='little') ## little == b'\x03\x02\x01\x00\x00'
  print (big, little)
  big = bytearray((0x010203).to_bytes(5, byteorder='big'))       ##   big  == b'\x00\x00\x01\x02\x03'
  little = bytearray((0x010203).to_bytes(5, byteorder='little')) ## little == b'\x03\x02\x01\x00\x00'
  
def test_01():
  accCmd = ( 0xFF, 0xFF, 0xFF, 0x3C, 0xC3, 0x88, 0x00, 0xA9, 0x01, 0x00, 0x01, 0x00, 0x02, 0xF7, 0xB2 ) # Tuple
  accCmd = [ 0xFF, 0xFF, 0xFF, 0x3C, 0xC3, 0x88, 0x00, 0xA9, 0x01, 0x00, 0x01, 0x00, 0x02, 0xF7, 0xB2 ] # List
  print(accCmd)
  print ("Data length : ", len(accCmd))
  newData = ConvertToByteArray(accCmd)
  print ("Data length after mod : ", len(newData))
  print(newData)

def test_02():
  #accCmd = ( 0xFF, 0xFF, 0xFF, 0x3C, 0xC3, 0x88, 0x00, 0xA9, 0x01, 0x00, 0x01, 0x00, 0x02, 0xF7, 0xB2 )
  accCmd = [ 0xFF, 0xFF, 0xFF, 0x3C, 0xC3, 0x88, 0x00, 0xA9, 0x01, 0x00, 0x01, 0x00, 0x02, 0xF7, 0xB2 ]
  accCmd[9] = 0x99  #""" Modify data """
  print(accCmd)
  print ("Data length : ", len(accCmd))
  newData = ConvertToByteArray(accCmd)
  print ("Data length after mod : ", len(newData))
  print(newData)

def test_03():
  # data has mixed of hexadecimal and decimal
  accCmd = [ 0xFF, 0xFF, 100, 0xC3, 0x88, 10, 0xA9, 11, 0x02, 0xF7, 0xB2 ]
  accCmd[9] = 0x99  #<-- Replace 0xF7 with 0x99 
  print("Original Data : ", accCmd)
  print ("Data length : ", len(accCmd))
  newData = ConvertToByteArray(accCmd)  
  print("Modified Data : ", newData)
  print ("Data length after mod : ", len(newData))

## ----------------------------------------------------------------------------
# Main program - This is the main function
## ----------------------------------------------------------------------------
def main():
  print()
  print("Begining of arrayBytes data manupiluation test")
  print()

  print ("------------------------------------------------------------------------------")
  print ("test #01")
  test_01()
  print ("------------------------------------------------------------------------------")
  print ("test #02")
  test_02()
  print ("------------------------------------------------------------------------------")
  print ("test #03")
  test_03()

  
# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
	main()


"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))

  

"""


##-----------------------------------------------------------------------------
"""
Resources:
 - 

"""

