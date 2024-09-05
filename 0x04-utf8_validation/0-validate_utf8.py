#!/usr/bin/python3
"""
 a method that determines if a given data set represents a valid UTF-8 encoding
"""

def validUTF8(data) {
        bytes = 0
        n1 = 1 << 7
        n2 = 1 << 6

       for byte in data:
          byte = byte & 0xFF

           if bytes == 0:
               if (byte >> 5) == 0b110:
                   bytes = 1
               elif (byte >> 4) == 0b1100:
                   bytes = 2
               elif (byte >> 3) == 0b1100:
                   bytes = 3
               elif (byte >> 7):
                   return False

           else:
               if (byte >> 6) != 0b10:
                 return False
               bytes -= 1

       return bytes == 0
