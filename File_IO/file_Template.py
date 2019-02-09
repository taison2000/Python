#!/usr/bin/python
# Comment start with #

#------------------------------------------------------------------------------
#  open - built-in function
#------------------------------------------------------------------------------

"""
#------------------------------------------------------------------------------
File Attributes:
  - closed
  - mode
  - name
  - softspace
#------------------------------------------------------------------------------
"""
  

"""
#------------------------------------------------------------------------------
File methods:
  - buffer
  - close
  - detach
  - encoding
  - errors
  - fileno
  - flush
  - isatty
  - line_buffering
  - newlines
  - read
  - readable
  - readline
  - readlines
  - seek
  - seekable
  - tell
  - truncate
  - writable
  - write
  - writelines
#------------------------------------------------------------------------------
"""

#------------------------------------------------------------------------------

fo = open ('somefile.txt', 'w')
print ('This is the first line', file=fo)
print ('This is the second line', file=fo)
print ('This is the third line', file=fo)

# File Number
print ("File Number : ", fo.fileno())

fo.close()        # "close" - method
print(fo.closed)  # "closed" - attribute


#------------------------------------------------------------------------------
# Resource
#  http://www.sthurlow.com/python/
# 


##-----------------------------------------------------------------------------
# See "import os" for related file naming, deletion, etc
# 
