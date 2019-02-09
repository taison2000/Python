#!/usr/bin/python
# Comment start with #


# Append mode will add data to the end of the file.

# Write mode will overwrite the file.

# Either mode will create the file automatically if it doesn't already exist, 
# 

# 'write' mode
logfile = open('test.log', 'w')                    
logfile.write('test succeeded')                    
logfile.close() 
print ( file('test.log').read() )

# 'append' mode
logfile = open('test.log', 'a')                    
logfile.write('line 2') 
logfile.close() 
print ( file('test.log').read() )
           

#------------------------------------------------------------------------------
# Resource
#  http://www.sthurlow.com/python/
# 
