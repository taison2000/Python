#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  bytes, bytearray

"""

'''bytes''' """vs""" '''bytearray'''

bytes_data     = b'\x00\x00\x01\x02\x03'    # bytes data content can not be changed
bData = bytes(5) # => bData == b'\x00\x00\x00\x00\x00'

bytearray_data = bytearray(b'\x00\x00\x01\x02\x03')
bData = bytearray(5) #=> bytearray(b'\x00\x00\x00\x00\x00')

"""
1. bytes content can not be changed
   bytearray content can be modified.
"""

"""
bData = bytes(5) => bData == b'\x00\x00\x00\x00\x00'

"""
import os
import time

## --- bytearray of nothing ---
byteNothing = b''

def method_encode():
    'spameggs'.encode('utf16')  #=> b'\xff\xfes\x00p\x00a\x00m\x00e\x00g\x00g\x00s\x00'
    'spameggs'.encode('utf-8')  #=> b'spameggs'

    return

""""
# -----------------------------------------------------------------------------
# Convert a list of bytes to array of bytes
#  for example, convert 'orgData' to 'modData'
#   orgData = [ 0xFF, 0xFF, 0xC3, 0x88, 0x00, 0xA9,  0x01, 0x02, 0xF7, 0xB2 ]
#   modData = b'\xFF\xFF\xC3\x88\x00\xA9\x01\x02\xF7\xB2'
# -----------------------------------------------------------------------------
"""
def ConvertToByteArray( orgData ):
    byteLength = len (orgData)

    newInt = int.from_bytes(orgData, byteorder='big') # newInt==1208921462382715560196018
    arrayBytes = newInt.to_bytes(byteLength, byteorder='big')

    #newInt = int.from_bytes(orgData, byteorder='little') # newInt==845137724319485919494143
    #arrayBytes = newInt.to_bytes(byteLength, byteorder='little')

    ## This can be done by using '''bytearray'''
    #modData = bytearray( orgData )

    return arrayBytes

def endian():
    """
    big endian - most significant value in the sequence is stored first
    little endian - the least significant value in the sequence is stored first
    """
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
    value = [ 0xFF, 0xFF, 100, 0xC3, 0x88, 10, 0xA9, 11, 0x02, 0xF7, 0xB2 ]
    # => value==[255, 255, 100, 195, 136, 10, 169, 11, 2, 247, 178]

    value[9] = 0x99  #<-- Replace 0xF7 with 0x99 
    #value==[255, 255, 100, 195, 136, 10, 169, 11, 2, 153, 178]; 0x99==153

    print("Original Data : ", value)
    print ("Data length : ", len(value))  #=> 11

    newData = ConvertToByteArray(value) 
    # => b'\xff\xffd\xc3\x88\n\xa9\x0b\x02\x99\xb2'

    print("Modified Data : ", newData)
    print ("Data length after mod : ", len(newData))

    return;


## ----------------------------------------------------------------------------
def concat_bytes_and_bytearray():
    """
    1. If append bytearray to bytes, result is bytes
    2. If append bytes to bytearray, result is bytearray
    """

    b  = b'\x00\x01\x02\x03'
    ba = bytearray(b'\x05\x06\x07\x08')

    result1 = b + ba  # result is 'bytes'
    result2 = ba + b  # result is 'bytearray'

    return;

## ----------------------------------------------------------------------------
def convert_string_to_bytearray_hex():
    data = "f1 c3 3c 06 04 30 30 30 30 30 30 30 31 2e"
    
    """ bytearray """
    bytearray_data = bytearray.fromhex( data )
    bytearray_data[12] = 61 ## ok to change bytearray_data data.
    ## following would cause exception(ValueError) because 'gg' is non-hexadecimal number
    bytearray_data = bytearray.fromhex( "aa bb gg" )

    """ bytes """
    byte_data = bytes.fromhex( data )   #<- byte_data content can not be change
    # b'\xf1\xc3<\x06\x0400000001.'
    return;

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
 - Convert string to bytearray:
  http://stackoverflow.com/questions/5649407/hexadecimal-string-to-byte-array-in-python
  

"""

