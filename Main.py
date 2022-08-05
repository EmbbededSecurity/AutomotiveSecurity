from PCANBasic import *
import numpy as np
import time
from DBCParser import *
import numpy as np
import matplotlib.pyplot as plt
from itertools import count
import csv
import pandas as pd
from matplotlib.animation import FuncAnimation

em_CAN = PCANBasic()



def setup(BUS_interface, PCAN_BAUD):
    result = em_CAN.Initialize(BUS_interface, PCAN_BAUD)

    if result == PCAN_ERROR_OK:
        print("Getstatus:-, ", em_CAN.GetStatus(BUS_interface), "-->initial success")
        print("hardware:-", em_CAN.GetValue(BUS_interface, PCAN_DEVICE_NUMBER))

def Plotting(signal):
    plt.style.use('fivethirtyeight')

    x_val = []
    y_val = []

    index = count()
    signal1 = signal








def Signal_Print(BUS_interface, PCAN_BAUD, ID, SignalStart, SignalEnd):
    flag=0
    result = em_CAN.Initialize(BUS_interface, PCAN_BAUD)
    ID = hex(ID)

    if result == PCAN_ERROR_OK:
        print("Getstatus:-, ", em_CAN.GetStatus(BUS_interface), "-->initial success")
        print("hardware:-", em_CAN.GetValue(BUS_interface, PCAN_DEVICE_NUMBER))

