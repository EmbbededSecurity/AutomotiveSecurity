import glob
import re
import pandas as pd
import math
from PCANBasic import *
import numpy as np
import time
from DBCParser import *
import numpy as np
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation
from random import randrange
import csv

def Logging(ID_IN,time, time_end, SignalStart, SignalLength):
    f = open('D:\\현대자동차 과제\\IDLE\\C-CAN(Idle) Messages File2.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    time=float(time)
    time_end = float(time_end)
    SignalEnd = SignalStart+SignalLength
    pt=[]
    for line in rdr:
        try:
            v= float(line[1])
            if time_end > v > time:
                ID =("0x"+str(line[9]))
                ID = int(ID,16)
                ID=hex(ID)
                ID_IN=int(ID_IN,16)
                ID_IN=hex(ID_IN)
                data=[]
                dlc = 0
                for x in line[12:-1]:
                    if x != '':
                        dlc += 1
                        x= bin(int(x,16))[2:]
                        if len(x) == 1:
                            x = "0000000"+x
                        elif len(x) == 2:
                            x = "000000"+x
                        elif len(x) == 3:
                            x = "00000"+x
                        elif len(x) == 4:
                            x = "0000"+x
                        elif len(x) == 5:
                            x = "000"+x
                        elif len(x) == 6:
                            x = "00"+x
                        elif len(x) == 7:
                            x = "0"+x
                        data.append(x)
                data = ''.join(data)

                # ID_IN = str(ID_IN)
                # ID = str(ID)
                SignalStart=int(SignalStart)
                SignalEnd=int(SignalEnd)
                if ID_IN == ID:
                    #print(int(data[SignalStart:SignalEnd],2))
                    pt.append(int(data[SignalStart:SignalEnd],2))






        except:
            1==1
    plt.plot(pt)
    plt.show()


    f.close()








def Signal_Print(BUS_interface, PCAN_BAUD, ID, SignalStart, SignalEnd):
    flag=0
    em_CAN = PCANBasic()
    result = em_CAN.Initialize(BUS_interface, PCAN_BAUD)
    fig = plt.figure(figsize=(6, 3))
    x_val = [0]
    y_val = [0]

    ln, = plt.plot(x_val, y_val, '-')
    # ID = hex(ID)

    if result == PCAN_ERROR_OK:
        print("Getstatus:-, ", em_CAN.GetStatus(BUS_interface), "-->initial success")
        print("hardware:-", em_CAN.GetValue(BUS_interface, PCAN_DEVICE_NUMBER))

    try:
        x = 0
        plt.style.use('fivethirtyeight')

        # x_val = []
        # y_val = []

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


                datafull=[]
                if hex(ID) == hex(R_msg.ID):
                    for i in range(0, R_msg.LEN):
                        data1= str(bin(R_msg.DATA[i])[2:])
                        if len(data1) == 1:
                                data1 = str("000"+str(data1))
                        if len(data1) == 2:
                                data1 = str("00"+str(data1))
                        if len(data1) == 3:
                                data1 = str("0"+str(data1))
                        datafull.append(data1)
                        #print(data_field_tmp)
                    datafull=''.join(datafull)

                    signalvalue=[]
                    for i in range(SignalEnd):
                        signalvalue.append(datafull[SignalStart+i])
                    signalvalue=''.join(signalvalue)
                    signalvalue = int(signalvalue,2)
                    #print(signalvalue)
                    print(time)
                    def update(frame):
                        x_val.append(x_val[-1] + 1)
                        y_val.append(signalvalue)
                        #print(time)

                        ln.set_data(x_val, y_val)
                        fig.gca().relim()
                        fig.gca().autoscale_view()
                        return ln,
                    animation = FuncAnimation(fig, update, interval=1)
                    plt.show()

    except:
        print("No")
# Finding variables by using regular expression(Regex)
MessageID = re.compile("BO_\s\d+")
MessageName = re.compile("BO_\s\d+\s\w+\w+\w+")
Message = re.compile("BO_\s\d+\s\w+\w+\w+" + ":")
dlc = re.compile("BO_\s\d+\s\w+\w+\w+" + ":" + "\s\d+")
Node = re.compile("BO_\s\d+\s\w+\w+\w+" + ":" + "\s\d+" + "\s\w+")
Signal = re.compile("SG_\s\S+\s" + ":" + "\s+\d+" + "\|" + "\d+" + "@")
Signal2 = re.compile("SG_\s\S+\s" + ":" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(" + "\S+,\S+" + "\)" + "\s"+"\["+"\S+" + "\|"+"\S+")
Signal3 = re.compile("SG_\s\S+\s" + ":" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(" + "\S+,\S+" + "\)" + "\s"+"\["+"\S+" + "\|")
Signal4 = re.compile("SG_\s\S+\s" + ":" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(" + "\S+,\S+" + "\)" + "\s"+"\["+"\S+")
Signal5 = re.compile("SG_\s\S+\s" + ":" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(" + "\S+,\S+" + "\)" + "\s"+"\[")
Signal6 = re.compile("SG_\s\S+\s" + ":" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(" + "\S+,\S+")
Signal7 = re.compile("SG_\s\S+\s" + ":" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(" + "\S+,")
Signal8 = re.compile("SG_\s\S+\s" + ":" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(" + "\S+")
Signal9 = re.compile("SG_\s\S+\s" + ":" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(")
Signed = re.compile("SG_\s\S+\s" + ":" + "\s+\d+" + "\|" + "\d+" + "@" + "\S+"+"\s\(")
Signed1 = re.compile("SG_\s\S+\s" + ":" + "\s+\d+" + "\|" + "\d+" + "@")
Signal10 = re.compile("SG_\s\S+\s" + ":" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+")
Periodic_ID = re.compile("CM_\sBO_\s\d+\s" + "\"" + "\[P]")
Periodic_Event_ID = re.compile("CM_\sBO_\s\d+\s" + "\"" + "\[PE]")
Event_ID = re.compile("CM_\sBO_\s\d+\s" + "\"" + "\[E]")
Frequency_Full = re.compile("BA_ " + "\"" + "GenMsgCycleTime" + "\"" + " BO_" + " \d+ " + "\d+")
Frequency = re.compile("BA_ " + "\"" + "GenMsgCycleTime" + "\"" + " BO_" + " \d+")
whyrano = re.compile("SG_" + "\s\S+Counter\s" + ":" + "\s\d+" + "\|" + "\d+")
whyrano_a = re.compile("SG_" + "\s\S+Counter\s" + ":" + "\s\d+" + "\|")
whyrano_b = re.compile("SG_" + "\s\S+Counter\s" + ":" + "\s\d+")
whyrano_c = re.compile("SG_" + "\s\S+Counter\s" + ":" + "\s")
whyrano1 = re.compile("SG_" + "\s\S+Counter\w+\s" + ":" + "\s\d+" + "\|" + "\d+")
whyrano1_a = re.compile("SG_" + "\s\S+Counter\w+\s" + ":" + "\s\d+" + "\|")
whyrano1_b = re.compile("SG_" + "\s\S+Counter\w+\s" + ":" + "\s\d+")
whyrano1_c = re.compile("SG_" + "\s\S+Counter\w+\s" + ":" + "\s")
whyrano2 = re.compile("SG_" + "\s\S+Cnt\d+\s" + ":" + "\s\d+" + "\|" + "\d+")
whyrano2_a = re.compile("SG_" + "\s\S+Cnt\d+\s" + ":" + "\s\d+" + "\|")
whyrano2_b = re.compile("SG_" + "\s\S+Cnt\d+\s" + ":" + "\s\d+")
whyrano2_c = re.compile("SG_" + "\s\S+Cnt\d+\s" + ":" + "\s")
whyrano3 = re.compile("SG_" + "\s\S+Cnt\s" + ":" + "\s\d+" + "\|" + "\d+")
whyrano3_a = re.compile("SG_" + "\s\S+Cnt\s" + ":" + "\s\d+" + "\|")
whyrano3_b = re.compile("SG_" + "\s\S+Cnt\s" + ":" + "\s\d+")
whyrano3_c = re.compile("SG_" + "\s\S+Cnt\s" + ":" + "\s")
whyrano4 = re.compile("SG_" + "\s\S+Cnt\w+\s" + ":" + "\s\d+" + "\|" + "\d+")
whyrano4_a = re.compile("SG_" + "\s\S+Cnt\w+\s" + ":" + "\s\d+" + "\|")
whyrano4_b = re.compile("SG_" + "\s\S+Cnt\w+\s" + ":" + "\s\d+")
whyrano4_c = re.compile("SG_" + "\s\S+Cnt\w+\s" + ":" + "\s")
whyrano5 = re.compile("SG_" + "\s\S+CNT\w+\s" + ":" + "\s\d+" + "\|" + "\d+")
whyrano5_a = re.compile("SG_" + "\s\S+CNT\w+\s" + ":" + "\s\d+" + "\|")
whyrano5_b = re.compile("SG_" + "\s\S+CNT\w+\s" + ":" + "\s\d+")
whyrano5_c = re.compile("SG_" + "\s\S+CNT\w+\s" + ":" + "\s")
whyrano6 = re.compile("SG_" + "\s\S+Count\d+\s" + ":" + "\s\d+" + "\|" + "\d+")
whyrano6_a = re.compile("SG_" + "\s\S+Count\d+\s" + ":" + "\s\d+" + "\|")
whyrano6_b = re.compile("SG_" + "\s\S+Count\d+\s" + ":" + "\s\d+")
whyrano6_c = re.compile("SG_" + "\s\S+Count\d+\s" + ":" + "\s")
whyrano7 = re.compile("SG_" + "\s\S+" + "Count\s" + ":" + "\s\d+" + "\|" + "\d+")
whyrano7_a = re.compile("SG_" + "\s\S+" + "Count\s" + ":" + "\s\d+" + "\|")
whyrano7_b = re.compile("SG_" + "\s\S+" + "Count\s" + ":" + "\s\d+")
whyrano7_c = re.compile("SG_" + "\s\S+" + "Count\s" + ":" + "\s")
Signa = re.compile("SG_\s\S+\s" + ":" + "\s+\d+" + "\|" + "\d+")
Sign = re.compile("SG_\s\S+\s" + ":" + "\s+\d+" + "\|")
Sig = re.compile("SG_\s\S+\s" + ":" + "\s+\d+")
Si = re.compile("SG_\s\S+\s" + ":" + "\s+")
Signal_m = re.compile("SG_\s\S+\s\w+" + "\s:" + "\s+" + "|" + "\s+" + "@")
Signa_m = re.compile("SG_\s\S+\s\w+" + "\s:" + "\s+\d+" + "\|" + "\d+")
Sign_m = re.compile("SG_\s\S+\s\w+" + "\s:" + "\s+\d+" + "\|")
Sig_m = re.compile("SG_\s\S+\s\w+" + "\s:" + "\s+\d+")
Si_m = re.compile("SG_\s\S+\s\w+" + "\s:" + "\s+")
Signalm2 = re.compile("SG_\s\S+\s\S+" + "\s:" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(" + "\S+\,\S+" + "\)" + "\s\[\S+" + "\|\S+")
Signalm3 = re.compile( "SG_\s\S+\s\S+" + "\s:" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(" + "\S+\,\S+" + "\)" + "\s\[\S+" + "\|")
Signalm4 = re.compile("SG_\s\S+\s\S+" + "\s:" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(" + "\S+\,\S+" + "\)" + "\s\[\S+")
Signalm5 = re.compile("SG_\s\S+\s\S+" + "\s:" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(" + "\S+\,\S+" + "\)" + "\s\[")
Signalm6 = re.compile("SG_\s\S+\s\S+" + "\s:" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(" + "\S+\,\S+")
Signalm7 = re.compile("SG_\s\S+\s\S+" + "\s:" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(" + "\S+\,")
Signalm8 = re.compile("SG_\s\S+\s\S+" + "\s:" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(" + "\S+")
Signalm9 = re.compile("SG_\s\S+\s\S+" + "\s:" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+" + "\S\s+" + "\(")
Signalm10 = re.compile("SG_\s\S+\s\S+" + "\s:" + "\s+\d+" + "\|" + "\d+" + "@" + "\d+")
Mulcode = re.compile("SG_\s\S+\s" + "m\d+")
mulcode = re.compile("SG_\s\S+\s" + "m")
Mulcode_Position = re.compile("SG_ MUL_CODE\s\S?\s?:\s\d+\|\d+")
Mulcode_Position1 = re.compile("SG_ MUL_CODE\s\S?\s?:\s\d+\|")
Mulcode_Position2 = re.compile("SG_ MUL_CODE\s\S?\s?:\s")




a = {}
b = {}
b['ID'] = []
b['channel'] = []
b['name'] = []
b['dlc'] = []
b['node'] = []
b['# of signals'] = []

invert = [7, 6, 5, 4, 3, 2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8, 23, 22, 21, 20, 19, 18, 17, 16, 31, 30, 29, 28, 27, 26,
          25, 24, 39, 38, 37, 36, 35, 34, 33, 32, 47, 46, 45, 44, 43, 42, 41, 40, 55, 54, 53, 52, 51, 50, 49, 48, 63,
          62, 61, 60, 59, 58, 57, 56]
outputpath = 'C:\\Users\MASON\Desktop\DBC\\'
sep = 1  # int(input("1:sperate 2:total"))
ID_copy = 0

# 폴더내의 모든 dbc 파일을 대상으로 작업 가능




def ParsingDBC(channel,IDin,Flag):
    for i in glob.glob(r'C:\Users\MASON\Desktop\DBC\*.dbc'):
        with open(i, 'r') as f:
            IDlist = []
            Signalname_List = []
            new_ID_list = []
            idx = -1
            signal = [0]
            Check_List = []
            cID_list = []
            cname_list = []
            nname_list = []
            DLC_list = []
            node_list = []
            Period_List = []
            PeriodEvent_List = []
            Event_List = []
            ID_Counter = []
            Counterplus = []
            Leng_List = []
            Startbit_List = []
            Frequency_Dict = {}
            big_list = []
            Check_List = []
            Big_check = []
            Count_Num = []
            NumofMulMsgs = []
            MultiCodeID = []
            MultiCodeList = []
            MultiCodeStart = []
            MultiCodeLeng = []
            Allmsgs = []
            IsMulti = []
            NumCounters = []
            Signalmsglist = []
            SignalMaxlist = []
            SignalMinlist = []
            SignalStart = []
            SignalLen = []
            Signalnummsgs = []
            MultiCode_Start =[]
            MultiCode_Leng = []
            new_allmsg=[]
            new_signal=[]
            test_couter=[]
            Multi_SignalMaxlist = []
            Multi_SignalMinlist = []
            Multi_SignalStart = []
            Multi_SignalLen = []
            SignalRange =[]
            SignalRange1=[]
            SignalSame=[]

            flag = 0
            sum1 = 0
            end = 0
            Sum = 0
            start1 = 0
            start = 0
            Signal_flag = 0
            IDlist.clear()
            Period_List.clear()
            ID_Counter.clear

            end1 = 0

            if sep == 1:
                fname = i.replace(".dbc", "")
                sepf = open("%s.txt" % (fname), 'w')
                iu = 0

            # if sep == 2:
            # tot.write(i)
            # tot.write('\n')
            for x, y in enumerate(f.readlines(), 1):
                # Find Regex among read line.
                MIDSearch = MessageID.search(y)
                MNameSearch = MessageName.search(y)
                MSearch = Message.search(y)
                DLCSearch = dlc.search(y)
                NODESearch = Node.search(y)
                SignalSearch = Signal.search(y)
                PeriodicSearch = Periodic_ID.search(y)
                Periodic_EventSearch = Periodic_Event_ID.search(y)
                EventSearch = Event_ID.search(y)
                Frequency_FullSearch = Frequency_Full.search(y)
                FrequencySearch = Frequency.search(y)
                whyranoSearch = whyrano.search(y)
                whyrano_aSearch = whyrano_a.search(y)
                whyrano_bSearch = whyrano_b.search(y)
                whyrano_cSearch = whyrano_c.search(y)
                whyrano1Search = whyrano1.search(y)
                whyrano1Search = whyrano.search(y)
                whyrano1_aSearch = whyrano1_a.search(y)
                whyrano1_bSearch = whyrano1_b.search(y)
                whyrano1_cSearch = whyrano1_c.search(y)
                whyrano1Search = whyrano1.search(y)
                SignaSearch = Signa.search(y)
                SignSearch = Sign.search(y)
                SigSearch = Sig.search(y)
                SiSearch = Si.search(y)
                whyrano2_aSearch = whyrano2_a.search(y)
                whyrano2_bSearch = whyrano2_b.search(y)
                whyrano2_cSearch = whyrano2_c.search(y)
                whyrano2Search = whyrano2.search(y)
                whyrano3_aSearch = whyrano3_a.search(y)
                whyrano3_bSearch = whyrano3_b.search(y)
                whyrano3_cSearch = whyrano3_c.search(y)
                whyrano3Search = whyrano3.search(y)
                whyrano4_aSearch = whyrano4_a.search(y)
                whyrano4_bSearch = whyrano4_b.search(y)
                whyrano4_cSearch = whyrano4_c.search(y)
                whyrano4Search = whyrano4.search(y)
                whyrano5_aSearch = whyrano5_a.search(y)
                whyrano5_bSearch = whyrano5_b.search(y)
                whyrano5_cSearch = whyrano5_c.search(y)
                whyrano5Search = whyrano5.search(y)
                whyrano6_aSearch = whyrano6_a.search(y)
                whyrano6_bSearch = whyrano6_b.search(y)
                whyrano6_cSearch = whyrano6_c.search(y)
                whyrano6Search = whyrano6.search(y)
                whyrano7_aSearch = whyrano7_a.search(y)
                whyrano7_bSearch = whyrano7_b.search(y)
                whyrano7_cSearch = whyrano7_c.search(y)
                whyrano7Search = whyrano7.search(y)
                Signal_mSearch = Signal_m.search(y)
                Signa_mSearch = Signa_m.search(y)
                Sign_mSearch = Sign_m.search(y)
                Sig_mSearch = Sig_m.search(y)
                Si_mSearch = Si_m.search(y)
                SignedSearch = Signed.search(y)
                Signed1Search = Signed1.search(y)
                Signal2Search = Signal2.search(y)
                Signal3Search = Signal3.search(y)
                Signal4Search = Signal4.search(y)
                Signal5Search = Signal5.search(y)
                Signal6Search = Signal6.search(y)
                Signal7Search = Signal7.search(y)
                Signal8Search = Signal8.search(y)
                Signal9Search = Signal9.search(y)
                Signal10Search = Signal10.search(y)
                Signalm2Search = Signalm2.search(y)
                Signalm3Search = Signalm3.search(y)
                Signalm4Search = Signalm4.search(y)
                Signalm5Search = Signalm5.search(y)
                Signalm6Search = Signalm6.search(y)
                Signalm7Search = Signalm7.search(y)
                Signalm8Search = Signalm8.search(y)
                Signalm9Search = Signalm9.search(y)
                Signalm10Search = Signalm10.search(y)
                MulcodeSearch = Mulcode.search(y)
                mulcodesearch = mulcode.search(y)
                Mulcode_PositionSearch = Mulcode_Position.search(y)
                Mulcode_Position1Search = Mulcode_Position1.search(y)
                Mulcode_Position2Search = Mulcode_Position2.search(y)



                # 주기 탐색 부분

                if Frequency_FullSearch and FrequencySearch:
                    FREQF = Frequency_FullSearch.group()
                    FREQ = FrequencySearch.group()
                    FREQID = hex(int(FREQ.replace("BA_ \"GenMsgCycleTime\" BO_ ", "")))
                    FREQT = int(FREQF.replace(FREQ, ""))
                    Frequency_Dict[FREQID] = FREQT
                # 주기 아이디 검색
                if PeriodicSearch:
                    PERIOD = PeriodicSearch.group()
                    PID = PERIOD.replace("CM_ BO_ ", "")
                    PID = hex(int(PID.replace(" \"[P]", "")))
                    Period_List.append(PID)
                # 주기/이벤트 아이디 검색
                if Periodic_EventSearch:
                    PERIOD = Periodic_EventSearch.group()
                    PID = PERIOD.replace("CM_ BO_ ", "")
                    PID = hex(int(PID.replace(" \"[PE]", "")))
                    PeriodEvent_List.append(PID)
                # 이벤트 아이디 검색
                if EventSearch:
                    EVENT = EventSearch.group()
                    EID = EVENT.replace("CM_ BO_ ", "")
                    EID = hex(int(EID.replace(" \"[E]", "")))
                    Event_List.append(EID)
                # 모든 아이디를 검색하는 부분
                if sep == 1 and MIDSearch and MNameSearch and MSearch and DLCSearch:
                    MID = MIDSearch.group()
                    MNAME = MNameSearch.group()
                    MESSAGE = MSearch.group()
                    DLC = DLCSearch.group()
                    NODE = NODESearch.group()
                    fp = 0
                    m = 0
                    mstart = 0
                    start = 0
                    SIGNA_m = 0
                    sig_max = 0
                    sig_min = 0
                    iu = 0
                    signal.append(0)
                    SignalMaxlist.append([])
                    SignalMinlist.append([])
                    SignalStart.append([])
                    Signalname_List.append([])
                    SignalLen.append([])

                    num = int(MID.replace("BO_ ", ""))
                    nname = str(MNAME.replace(MID, ""))
                    cname = fname.replace(outputpath, "")
                    dlc2 = int(DLC.replace(MESSAGE, ""))
                    node = str(NODE.replace(DLC, ""))
                    ID = hex(num)
                    if ID not in cID_list:
                        IDlist.append(ID)
                        cID_list.append(ID)
                        cname_list.append(cname)
                        nname_list.append(nname)
                        DLC_list.append(dlc2)
                        node_list.append(node)
                        flag += 1
                # 아이디 검색후 밑에 나오는 시그널 부분 파싱
                elif Signal_mSearch and flag >= 1 and SignedSearch:

                    sum1 = Sum
                    end1 = end
                    iu = iu + 1
                    sig_max1 = sig_max
                    sig_min1 = sig_min
                    signal[flag - 1] = iu
                    signa1 = SIGNA_m
                    SIGNA_m = Signa_mSearch.group()
                    SIGN_m = Sign_mSearch.group()
                    SIG_m = Sig_mSearch.group()
                    SI_m = Si_mSearch.group()
                    end = int(SIGNA_m.replace(SIGN_m, ""))
                    start = int(SIG_m.replace(SI_m, ""))
                    Sum = start + end
                    sum2 = (sum1)
                    s = cID_list.index(ID)
                    c_dlc = (DLC_list[s] * 8)
                    sigidx = IDlist.index(ID)
                    sig = Signalm2Search.group()
                    sig2 = Signalm3Search.group()
                    sig3 = Signalm5Search.group()
                    sig4 = Signalm6Search.group()
                    sig5 = Signalm7Search.group()
                    sig6 = Signalm9Search.group()
                    Signedval = SignedSearch.group()
                    Signedval1 = Signed1Search.group()
                    Signedval = Signedval.replace(Signedval1,"")
                    Signedval = Signedval.replace(" (","")
                    sig_max = float((sig.replace(sig2, "")).replace("]", ""))
                    if Signedval == "1-":
                        sig_min = 0
                    else :
                        sig_min = float((sig2.replace(sig3, "")).replace("|", ""))
                    offset = float((sig4.replace(sig5, "")).replace(")", ""))
                    factor = float((sig5.replace(sig6, "")).replace(",", ""))
                    sig_max = math.ceil((sig_max - offset) / factor)
                    sig_min = math.ceil((sig_min - offset) / factor)



                    if (start == start1) and (fp != 0):
                        Multi_SignalStart.append(start)
                        Multi_SignalLen.append(end)
                        Multi_SignalMinlist.append(sig_min1)
                        Multi_SignalMaxlist.append(sig_max1)




                    else:
                        SignalStart[sigidx].append(start)
                        Signalname_List[sigidx].append(SI_m)
                        SignalLen[sigidx].append(end)
                        SignalMinlist[sigidx].append(sig_min)
                        SignalMaxlist[sigidx].append(sig_max)

                    if MulcodeSearch:
                        mul1 = MulcodeSearch.group()
                        mul2 = mulcodesearch.group()
                        MultiCode = mul1.replace(mul2, "")
                        if ID not in MultiCodeID:
                            MultiCodeID.append(ID)
                            MultiCodeList.append([])

                        MultiCodeList[MultiCodeID.index(ID)].append(int(MultiCode))


                elif SignalSearch and Signal2Search and flag >= 1 and SignedSearch:
                    sum1 = Sum
                    end1 = end
                    start1 = start
                    sig_max1 = sig_max
                    sig_min1 = sig_min
                    iu = iu + 1
                    signal[flag - 1] = iu
                    SIGNA = SignaSearch.group()
                    SIGN = SignSearch.group()
                    SIG = SigSearch.group()
                    SI = SiSearch.group()
                    signal2 = Signal2Search.group()
                    end = int(SIGNA.replace(SIGN, ""))
                    start = int(SIG.replace(SI, ""))
                    Sum = start + end
                    sum2 = (sum1)
                    s = cID_list.index(ID)
                    c_dlc = (DLC_list[s] * 8)
                    sigidx = IDlist.index(ID)+Signal_flag
                    sig = Signal2Search.group()
                    sig2 = Signal3Search.group()
                    sig3 = Signal5Search.group()
                    sig4 = Signal6Search.group()
                    sig5 = Signal7Search.group()
                    sig6 = Signal9Search.group()
                    Signedval = SignedSearch.group()
                    Signedval1 = Signed1Search.group()
                    Signedval = Signedval.replace(Signedval1,"")
                    Signedval = Signedval.replace(" (","")
                    sig_max = float((sig.replace(sig2, "")).replace("]", ""))
                    if Signedval == "1-":
                        sig_min = 0
                    else :
                        sig_min = float((sig2.replace(sig3, "")).replace("|", ""))
                    offset = float((sig4.replace(sig5, "")).replace(")", ""))
                    factor = float((sig5.replace(sig6, "")).replace(",", ""))
                    sig_max = math.ceil((sig_max - offset) / factor)
                    sig_min = math.ceil((sig_min - offset) / factor)



                    #멀티 시그널 검색
                    if (start == start1) and (fp != 0):
                        Multi_SignalStart.append(start)
                        Multi_SignalLen.append(end)
                        Multi_SignalMinlist.append(sig_min)
                        Multi_SignalMaxlist.append(sig_max)
                    else:
                        SignalStart[sigidx].append(start)
                        Signalname_List[sigidx].append(SI)
                        SignalLen[sigidx].append(end)
                        SignalMinlist[sigidx].append(sig_min)
                        SignalMaxlist[sigidx].append(sig_max)




                if Mulcode_PositionSearch:
                    MP = Mulcode_PositionSearch.group()
                    MP1 = Mulcode_Position1Search.group()
                    MP2 = Mulcode_Position2Search.group()
                    Multi_leng = MP.replace(MP1, "")
                    Multi_Start = MP1.replace(MP2, "")
                    Multi_Start = Multi_Start.replace("|", "")
                    if ID in MultiCodeID:
                        MultiCode_Start.append(Multi_Start)
                        MultiCode_Leng.append(Multi_leng)


                # 카운터 파싱 각각 다른 정규식 표현으로 파싱해서 Counter 리스트에 추가
                if whyranoSearch:
                    COUNTER = whyranoSearch.group()
                    a = whyrano_aSearch.group()
                    b = whyrano_bSearch.group()
                    c = whyrano_cSearch.group()
                    Leng = COUNTER.replace(a, "")
                    Startbit = b.replace(c, "")


                    if ID not in ID_Counter:
                        Count_Num.append(0)
                        ID_Counter.append(ID)
                        Leng_List.append(Leng)
                        Startbit_List.append(Startbit)
                    elif ID in ID_Counter:
                        ci = ID_Counter.index(ID)
                        Count_Num[ci] += 1
                        if Count_Num[ci] > 0:
                            ID_Counter.append(ID)
                            Leng_List.append(Leng)
                            Startbit_List.append(Startbit)
                            Counterplus.append(ID)



                elif whyrano1Search:
                    COUNTER = whyrano1Search.group()
                    a = whyrano1_aSearch.group()
                    b = whyrano1_bSearch.group()
                    c = whyrano1_cSearch.group()
                    Leng = COUNTER.replace(a, "")
                    Startbit = b.replace(c, "")

                    if ID not in ID_Counter:
                        Count_Num.append(0)
                        ID_Counter.append(ID)
                        Leng_List.append(Leng)
                        Startbit_List.append(Startbit)
                    elif ID in ID_Counter:
                        ci = ID_Counter.index(ID)
                        Count_Num[ci] += 1
                        if Count_Num[ci] > 0:
                            ID_Counter.append(ID)
                            Leng_List.append(Leng)
                            Startbit_List.append(Startbit)
                            Counterplus.append(ID)





                elif whyrano2Search:
                    COUNTER = whyrano2Search.group()
                    a = whyrano2_aSearch.group()
                    b = whyrano2_bSearch.group()
                    c = whyrano2_cSearch.group()
                    Leng = COUNTER.replace(a, "")
                    Startbit = b.replace(c, "")

                    if ID not in ID_Counter:
                        Count_Num.append(0)
                        ID_Counter.append(ID)
                        Leng_List.append(Leng)
                        Startbit_List.append(Startbit)
                    elif ID in ID_Counter:
                        ci = ID_Counter.index(ID)
                        Count_Num[ci] += 1
                        if Count_Num[ci] > 0:
                            ID_Counter.append(ID)
                            Leng_List.append(Leng)
                            Startbit_List.append(Startbit)
                            Counterplus.append(ID)



                elif whyrano3Search:
                    COUNTER = whyrano3Search.group()
                    a = whyrano3_aSearch.group()
                    b = whyrano3_bSearch.group()
                    c = whyrano3_cSearch.group()
                    Leng = COUNTER.replace(a, "")
                    Startbit = b.replace(c, "")

                    if ID not in ID_Counter:
                        Count_Num.append(0)
                        ID_Counter.append(ID)
                        Leng_List.append(Leng)
                        Startbit_List.append(Startbit)
                    elif ID in ID_Counter:
                        ci = ID_Counter.index(ID)
                        Count_Num[ci] += 1
                        if Count_Num[ci] > 0:
                            ID_Counter.append(ID)
                            Leng_List.append(Leng)
                            Startbit_List.append(Startbit)
                            Counterplus.append(ID)



                elif whyrano4Search:
                    COUNTER = whyrano4Search.group()
                    a = whyrano4_aSearch.group()
                    b = whyrano4_bSearch.group()
                    c = whyrano4_cSearch.group()
                    Leng = COUNTER.replace(a, "")
                    Startbit = b.replace(c, "")

                    if ID not in ID_Counter:
                        Count_Num.append(0)
                        ID_Counter.append(ID)
                        Leng_List.append(Leng)
                        Startbit_List.append(Startbit)
                    elif ID in ID_Counter:
                        ci = ID_Counter.index(ID)
                        Count_Num[ci] += 1
                        if Count_Num[ci] > 0:
                            ID_Counter.append(ID)
                            Leng_List.append(Leng)
                            Startbit_List.append(Startbit)
                            Counterplus.append(ID)



                elif whyrano5Search:
                    COUNTER = whyrano5Search.group()
                    a = whyrano5_aSearch.group()
                    b = whyrano5_bSearch.group()
                    c = whyrano5_cSearch.group()
                    Leng = COUNTER.replace(a, "")
                    Startbit = b.replace(c, "")

                    if ID not in ID_Counter:
                        Count_Num.append(0)
                        ID_Counter.append(ID)
                        Leng_List.append(Leng)
                        Startbit_List.append(Startbit)
                    elif ID in ID_Counter:
                        ci = ID_Counter.index(ID)
                        Count_Num[ci] += 1
                        if Count_Num[ci] > 0:
                            ID_Counter.append(ID)
                            Leng_List.append(Leng)
                            Startbit_List.append(Startbit)
                            Counterplus.append(ID)



                elif whyrano6Search:
                    COUNTER = whyrano6Search.group()
                    a = whyrano6_aSearch.group()
                    b = whyrano6_bSearch.group()
                    c = whyrano6_cSearch.group()
                    Leng = COUNTER.replace(a, "")
                    Startbit = b.replace(c, "")

                    if ID not in ID_Counter:
                        Count_Num.append(0)
                        ID_Counter.append(ID)
                        Leng_List.append(Leng)
                        Startbit_List.append(Startbit)
                    elif ID in ID_Counter:
                        ci = ID_Counter.index(ID)
                        Count_Num[ci] += 1
                        if Count_Num[ci] > 0:
                            ID_Counter.append(ID)
                            Leng_List.append(Leng)
                            Startbit_List.append(Startbit)
                            Counterplus.append(ID)



                elif whyrano7Search:
                    COUNTER = whyrano7Search.group()
                    a = whyrano7_aSearch.group()
                    b = whyrano7_bSearch.group()
                    c = whyrano7_cSearch.group()
                    Leng = COUNTER.replace(a, "")
                    Startbit = b.replace(c, "")

                    if ID not in ID_Counter:
                        Count_Num.append(0)
                        ID_Counter.append(ID)
                        Leng_List.append(Leng)
                        Startbit_List.append(Startbit)
                    elif ID in ID_Counter:
                        ci = ID_Counter.index(ID)
                        Count_Num[ci] += 1
                        if Count_Num[ci] > 0:
                            ID_Counter.append(ID)
                            Leng_List.append(Leng)
                            Startbit_List.append(Startbit)
                            Counterplus.append(ID)

            del signal[-1]



            if channel == cname:
                #IDin=hex(int(IDin))
                index = IDlist.index(IDin)
                print(IDin + " has " + str(len(SignalStart[index])) +" Singnals")
                for i in range(len(Signalname_List[index])):
                    print(str(i+1)+" : "+ Signalname_List[index][i])
                SN = int(input("Please enter Signal Number "))
                SS= int(SignalStart[index][SN])
                SL = int(SignalLen[index][SN])
                if Flag == 1:
                    Signal_Print(PCAN_USBBUS1,PCAN_BAUD_500K,IDin,SS,SL)
                elif Flag == 2:
                    T = input("Time Start")
                    TE = input("Time End")
                    Logging(IDin,T,TE,SS,SL)



if __name__ == '__main__':
    Signal_Print(PCAN_USBBUS1,PCAN_BAUD_500K, 0x163, 10, 20)
    #ParsingDBC("C-CANN",0x2B0,2)