import time
import sys
import os
import multiprocessing
from multiprocessing import Value
sys.path.append(os.getcwd())
import math 
from config.config import *
from Gyro.Gyro import Gyro
from Utils.Visualisation.Visual import *
from Control.PID import *
from Control.Commander import *
import csv
try:
    import RPi.GPIO as GPIO
    from mpu6050 import mpu6050
except:
    print('[INFO] Could not import pi based packages')
import glob


#Clean Log
files = glob.glob('Data/*')
for f in files:
    os.remove(f)

#Reset Clock
reference_time = time.time()

#Controlling Loop
def MainLoop(speed):

    #Instantiate a gyro object
    Gyroscope = Gyro(gyro_addr)

    #Instantiate a controller object
    Kp = 2
    Kd = 0.008
    Ki = 0
    Controller = Control(Kp, Ki, Kd, 0, 600)

    #Initiate data
    Tilt = []
    Time_t = []
    Time_s = []
    Speed = []
    previous_error = 0
    error_integral = 0
    angle = 0
    init_time = time.time()
    

    r1 = time.time()
    while True:
        final_time = time.time()
        delta = final_time-init_time
        #Extract the value continuously
        try:
            angle = Gyroscope.get_Tilt(angle, delta, logging=False, reference_time=reference_time)
        except:
            print('[INFO] Could not fetch angle value')
            break

        
        speed.value, previous_error, error_integral = Controller.get_Actuation(angle, previous_error, error_integral, delta, logging=False, reference_time=reference_time)
        init_time = time.time()
        #Take action
        #print('reaction time in seconds: ',time.time()-r1)
        #Controller.Balance(speed,0.3)
        r1 = time.time()
        print(speed.value)
        #print(angle)

def Command(speed):
    commander = Commander()
    while True:
        try:
            
            commander.Balance(speed.value)

        except:
            print("[INFO] No speed input yet")
            
#Launch Multiprocessing
#Try livestreaming
speed = Value('d', 0.0)
p1 = multiprocessing.Process(target=MainLoop, args=(speed,))
p2 = multiprocessing.Process(target=Command, args=(speed,))
#p3 = multiprocessing.Process(target=LivePlot, args=['Data/Tilt.csv',0])
p1.start()
p2.start()
#p3.start()
#p3.join()
