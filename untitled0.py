import time
from networktables import NetworkTables

from playsound import playsound

import logging
logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize()
sd = NetworkTables.getTable("datatable")

tyme = 111

while True:
    
    sd.putNumber('matchTime', tyme)
