from playsound import playsound 
from networktables import NetworkTables
import logging

logging.basicConfig(level=logging.DEBUG)
NetworkTables.initialize(server="10.71.8.2")

table = NetworkTables.getTable("datatable")


while True:

if (table.getBoolean("limitswitch") = true)       
playsound('insert/the/filepath/here/example.mp3') 

