import RPi.GPIO as GPIO
import time
from mpu6050 import mpu6050
import math
sensor=mpu6050(0x68)

##Enter set up parameters
CLK_M1 = 15
CW_M1 = 18
CLK_M2 = 17
CW_M2 = 27
degperstep=1.8

##Setup Pin Modes
GPIO.setmode(GPIO.BCM)
GPIO.setup(CLK_M1, GPIO.OUT) #CLK
GPIO.setup(CW_M1, GPIO.OUT) #CW
GPIO.setup(CLK_M2, GPIO.OUT) #CLK
GPIO.setup(CW_M2, GPIO.OUT) #CW

def rotateMotorR():
    #Set direction
    GPIO.output(CW_M2,GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(CLK_M2,GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(CLK_M2,GPIO.LOW)


def rotateMotorL():
    #Set direction
    GPIO.output(CW_M1,GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(CLK_M1,GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(CLK_M1,GPIO.LOW)


def move_forward(speed):
    #Find the residual delay
    T = (degperstep*60)/(360*speed)
    T = T - 0.0004
    print(T)
    if T<0: #Faster than maximum
        T = 0

    #Set direction
    GPIO.output(CW_M2,GPIO.HIGH)
    GPIO.output(CW_M1,GPIO.LOW)
    time.sleep(0.0004)
    GPIO.output(CLK_M1,GPIO.HIGH)
    GPIO.output(CLK_M2,GPIO.HIGH)
    time.sleep(0.0004)
    GPIO.output(CLK_M1,GPIO.LOW)
    GPIO.output(CLK_M2,GPIO.LOW)
    time.sleep(T)

def move_backward(speed):
    #Find the residual delay
    T = (degperstep*60)/(360*speed)
    T = T - 0.0004
    print(T)
    if T<0: #Faster than maximum
        T = 0

    #Set direction
    GPIO.output(CW_M1,GPIO.HIGH)
    GPIO.output(CW_M2,GPIO.LOW)
    time.sleep(0.0004)
    GPIO.output(CLK_M1,GPIO.HIGH)
    GPIO.output(CLK_M2,GPIO.HIGH)
    time.sleep(0.0004)
    GPIO.output(CLK_M1,GPIO.LOW)
    GPIO.output(CLK_M2,GPIO.LOW)
    time.sleep(T)


def TestMotors():
    print('Testing Right Motor ...')
    for i in range(1000):
        rotateMotorR()

    print('Testing Left Motor ...')
    for i in range(1000):
        rotateMotorL()

    print('Moving Forward ...')
    for i in range(1000):
        move_forward(0.0004)

    print('Moving Backward ...')
    for i in range(1000):
        move_backward(0.0004)

def get_Tilt():
    data = sensor.get_accel_data()
    tilt = math.atan(data["x"]/(math.sqrt(data["y"]**2+data["z"]**2)))
    tilt=tilt*180/math.pi
    return tilt #Value between -90 and 90degrees

def TestGyro():
    print('Fetching data from gyro')
    for i in range(200):
        print(get_Tilt())
        time.sleep(0.3)

while True:
    move_backward(200) #1 per second

