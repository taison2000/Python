# -*- coding: utf-8 -*-
"""
in -

"""

from __future__ import division, unicode_literals, print_function, absolute_import
from pyvisa import logger, __version__, log_to_screen, constants
from pyvisa.highlevel import ResourceManager


def in_a_list():
  l = [('50', 50), ('75', 75), ('110', 110), ('134', 134), ('150', 150), ('200', 200), ('300', 300), ('600', 600), ('1200', 1200), ('1800', 1800), ('2400', 2400), ('4800', 4800), ('9600', 9600), ('19200', 19200), ('38400', 38400), ('57600', 57600), ('115200', 115200)]
  if ('2400', 2400) in l:
    print ("yes")
  else:
    print ("No")

def keyword_in_test():
  in_a_list()

# ------------------------------------------------------------------------------
# Code entry
# ------------------------------------------------------------------------------  
if __name__ == '__main__':
  keyword_in_test()