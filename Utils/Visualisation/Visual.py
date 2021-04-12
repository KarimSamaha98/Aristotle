import time
import random
import matplotlib.pyplot as plt

def livePlot(variable, Variable, Time, figure, axis, number, Color):
    #Get intial time 
    if len(Variable) == 0:
        Time = []
        global reference_time
        reference_time = time.time()
    #Update data
    if len(Variable) > 100:
        Variable.pop(0)
        Time.pop(0)

    Variable.append(variable)
    Time.append(time.time() - reference_time)

    #Clear axis
    plt.gca().cla()

    #Plot
    axis[number].plot(Time, Variable,color=Color)
    axis[number].scatter(Time,Variable,color=Color)

    #Func
    def namestr(obj, namespace):
        return [name for name in namespace if namespace[name] is obj]

    #Label
    axis[number].set_title("Plot of %s readings" % namestr(Variable, globals()))
    axis[number].set_xlabel('Time in s')
    axis[number].set_ylabel(namestr(Variable, globals()))

    #Plot
    plt.draw()
    plt.pause(0.001)
    #Return
    return Variable, Time


#Test it out 
if __name__ == "__main__":
    fig = plt.figure(figsize=(12,6))
    Tilt = []
    Time = []
    for i in range(150):
        Tilt, Time = livePlot(random.randint(-5,5), Tilt, Time)
        time.sleep(1)