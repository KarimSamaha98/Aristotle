import time
import random
import matplotlib.pyplot as plt

def livePlot(variable, Variable, Time):
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
    plt.plot(Time, Variable)
    plt.scatter(Time,Variable)

    #Func
    def namestr(obj, namespace):
        return [name for name in namespace if namespace[name] is obj]

    #Label
    plt.title("Plot of %s readings" % namestr(Variable, globals()))
    plt.xlabel('Time in s')
    plt.ylabel(namestr(Variable, globals()))

    #Draw
    plt.draw()
    plt.pause(0.05)

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