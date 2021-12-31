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

for codename in fileinput.input():
   codename=codename.strip()
   device.enter_learning()

   ir_packet = None
   while ir_packet == None:

      time.sleep(1)
      try:
         ir_packet = device.check_data()
      except:
         pass


   with open(codename + ".ir", "bw") as fout:
      fout.write(ir_packet)

   print("Learned !")