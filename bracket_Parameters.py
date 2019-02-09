# -*- coding: utf-8 -*-
"""
    Python 
    ~~~~~~~~~~~

    Module to provide an import shortcut for the most common VISA operations.

    This file is part of PyVISA.

    :copyright: 2014 by PyVISA Authors, see AUTHORS for more details.
    :license: MIT, see COPYING for more details.
"""

import os
import time

## ----------------------------------------------------------------------------
def format_parameter():
  i = 123; 
  j = 456;
  s = '{0}:{1}\n'.format('%-15s'%i, '%02X'%j)
  # {0} - First parameter of format
  # {1} - Second parameter of format
  
  s1 = "{2} {1} {0} {3}".format( "going", "is", "what", 'on?' )
  # => s1 == 'what is going on?'
  
  s2 = "{Third} {Second} {First} {Fourth}".format( First="going", Second="is", Third="what", Fourth='on?' )
  
  return s

def main():
    format_parameter()
    return;

## ----------------------------------------------------------------------------
if __name__ == "__main__":
    main()


##-----------------------------------------------------------------------------
"""
Resources:
 - 

"""
