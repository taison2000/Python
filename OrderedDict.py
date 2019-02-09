# -----------------------------------------------------------------------------
# 			Hunter Industries
#
# updated       Description
# ---------------------------------------------
# 05/27/2015   	 Initial Release
#
# -----------------------------------------------------------------------------

##-----------------------------------------------------------------------------

'''----- Need this import for Ordered Dictionary -----'''
from collections import OrderedDict


gbRetrieveResp = b'\xFF\xFF\x3C\xC3\x82\x00\xC1\x01\x00\x01\x00\x0B\xA5\xBD'
gbRetrieveCmd = b'\xFF\xFF\x3C\xC3\x82\x00\xA9\x01\x00\x03\x00\x0B\x01\x00\x70\x2D'

gdRetrieveSave = OrderedDict ([
  ('Preamble', b'\xFF\xFF\x3C\xC3'), # Byte[0:3]
  ('SystemId', b'\x82'),    # Byte[4]
  ('SiteId', b'\x00'),      # Byte[5]
  ('Fcb', b'\xA9'),         # Byte[6]
  ('DeviceId', b'\x01\x00'),# Byte[7:8]
  ('Len', b'\x03\x00'),     # Byte[9:10]- LEN (from Command ID to end of data not including CRC)
  ('CommandId' , b'\x0B'),  # Byte[11]
  ('RetFunc' , b'\x01'),    # Byte[12]
  ('RetNum' , b'\x00'),     # Byte[13]
  ('Checksum', b'\x70\x2D') # Byte[14:15]
])



def printDict (dictData):
  for k in dictData:
    print (k, ':', dictData[k])

def printByteArrayDict (dictData):
  for k in dictData:
    s=''
    for j in dictData[k]:
      s+=format(j, '02X')+' '
    print (k, ':', s)



def Analysis_OrderedDict_Each_Field_Length ():
  global gdRetrieveSave
  
  ## print out the size of each field
  for k in gdRetrieveSave:
    print("Size of %s is %d" % (k, len(gdRetrieveSave[k])))
    
  return;


def CopyByteArrayToOrderedDict(byteArray, orderedDict):
  """
    Convert the bytearray data to an Ordered Dictionary
  """
  startPos = 0;
  endPos = 0
  for key in orderedDict:
    length = len(orderedDict[key])
    endPos = startPos+length
    orderedDict[key] = byteArray[startPos:endPos]
    startPos=endPos
    #print("Size of %s is %d" % (key, len(orderedDict[key])))

  return orderedDict;

  
## ----- Add -----
# Add item to an OrderedDict 
# - http://stackoverflow.com/questions/16664874/how-can-i-add-the-element-at-the-top-of-ordereddict-in-python
def AddItemsToAnOrderedDict():
  od = OrderedDict([
    ('First Name', 'John'),   ## Note: between key and value, use comma(,), not colon(:)
    ('Last Name', 'Doe'),
    ('Birth Year', 1981),
    ('Birth Month', 10),
    ('Birth Day', 28),
  ])
  print(od)
  
  od.update({'Age': 38})  ## None: Now use comma(,) between key and value
  print (od)
  
  od.update({'occupation', 'engineer'})
  print(od)
  
  return;


##-----------------------------------------------------------------------------
if __name__=="__main__":
  Analysis_OrderedDict_Each_Field_Length()
  

##-----------------------------------------------------------------------------
"""
Resources:
 - http://stackoverflow.com/questions/16664874/how-can-i-add-the-element-at-the-top-of-ordereddict-in-python


"""
