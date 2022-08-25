#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	id = input('New RFID Detected Enter Card Id: ')
	text = input('Enter Name And Roll No.: ')
	print("Now place your tag to write")
	reader.write(id)
	reader.write(text)
	print("Written")
finally:
        GPIO.cleanup()
