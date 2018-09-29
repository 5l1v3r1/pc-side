from playsound import playsound 
from networktables import  NetworkTables
# import logging
# logging.basicConfig(level=logging.DEBUG)

ip = "127.0.0.1"

NetworkTables.initialize(server = ip)
sd = NetworkTables.getTable("datatable")
sdFlag = 0

while True:
    if ((sd.getNumber("Soundworks", 0) == 17) and sdFlag == 0):
        playsound('sound.mp3')
        sdFlag = 1