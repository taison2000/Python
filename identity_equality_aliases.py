#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Python : Generator
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import time


## ----------------------------------------------------------------------------
same_person_1 = {'name':'Charles L. Dodgson', 'born':1823}
same_person_1 = same_person_2

same_person_1 == same_person_2  # True, same_person_1.__eq__(same_person_2)
same_person_1 is same_person_2  # True
id(same_person_1) == id(same_person_2)  # same id, so same_person_2 is alias of same_person_1

## update 'same_person_1', then 'same_person_2' also being changed
same_person_1['balance'] = 950
print(same_person_2) # {'born': 1823, 'name': 'Charles L. Dodgson', 'balance': 950}

diff_person = {'born': 1823, 'name': 'Charles L. Dodgson', 'balance': 950}
diff_person == same_person_1    # True, both have same value, result of __eq__
diff_person is same_person_1    # False, different id


# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    """
    - range()
    """
    pass

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
else:
    """
    Called by other module
    """
    pass

##-----------------------------------------------------------------------------
## Python source code
# - https://www.python.org/downloads/source/

##-----------------------------------------------------------------------------
"""
Resources:

 - https://wiki.python.org/moin/Generators
 - 

"""

##-----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Note: 
# -----------------------------------------------------------------------------
"""

  - No ++ or --, use a+=1 or a-=1 
  - print ("Variable %d", %Val)
    print ("Variable %d %d", % (Val1, Val2))
  - Syntax Tip : line breaks are ignored inside pairs of [], {}, or ().
    So building multiline lists, liscomps, genexps, dictionaries and the like no need
    no need to use \ for line continuation escape
  - 
"""

'''
3 single quote string
'''

