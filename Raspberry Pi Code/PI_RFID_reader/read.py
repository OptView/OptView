import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
print("Check Your Tag")
try:
    id, text = reader.read()
    if text:
        print(type(text))
    else:
        print("Nothing")
finally:
    GPIO.cleanup()