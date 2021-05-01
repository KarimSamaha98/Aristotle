import csv
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import sys
import os
sys.path.append(os.getcwd())
from Utils.Logging.Logging import *


def GetData(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter =',')
        counter = 0
        Data = []
        #Read Data into python lists
        for row in csv_reader:
            if counter == 0:
                #Extract the labels
                Labels = row
            else:
                Data.append(row)
            counter = counter + 1
        #Delete old content
        if counter > 1000:
            csv
        #Convert to numpy
        Data = np.array(Data, dtype=float)
        Label = np.array(Labels, dtype=str)
        #Process
        X = np.transpose(Data[:,0])
        Y = np.transpose(Data[:,1:])
        LabelX = Labels[0]
        LabelY = Labels[1:]
        

        return X,Y,LabelX,LabelY

def LivePlot(filename,  index=0):

    def Plot(i):
        #Plots the arrays X and Y
        plt.cla()
        X,Y,LabelX,LabelY = GetData(filename)
        plt.plot(X,Y[index])
        plt.xlabel(LabelX)
        plt.ylabel(LabelY[index])
        
    #Plots live data
    ani = FuncAnimation(plt.gcf(), Plot, interval=100)
    plt.show()



#Test it out 
if __name__ == "__main__":
        LivePlot('Data/gyroscope.csv',0)


    