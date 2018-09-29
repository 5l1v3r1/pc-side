from playsound import playsound 
from networktables import  NetworkTables
# import logging
# logging.basicConfig(level=logging.DEBUG)

ip = "10.71.8.2"

NetworkTables.initialize(server = ip)
sd = NetworkTables.getTable("datatable")

while True:
    if (sd.getNumber("Soundworks", 0) == 17):
            playsound('C:/Users/mars/Desktop/a.mp3') 