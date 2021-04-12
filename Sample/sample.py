import time
import sys
import os
sys.path.append(os.getcwd())
import math 
from config.config import *
from Gyro.Gyro import Gyro
from Utils.Visualisation.Visual import *
    
try:
    import RPi.GPIO as GPIO
    from mpu6050 import mpu6050
except:
    print('[INFO] Could not import pi based packages')

#Instantiate a gyro object
Gyroscope = Gyro(gyro_addr)
Tilt = []
Time = []
fig = plt.figure(figsize=(12,6))
while True:
    #Extract the value continuously
    try:
        angle = Gyroscope.get_Tilt()
    except:
        print('Could not fetch angle value')
    #Plot it in a loop
    Tilt, Time = livePlot(angle, Tilt, Time)
    time.sleep(0.5)