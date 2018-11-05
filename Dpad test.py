import RPi.GPIO as GPIO
from time import sleep

#lights
red = 27
green = 18
blue = 17

#direction
up = 26
down = 12
right = 19
left = 16

#Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(right, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(left, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


try:
    while (True):
        if (GPIO.input(up) == GPIO.HIGH):
            print "UP"
            GPIO.output(red,GPIO.HIGH)
            sleep(0.1)
            GPIO.output(red,GPIO.LOW)
            sleep(0.1)

        if (GPIO.input(down) == GPIO.HIGH):
            print "DOWN"
            GPIO.output(green,GPIO.HIGH)
            sleep(0.1)
            GPIO.output(green,GPIO.LOW)
            sleep(0.1)

        if (GPIO.input(right) == GPIO.HIGH):
            print "RIGHT"
            GPIO.output(blue,GPIO.HIGH)
            sleep(0.1)
            GPIO.output(blue,GPIO.LOW)
            sleep(0.1)

        if (GPIO.input(left) == GPIO.HIGH):
            print "LEFT"
            GPIO.output(red,GPIO.HIGH)
            sleep(0.1)
            GPIO.output(red,GPIO.LOW)
            sleep(0.1)
except KeyboardInterrupt:
    print "Ending"
    GPIO.cleanup()
