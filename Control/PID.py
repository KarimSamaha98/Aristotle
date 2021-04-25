from Motors.Motors import *
class Controller:
    def __init__(self, Kp, Ki, Kd, reference, treshhold):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.reference = reference
        self.treshhold = treshhold

    def get_Actuation(self, reading, previous_error, error_integral, delta):
        #params are the Kp, Ki, Kd parameters
        #output: actuation signals
        error = self.reference - reading
        if abs(error) < 1:
            error = 0
        print(error)
        print('e ,', error)
        #calculate the derivative
        error_derivative = (error - previous_error)/delta
        print('ed ,', error_derivative)
        #calculate the integral
        error_integral = ((error + previous_error)/2)*delta + error_integral
        print('ei ,', error_integral)
        #compute actuation signal
        actuation = self.Kp*error + self.Kd*error_derivative + self.Ki*error_integral
        #need to saturate the input
        #print(actuation)
        if abs(actuation)>self.treshhold:
            if actuation>0:
                actuation = self.treshhold
            else:
                actuation = -self.treshhold
        #return the actuation signal
        return actuation,error,error_integral

    def Balance(self, actuation, delta):
        init = time.time()
        if actuation < 0:
            print('[INFO] Moving Backwards')
            while(time.time()-init<delta):
                move_backward(abs(actuation))
                
        else:
            move_forward(abs(actuation))
            print('[INFO] Moving Forward')
            while(time.time()-init<delta):
                move_forward(abs(actuation))
