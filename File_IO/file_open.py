#!/usr/bin/python
# Comment start with #

fo = open ('somefile.txt', 'w')
print ('This is the first line', file=fo)
print ('This is the second line', file=fo)
print ('This is the third line', file=fo)

fo.close()        # "close" - method
print(fo.closed)  # "closed" - attribute


#------------------------------------------------------------------------------
# Resource
#  http://www.sthurlow.com/python/
# 
