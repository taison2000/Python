# function call parameters are pass by value.
# Original variable is not affected.
def increment(x):
  x=x+1
  print (x)
  
def change_list_content(l):
  print ('got', l)
  l.append('four')
  print ("list change to", l)
  
if __name__ == "__main__":
  y = 27
  print (y)
  increment (y)
  print (y)

  # List pass to function is by reference
  list = ['one', 'two', 'three']
  print ("before function call = ", list)
  change_list_content(list)
  print ("after function call = ", list)
  
## ----------------------------------------------------------------------------
