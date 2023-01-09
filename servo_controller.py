import RPi.GPIO as GPIO
import time

class ServoController:
    def __init__(self, pin, angle):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.p = GPIO.PWM(pin, 50)
        if angle == 0:
            self.p.start(3)
        elif angle == 45:
            self.p.start(5.5)
        elif angle == 90:
            self.p.start(8)
        elif angle == 135:
            self.p.start(10.25)
        elif angle == 180:
            self.p.start(12.5)
        else:
            self.p.start(8)
        time.sleep(0.5)
    
    def degree(self, angle):
        time_sleep = 0.5
        if angle == 0:
            self.p.ChangeDutyCycle(3)
        elif angle == 45:
            self.p.ChangeDutyCycle(5.5)
        elif angle == 90:
            self.p.ChangeDutyCycle(8)
        elif angle == 135:
            self.p.ChangeDutyCycle(10.25)
        elif angle == 180:
            self.p.ChangeDutyCycle(12.5)
        else:
            time_sleep = 0
        time.sleep(time_sleep)

    def example1(self):
        self.degree(0)
        self.degree(45)
        self.degree(90)
        self.degree(135)
        self.degree(180)
        self.degree(135)
        self.degree(90)
        self.degree(45)
        self.degree(0)
    
    def example2(self, reps):
        for i in range(0, reps):
            self.degree(45)
            self.degree(135)
    
    def example3(self, reps):
        for i in range(0, reps):
            self.degree(0)
            self.degree(180)

    def example4(self, reps):
        for i in range(0, reps):
            self.degree(90)
            self.degree(45)
            self.degree(135)
            self.degree(0)
            self.degree(180)
            self.degree(45)
            self.degree(135)
            self.degree(90)

    def stop(self):
        self.p.stop()
        GPIO.cleanup()
