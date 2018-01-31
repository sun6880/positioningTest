'''
GPS Interfacing with Raspberry Pi using Pyhton
http://www.electronicwings.com
'''
import serial               #import serial pacakge
from time import sleep
import webbrowser           #import package for opening link in browser
import sys                  #import system package
import json
from collections import OrderedDict

def GPS_Info():
    nmea_time = []
    nmea_latitude = []
    nmea_longitude = []
    nmea_used_settle = []
    nmea_time = NMEA_buff[0]                    #extract time from GPGGA string
    nmea_latitude = NMEA_buff[1]                #extract latitude from GPGGA string
    nmea_longitude = NMEA_buff[3]               #extract longitude from GPGGA string
    nmea_used_settle = NMEA_buff[6]
    
    #if(bool(nmea_latitude.strip())!=False):
    
    #gps_data = OrderedDict()
    #gps_data["time"] = int(float(nmea_time)) + 90000
    #gps_data["lat"] = nmea_latitude
    #gps_data["long"] = nmea_longitude
    
    #print(json.dumps(gps_data,ensure_ascii=False, indent="\t"
    
    print("time:",int(float(nmea_time)) + 90000,'\n')
    print("NMEA Time:",nmea_time,'\n')
    print ("NMEA Latitude:",nmea_latitude,"NMEA Longitude:",nmea_longitude,'\n')
    print ("NMEA usedSettle:",nmea_used_settle,'\n')
    
    #if(nmea_latitude==" "):
    #   print("test:",nmea_latitude,".\n")
    
    #    lat = float(nmea_latitude)                  #convert string into float for calculation
    #    longi = float(nmea_longitude)               #convertr string into float for calculation
    
    #    lat_in_degrees = convert_to_degrees(lat)    #get latitude in degree decimal format
    #    long_in_degrees = convert_to_degrees(longi) #get longitude in degree decimal format
    
#convert raw NMEA string into degree decimal format   
def convert_to_degrees(raw_value):
    decimal_value = raw_value/100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    position = degrees + mm_mmmm
    position = "%.4f" %(position)
    return position
    

def get_gps_data():
    global NMEA_buff
    global lat_in_degrees
    global long_in_degrees
   
    gpgga_info = "$GPGGA,"
    ser = serial.Serial ("/dev/ttyS0")              #Open port with baud rate
    GPGGA_buffer = 0
    GP_buffer = 0
    NMEA_buff = 0
    lat_in_degrees = 0
    long_in_degrees = 0
    used_settle = 0
    try: 
        while True:
            received_data = (str)(ser.readline())                   #read NMEA string received
            GPGGA_data_available = received_data.find(gpgga_info)   #check for NMEA GPGGA string
            if (GPGGA_data_available>=0):
                GPGGA_buffer = received_data.split("$GPGGA,",1)[1]  #store data coming after "$GPGGA," string
                return GPGGA_buffer
               # NMEA_buff = (GPGGA_buffer.split(','))               #store comma separated data in buffer
               # GPS_Info()                                          #get time, latitude, longitude
               # break
            #break
            #print("lat in degrees:", lat_in_degrees," long in degree: ", long_in_degrees, '\n')  
            #map_link = 'http://maps.google.com/?q=' + convert_to_degrees(float("3533.8322")) + ',' + convert_to_degrees(float("12919.0218")) #'http://maps.google.com/?q=' + lat_in_degrees + ',' + long_in_degrees    #create link to plot location on Google map
            #print("<<<<<<<<press ctrl+c to plot location on google maps>>>>>>\n")               #press ctrl+c to plot on map and exit 
            
                      
    except KeyboardInterrupt:
        webbrowser.open(map_link)        #open current position information in google map
        sys.exit(0)
