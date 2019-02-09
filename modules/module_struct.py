#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
 Module - struct
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - 
"""

## ----------------------------------------------------------------------------

import os
import time
from struct import *

## ----------------------------------------------------------------------------
"""
Format  C_Type            Python_type         Standard_size   Notes 
----------------------------------------------------------------------------
x       pad byte            no value
c       char                bytes of length 1   1   
b       signed char         integer             1             (1),(3)
B       unsigned char       integer             1             (3) 
?       _Bool               bool                1             (1) 
h       short               integer             2             (3) 
H       unsigned short      integer             2             (3) 
i       int                 integer             4             (3)
I       unsigned int        integer             4             (3)
l       long                integer             4             (3)
L       unsigned long       integer             4             (3)
q       long long           integer             8             (2), (3)
Q       unsigned long long  integer             8             (2), (3)
n       ssize_t             integer                           (4) 
N       size_t              integer                           (4) 
f       float               float               4             (5) 
d       double              float               8             (5) 
s       char[]              bytes
p       char[]              bytes
P       void *              integer                           (6) 
"""

## ----------------------------------------------------------------------------
## ----------------------------------------------------------------------------
def method_Struct():
    stut = Struct('hhl')
    p = stut.pack(1, 2, 3)   # b'\x01\x00\x02\x00\x03\x00\x00\x00'

## ----------------------------------------------------------------------------
def method_pack():
    """
    pack( fmt, v1, v2, ... ) -> bytes
    pack('h', 3) => b'\x03\x00'
    pack('l', 3) => b'\x03\x00\x00\x00'
    pack('hh', 3, 5) => b'\x03\x00\x05\x00'
    pack('hl', 1, 2) => b'\x01\x00\x00\x00\x02\x00\x00\x00'

    """
    p1 = pack('l', 10)
    p1 = pack('h', 10)
    p2 = pack('hl', 1, 2)
    p3 = pack('hhl', 1, 2, 3)
    return;

## ----------------------------------------------------------------------------
def method_unpack():
    b = b'\x12\x45\x00\xAB'

    val = struct.unpack( '<BBH', b ) # val==(18, 69, 43776) - tuple

    ## big endian; little endian
    val = struct.unpack( '>BBH', b )  # big endian
    val = struct.unpack( '<BBH', b )  # little endian
    val = struct.unpack( 'BBH', b )   # little endian (default)

    return;

def method_unpack1():
    a  = b'\xca\xfe\xba\xbe'

    # b==(3405691582,)  <- Tuple
    b = struct.unpack(">I", a)

    # b==3405691582     <- First item of tuple
    b = struct.unpack(">I", a)[0]

    # c=='0xcafebabe'
    c = hex( struct.unpack(">I", a)[0] )

    return;

# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    method_unpack()

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


## ----------------------------------------------------------------------------
## Resource
## ----------------------------------------------------------------------------
"""
 - book : Introducing Python ( Bill Lubanovic )
    CH7 - Mangle Data Like a Pro
  
  
"""

