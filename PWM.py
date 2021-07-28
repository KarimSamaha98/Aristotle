from time import sleep
import pigpio
import RPi.GPIO as GPIO



CLK_M1 = 15 #CLK pin connected to pi for motor R
CW_M1 = 18 #CW pin connected to pi for motor R
CLK_M2 = 17 #CLK pin connected to pi for motor L
CW_M2 = 27 #CW pin connected to pi for motor R
degperstep=0.225 #Degrees per step of the stepper motor



#Using RPi.GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(CLK_M1,GPIO.OUT)
GPIO.setup(CW_M1,GPIO.OUT)
pwm1 = GPIO.PWM(CLK_M1,100)
GPIO.output(CW_M1,0)
pwm1.start(50)

GPIO.setup(CLK_M2,GPIO.OUT)
GPIO.setup(CW_M2,GPIO.OUT)
pwm2 = GPIO.PWM(CLK_M2,100)
GPIO.output(CW_M2,1)
pwm2.start(50)

for i in range(3000):
    pwm1.ChangeFrequency(i+1)
    pwm2.ChangeFrequency(i+1)
    print(i)

GPIO.output(CW_M2,0)
GPIO.output(CW_M1,1)

for i in range(1000):
    pwm1.ChangeFrequency(i+1)
    pwm2.ChangeFrequency(i+1)
    print(i)

for i in range(100):
    print(i)
    sleep(0.1)
    
pwm1.stop()
pwm2.stop()

# #Connect to pigpio
# pi2 = pigpio.pi()
# pi2.set_PWM_dutycycle(CLK_M1, 128)
# pi2.set_PWM_dutycycle(CLK_M2, 128)
# #pi2.set_PWM_frequency(CLK_M1,2000)
# pi2.write(CW_M1, 1)
# pi2.write(CW_M2, 1)
# for i in range(2000):
#     pi2.set_PWM_frequency(CLK_M1,i)
#     pi2.set_PWM_frequency(CLK_M2,i)
#     print(i)
#     sleep(0.01)
# pi2.set_PWM_dutycycle(CLK_M1,0)
# pi2.set_PWM_dutycycle(CLK_M2,0)
