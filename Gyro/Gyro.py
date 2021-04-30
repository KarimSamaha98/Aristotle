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

    def get_Tilt(self, tilt, dt):
        Complementary = True
        data = sensor.get_accel_data()
        gyro = sensor.get_gyro_data()
        if Complementary:
            acc = math.atan(data["x"]/(math.sqrt(data["y"]**2+data["z"]**2)))
            gyro = gyro["y"]
            tilt = 0.98*(tilt + gyro*dt) + 0.02*acc
        else:
            tilt = math.atan(data["x"]/(math.sqrt(data["y"]**2+data["z"]**2)))
        tilt=math.atan(data["x"]/data["z"])
        tilt=tilt*180/math.pi
        return tilt #Value between -90 and 90degrees

if __name__ == "__main__":
    Gyro = Gyro(gyro_addr)
    tilt = 0
    init = time.time()
    while(True):
        final = time.time()
        dt = final - init
        print(Gyro.get_Tilt(tilt, dt))
        time.sleep(0.1)
        init = time.time()
