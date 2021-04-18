import time
import sys
import os
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

#Instantiate a gyro object
Gyroscope = Gyro(gyro_addr)

#Instantiate a controller object
Kp = 1
Kd = 0
Ki = 0
Controller = Controller(Kp, Ki, Kd, -5, 600)


Tilt = []
Time_t = []
Time_s = []
Speed = []
figure, axis = plt.subplots(1, 2)
previous_error = 0
error_integral = 0
init_time = time.time()
##Write csv
with open('logs.csv','w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['angle','speed'])
while True:

    #Extract the value continuously
    try:
        angle = Gyroscope.get_Tilt()
    except:
        print('Could not fetch angle value')
        break
    
    #Plot it in a loop
    #Tilt, Time_t = livePlot(angle, Tilt, Time_t, figure,axis,0,'green')
    #Get the actuation signal
    final_time = time.time()
    delta = final_time-init_time
    #print(angle)
    stamp1 = time.time()
    speed, previous_error, error_integral = Controller.get_Actuation(angle, previous_error, error_integral, delta)
    stamp2 = time.time()
    #print('time to get the actuation is ', stamp2-stamp1, ' seconds')
    init_time = time.time()
    #print('the speed in rpm is ', speed)
    #Speed, Time_s = livePlot(speed, Speed, Time_s, figure,axis,1,'blue')
    
    #Take action
    Controller.Balance(speed, 0.05)
    #time.sleep(0.1)
    with open('logs.csv','a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([angle-5, speed])
