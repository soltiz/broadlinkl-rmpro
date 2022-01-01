import broadlink
import time
import sys
import fileinput
from flask import Flask

app = Flask(__name__)
device = broadlink.rm(("broadlink",80), bytearray.fromhex("780f77fd3d92"), 0x2712)
device.auth()
print ("Connecting to Broadlink device....")
time.sleep(1)
print ("Connected....")


def sendIr(command):
   with open(command + ".ir","br") as fin:
      ir_packet=fin.read()
   device.send_data(ir_packet)
   print (" '%s' Code Sent...."%(command))

@app.route("/chup")
def increaseNadVolume():
    sendIr('up')
    return "<status>OK</status>"

@app.route("/chdown")
def decreaseNadVolume():
    sendIr('down')
    return "<status>OK</status>"

@app.route("/yellow")
def muteNad():
    sendIr('mute')
    return "<status>OK</status>"

@app.route("/green")
def switchOnNad():
    sendIr('on')
    return "<status>OK</status>"

@app.route("/red")
def switchOffNad():
    sendIr('down')
    sendIr('down')
    sendIr('off')
    return "<status>OK</status>"


