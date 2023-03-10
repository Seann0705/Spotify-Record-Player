#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        print("Waiting for a RFID sticker to be scanned...")
        id = reader.read()[0]
        print("The ID of the card is:", id)
        
finally:
        GPIO.cleanup()
       
       