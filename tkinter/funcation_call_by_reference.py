#!/usr/bin/python

# Function definition is here
def changeme( mylist ):
  "This changes a passed list into this function"
  mylist = [1,2,3,4]; # This would assign NEW reference in mylist, so it has nothing to do with original list
  print ("Values inside the function: ", mylist)
  return

def AppendToList(myL):
  myL.append([1,2,3,4]) #<- This will modify the original list
  print ( "Value inside the function: ", myL)
  return;

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)

AppendToList(mylist)
print ("Values outside the function: ", mylist)