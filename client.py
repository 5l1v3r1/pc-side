import sys
import time
from networktables import NetworkTables

# To see messages from networktables, you must setup logging
import logging
logging.basicConfig(level=logging.DEBUG)

ip = "192.168.1.104"

NetworkTables.initialize(server=ip)

sd = NetworkTables.getTable("datatable")

i = 0
while True:
    print('robotTime:', sd.getNumber('robotTime', 'N/A'))
    
    sd.putNumber('dsTime', i)
    # time.sleep(1)
    i += 1
