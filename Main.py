from PCANBasic import *
import numpy as np
import time
from DBCParser import *


CAN_B = PCANBasic()



def setup(BUS_interface, PCAN_BAUD):
    result = CAN_B.Initialize(BUS_interface, PCAN_BAUD)

    if result == PCAN_ERROR_OK:
        print("Getstatus:-, ", CAN_B.GetStatus(BUS_interface), "-->initial success")
        print("hardware:-", CAN_B.GetValue(BUS_interface, PCAN_DEVICE_NUMBER))

        
def Online_Test(DBC_NAME):
    DBC = ParsingDBC(DBC_NAME)



if __name__ == '__main__':
    Online_Test("B-CAN")




