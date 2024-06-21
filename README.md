![image](https://github.com/piyush-khanna-qmb/Zoomer-Boomer/assets/97603905/3e5096d6-3a83-4507-a6f8-e374676d40ba)

It's officially job grabbing session for us as it June of '23 and I'm still not over with my projects.
We face many coding rounds where the IDEs are lame and don't support copy/paste functionality.
Why bother paste inability ffs, when you can type what you've got on clipboard? And why worry when you can automate the typing process itself? And why even design the code's algo when you can get that code from your buddy's machine over bluetooth, which his lazy ass copies from GFG or SoF?

Yup, here's the deal:

**Zoombastic.py**
The python code running in side thread of your friend's machine that keeps a check on the clipboard of user profile using win32clipboard.
In case something worthwhile is copied, it passes the text with its line breaks and indentation preserved, to Zoomer ESP.
The person need not paste the text to Serial monitor himself, thus avoiding byte reference errors or baudrate cache empty errors or any such Arduino IDE-specific random BS.

**Zoomer.ino**:
The Sender ESP.
Your buddy searches for code over internet from his machine; Copies it and pastes it on the serial monitor of the ESP connected to his laptop.

**Boomer.ino**:
The recieving ESP
Boomer gets the data incoming from Zoomer over local WiFi, with proper indentation and line breaks maintained in case of our friendly neighbourhood Python.

**Boombastic.py**
The python code running in side thread over the cheater's machine to keep a check of data incoming to Boomer's Serial monitor using PySerial.
Goes on to typewrite whatever it recieves from Zoomer end.
