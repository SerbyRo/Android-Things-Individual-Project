import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.setup(24, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#GPIO.output(24, GPIO.LOW)
#GPIO.output(18, GPIO.LOW)

while True:
    switch_state = GPIO.input(23)
    if switch_state == GPIO.LOW:
        GPIO.output(18,GPIO.LOW)
        GPIO.output(24,GPIO.HIGH)
        time.sleep(5)
    else:
        GPIO.output(24, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(3)


GPIO.cleanup()
