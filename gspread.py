#!/usr/bin/python3

import serial
import time
   
def main():
    con=serial.Serial('/dev/ttyACM0', 9600)
#   print (con.portstr)
#   while 1:
#       str=con.readline()
#       print (len(str))
#       print (str)
   
    str=con.readline()
#   print (len(str))
    print (int(str))

if __name__ == '__main__':
    main()
