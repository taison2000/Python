#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
  Python - Dictionary
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

"""
#------------------------------------------------------------------------------
Dictionary - dict:
  Methods
  - clear()
  - copy()
  - fromkeys()
  - get()
  - items()
  - keys()
  - move_to_end() #<- This only available to OrderedDict
  - pop()
  - popitem()
  - setdefault()
  - update()
  - values()
#------------------------------------------------------------------------------
"""

import os
import time

from collections import OrderedDict

## --- ORDERED dictionary ---
bOrderedGlobal = OrderedDict ([
  ('Preamble' , b'\xFF\xff\x3C\xC3'),
  ('SystemId' , b'\x88'),
  ('SiteId' , b'\x00'),
  ('Fcb' , b'\x00'),
  ('DeviceId' , b'\x01\x00'),
  ('Len' , b'\x14\x00'),
  ('CommandId' , b'\x01'),
  ('FwVer' , b'\x00'),
  ('EngRev' , b'\x00'),
  ('Size' , b'\x06\x00'),
  ('Hours' , b'\x00'),
  ('Minutes' , b'\x00'),
  ('Seconds' , b'\x00'),
  ('Month' , b'\x00'),
  ('Day' , b'\x00'),
  ('Year' , b'\xDF\x07'),
  ('SysDcHour' , b'\x00'),
  ('FcpDcHour' , b'\x00'),
  ('Options' , b'\x00'),
  ('CurEtap' , b'\x00'),
  ('MaxEtap' , b'\x00'),
  ('Response' , b'\x00'),
  ('ReportInterval' , b'\x00'),
  ('OptStatus' , b'\x00'),
  ('OffStatus' , b'\x00'),
  ('GblSeasAdj' , b'\x00\x00'),
  ('StackMode' , b'\x00'),
  ('SsPrgThold' , b'\x00'),
  ('SsgSsPrgThold' , b'\x00'),
  ('RotaryKnob' , b'\x00')
])

## Note: when print out a dictionary, items would not be in same order as list below
bCurGlobal = {
  'Preamble' : b'\xFF\xff\x3C\xC3',
  'SystemId' : b'\x88',
  'SiteId' : b'\x00',
  'Fcb' : b'\x00',
  'DeviceId' : b'\x01\x00',
  'Len' : b'\x14\x00',
  'CommandId' : b'\x01',
  'FwVer' : b'\x00',
  'EngRev' : b'\x00',
  'Size' : b'\x06\x00',
  'Hours' : b'\x00',
  'Minutes' : b'\x00',
  'Seconds' : b'\x00',
  'Month' : b'\x00',
  'Day' : b'\x00',
  'Year' : b'\xDF\x07',
  'SysDcHour' : b'\x00',
  'FcpDcHour' : b'\x00',
  'Options' : b'\x00',
  'CurEtap' : b'\x00',
  'MaxEtap' : b'\x00',
  'Response' : b'\x00',
  'ReportInterval' : b'\x00',
  'OptStatus' : b'\x00',
  'OffStatus' : b'\x00',
  'GblSeasAdj' : b'\x00\x00',
  'StackMode' : b'\x00',
  'SsPrgThold' : b'\x00',
  'SsgSsPrgThold' : b'\x00',
  'RotaryKnob' : b'\x00'
}

SampleOrderedDict = OrderedDict ([
  ('Preamble' , b'\xFF\xff\x3C\xC3'),
  ('SystemId' , b'\x88'),
  ('SiteId' , b'\x00'),
  ('Fcb' , b'\x00'),
  ('DeviceId' , b'\x01\x00'),
  ('Len' , b'\x14\x00'),
  ('CommandId' , b'\x01'),
  ('FwVer' , b'\x00'),
])
  
