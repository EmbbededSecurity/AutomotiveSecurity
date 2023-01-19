# Abstract
It has been known that it is the most difficult to detect a masquerade attack that injects malicious messages by mimicking the original transmission periodicity and a data payload. 
There is no difference between normal and malicious messages when it comes to their transmission periodicity and the content of their data payload. 
Thus we open our datasets to the public to foster further car security research.

If you plan to use this data set for your own research, please cite:
...
@article{lee2022ttids,
  title={TTIDS: Transmission-resuming Time-based Intrusion Detection System for Controller Area Network (CAN)},
  author={Lee, Seyoung and Jo, Hyo Jin and Cho, Aram and Lee, Dong Hoon and Choi, Wonsuk},
  journal={IEEE Access},
  year={2022},
  publisher={IEEE}
}
...

# Dataset
We provide datasets which include masquerade attack with suspension attack through UDS services and Bus-off attack. 
Datasets were constructed by logging CAN traffic via the OBD-II port from a real vehicle while message injection attacks were performing.

 ＊Normal
    - Idling (about 40 min)
    - Driving (about 1.5 h)

 ＊Masquerade attack using UDS services:
   - Suspended ECU (Req ID: 0x7B7)
   - Masquerading CAN IDs: 0x48A, 0x48C, 0x58B

 ＊Masquerade attack using Bus-off attack
   - Bus-off target ID: 0x48A
   - Masquerading CAN IDs: 0x48A, 0x48C, 0x58B

# Data atttibutes (Timestamp, Arbitration_ID, DLC, Data, Class)
1. Timestamp: Recored time (ms)
2. CAN_ID: ID of CAN message in HEX (e.g., 0x153)
3. DLC: Number of data bytes, from 0 to 8
4. Data: data value (byte)
5. Class: Normal or Attack

By Emsec

