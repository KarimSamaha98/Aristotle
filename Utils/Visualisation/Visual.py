import csv
import random
import time

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


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
def GetData(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = )
        for row in csv_reader:
            print(row)

def Plot(X,Y, color = 'blue'):
    #Plots the arrays X and Y
    plt.cla()
    plt.plot(X,Y,color)
   
def LiveStream():
    #Plots live data
    ani = FuncAnimation(plt.gcf(), Plot, interval=1000)


#Test it out 
if __name__ == "__main__":
    GetData(filename = 'Data/gyro.csv')


    