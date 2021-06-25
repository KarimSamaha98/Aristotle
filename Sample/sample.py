import time
import sys
import os
import multiprocessing
sys.path.append(os.getcwd())
import math 
from config.config import *
from Gyro.Gyro import Gyro
from Utils.Visualisation.Visual import *
from Control.PID import *
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
def MainLoop():

    #Instantiate a gyro object
    Gyroscope = Gyro(gyro_addr)

    #Instantiate a controller object
    Kp = 1.2
    Kd = 0
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



    while True:
        final_time = time.time()
        delta = final_time-init_time
        #Extract the value continuously
        try:
            angle = Gyroscope.get_Tilt(angle, delta, logging=True, reference_time=reference_time)
        except:
            print('[INFO] Could not fetch angle value')
            break

        
        speed, previous_error, error_integral = Controller.get_Actuation(angle, previous_error, error_integral, delta, logging=True, reference_time=reference_time)
        init_time = time.time()
        
        #Take action
        Controller.Balance(speed,0.05)

#Launch Multiprocessing
#Try livestreaming
p1 = multiprocessing.Process(target=MainLoop)
p2 = multiprocessing.Process(target=LivePlot, args=['Data/Gyroscope.csv',1])
p1.start()
p2.start()
p2.join()
