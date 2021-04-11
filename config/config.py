#Configuration

##Enter set up parameters for stepper motors
CLK_M1 = 15 #CLK pin connected to pi for motor R
CW_M1 = 18 #CW pin connected to pi for motor R
CLK_M2 = 17 #CLK pin connected to pi for motor L
CW_M2 = 27 #CW pin connected to pi for motor R
degperstep=1.8 #Degrees per step of the stepper motor

##Setup Pin Modes
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(CLK_M1, GPIO.OUT) #CLK
    GPIO.setup(CW_M1, GPIO.OUT) #CW
    GPIO.setup(CLK_M2, GPIO.OUT) #CLK
    GPIO.setup(CW_M2, GPIO.OUT) #CW
except:
    print('[INFO] Could not setup GPIO pins')

##Gyroscope Address
gyro_addr = 0x68
try:
    sensor=mpu6050(gyro_addr)
except:
    print('[INFO] Could not setup gyroscope')
