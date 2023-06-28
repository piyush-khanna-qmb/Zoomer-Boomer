"""
The program on the reciever side to print whatever is coming from the sender (Zoomer) side
"""

import serial
import time
import pyautogui as pag

boom= serial.Serial('COM5', 115200)

#shit-ignore
time.sleep(5)
print("Assuming ready for texts now :)")
hh= boom.read_all()

while True:
    got= boom.read_all().decode('ascii')
    if got:
        print("Got new text")
        time.sleep(1)
        print("Now printing in 5 seconds...")
        pag.typewrite(got)