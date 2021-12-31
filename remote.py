#!/usr/bin/python

import broadlink
import time
import sys
import fileinput



device = broadlink.rm(("broadlink",80), bytearray.fromhex("780f77fd3d92"), 0x2712)

print ("Connecting to Broadlink device....")
device.auth()
time.sleep(1)
print ("Connected....")


for command in fileinput.input():
   command=command.strip()
   with open(command + ".ir","br") as fin:
      ir_packet=fin.read()
   device.send_data(ir_packet)
   print (" '%s' Code Sent...."%(command))
