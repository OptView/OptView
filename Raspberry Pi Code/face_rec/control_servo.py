from gpiozero import AngularServo
from time import sleep
import threading

servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0025)


def move_servo():
    servo.angle = 60
    sleep(3)  # Adjust the sleep time as needed
    servo.angle = -30


def move_servo_non_blocking():
    threading.Thread(target=move_servo).start()


# Test the function if needed
if __name__ == "__main__":
    move_servo_non_blocking()
