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

    try:
        x = 0
        plt.style.use('fivethirtyeight')

        x_val = []
        y_val = []

        index = count()
        while (True):
            status, R_msg, Time = em_CAN.Read(BUS_interface)

            if status == PCAN_ERROR_OK:
                if flag ==0:
                    first_time=Time.millis + Time.micros * 0.001
                    flag = 1

                time = (Time.millis + Time.micros * 0.001)-first_time
                i = 0
                data = ("{0}\t {1}\t {2}\t".format(time, hex(R_msg.ID), R_msg.LEN))

                datafull = []
                if ID == hex(R_msg.ID):
                    for i in range(0, R_msg.LEN):
                        data1 = str(bin(R_msg.DATA[i])[2:])
                        if len(data1) == 1:
                            data1 = str("000" + str(data1))
                        if len(data1) == 2:
                            data1 = str("00" + str(data1))
                        if len(data1) == 3:
                            data1 = str("0" + str(data1))
                        datafull.append(data1)
                        # print(data_field_tmp)
                    datafull = ''.join(datafull)

                    signalvalue = []
                    for i in range(SignalEnd):
                        signalvalue.append(datafull[SignalStart + i])
                    signalvalue = ''.join(signalvalue)
                    signalvalue = int(signalvalue, 2)

                    print(signalvalue)
