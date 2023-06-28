"""
The program on the sender side to send the message to the receiver (Boomer) side whenever a new text is copied and loaded on the clipboard.
"""

import serial
import win32clipboard
import time

# Serial port settings
serial_port = 'COM20'
baud_rate = 115200

# Connect to the serial port
ser = serial.Serial(serial_port, baud_rate)

# Continuously monitor the clipboard
copied_text= ""
win32clipboard.OpenClipboard()
try:
    # Check if the clipboard contains text
    if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
        # Get the copied text from the clipboard
        copied_text = win32clipboard.GetClipboardData()
        print("Last copied text was: "+copied_text)
except:
    pass
purana= naya= copied_text

while True:
    win32clipboard.OpenClipboard()
    try:
        # Check if the clipboard contains text
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
            # Get the copied text from the clipboard
            naya = win32clipboard.GetClipboardData()
            
            # Send the copied text to the serial port
            if naya!= purana:
                print("New text copied and sent to Boomer: "+naya)
                ser.write(naya.encode('ascii'))
                purana= naya

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        win32clipboard.CloseClipboard()

    time.sleep(0.1)  # Adjust delay as needed