##-----------------------------------------------------------------------------
## --- update ---
def CombineDictionaries():
  d1 = {
    'Preamble' : b'\xFF\xff\x3C\xC3',
    'SystemId' : b'\x88',
    'SiteId' : b'\x00',
    'Fcb' : b'\x00',
    'DeviceId' : b'\x01\x00',
    'Len' : b'\x14\x00',
    'CommandId' : b'\x01',
  }
  
  d2 = {
    'FwVer' : b'\x00',
    'EngRev' : b'\x00',
    'Size' : b'\x06\x00',
    'Hours' : b'\x00',
    'Minutes' : b'\x00',
    'Seconds' : b'\x00',
    'Month' : b'\x00',
    'Day' : b'\x00',
    'Year' : b'\xDF\x07',
    'SysDcHour' : b'\x00',
    'FcpDcHour' : b'\x00',
    'Options' : b'\x00',
    'CurEtap' : b'\x00',
    'MaxEtap' : b'\x00',
    'Response' : b'\x00',
    'ReportInterval' : b'\x00',
    'OptStatus' : b'\x00',
    'OffStatus' : b'\x00',
    'GblSeasAdj' : b'\x00\x00',
    'StackMode' : b'\x00',
    'SsPrgThold' : b'\x00',
    'SsgSsPrgThold' : b'\x00',
    'RotaryKnob' : b'\x00'
  }

  ## Use "update" method to join two dictionaries.
  d1.update( d2 )
  
  return
  
##-----------------------------------------------------------------------------
## --- Add an item to an Ordered Dictionary ---
def add_item_to_OrderedDict():
  # can not use dictResult = dict1 + dict2
  rd = OrderedDict ([
    ('System id', 0x111),
    ('Count', 100),
    ('System Name', 'Hunter Controller'),
    ('Program ID', 1234),
  ])
  print( rd )
  
  rd.update( [("NewItem", 'NI_Key_123')] )    ## Notice [(Key, value)] format for OrderedDict
  rd.update( {"NewItemAgain", 'Key_again'} )  ## or this format
  
  print( rd )
  
  # simply
  rd["newKey"] = "Just added"
  
  return;
  
  
##-----------------------------------------------------------------------------
def nestedDictionary():
  from collections import OrderedDict
  baseDataDict = OrderedDict([ # Total 5 Bytes
    ('s_MOD_TYPE', b'\x01'),      # 1B
    ('s_SLOT', b'\x00'),          # 1B
    ('s_MOD_FW_VER', b'\x00\x00'),# 2B
    ('s_MOD_ENG_REV', b'\x00'),   # 1B
  ])
  
  nestedDict = OrderedDict([
    ('head', b'\xff\xff\x3c\xc3'), 
    ('cmd', b'\x0a'), 
    ('data',baseDataDict), #<- nested dictionary
    ('checksum',b'\x34\xf3')
  ])
  
  print( nestedDict )
  #--> OrderedDict([('head', b'\xff\xff<\xc3'), ('cmd', b'\n'), ('data', OrderedDict([('s_MOD_TYPE', b'\x01'), ('s_SLOT', b'\x00'), ('s_MOD_FW_VER', b'\x00\x00'), ('s_MOD_ENG_REV', b'\x00')])), ('checksum', b'4\xf3')])
  
  for key in nestedDict:
    print( key, " : ", nestedDict[key])
# head  :  b'\xff\xff<\xc3'
# cmd  :  b'\n'
# data  :  OrderedDict([('s_MOD_TYPE', b'\x01'), ('s_SLOT', b'\x00'), ('s_MOD_FW_VER', b'\x00\x00'), ('s_MOD_ENG_REV', b'\x00')])
# checksum  :  b'4\xf3'

  return

##-----------------------------------------------------------------------------  
def main():
  print( '\nNormal dictionary' )
  print( bCurGlobal )  # Print entire dictionary, Notice the output is not the same order
  
  print( '\nOrdered dictionary' )
  print( bOrderedGlobal )

"""
  # access using items
  print ('\nfor loop access using ITEMS method')
  for k, v in bCurGlobal.items():
    print ('%-15s' % k, ':', v) ## left-aligned if when minus(-) sign
    #print ('%15s' % k, ':', v) ## right-aligned if no minus(-) sign

  print ('\nfor loop access using KEYS method')
  for k in bCurGlobal:
    print ('%-15s' % k, ':', bCurGlobal[k])
    
  print ('\nfor loop access using VALUES method')
  for v in bCurGlobal.values():
    print (v)
"""

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
  add_item_to_OrderedDict()
	#main()


