# AutomotiveSecurity

This is a Data Analyzer for CAN Bus protocols.

You can analyze the data based on .DBC files you already have or define the signals by yourself.

Please Download PCANBasic.py file to read the packets from CAN Bus by using PEAK's PCAN tools.

1. DBC Parser.py
- This code would help you to define Signal, IDs, Nodes and etc. followed by the .DBC files you offered.
- Pleased located .DBC files you have by naming it with the channel name under same folder.

2. Main.py
- Analyzing signal from CAN data by using signal information proposed by user/DBC files
    - Online Mode : Analyzing CAN Data received from PCAN tool by PEAK
    - Offline Mode : Analyzing CAN Data from log files

3. Tagging.py
- Transmitting CAN Data by tagging whether it is Attack or Normal data.


