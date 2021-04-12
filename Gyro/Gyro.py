import time
import sys
import os
sys.path.append(os.getcwd())
import math 
from config.config import *
    
try:
    import RPi.GPIO as GPIO
    from mpu6050 import mpu6050
except:
    print('[INFO] Could not import pi based packages')


class Gyro:
    def __init__ (self, addr):
        self.address = addr

    def get_Tilt(self):
        data = sensor.get_accel_data()
        tilt = math.atan(data["x"]/(math.sqrt(data["y"]**2+data["z"]**2)))
        tilt=tilt*180/math.pi
        return tilt #Value between -90 and 90degrees