from test import *
import blescan
import sys
import bluetooth._bluetooth as bluez
import json
#import time
#import logging
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

dev_id = 0
#logging.basicConfig(filename='./log/test.log',level=logging.DEBUG)
try:
	sock = bluez.hci_open_dev(dev_id)
	print ("ble thread started")

except:
	print ("error accessing bluetooth device...")
    	sys.exit(1)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)
b_dic={}

def get_beacon_data():
        
        returnedList = blescan.parse_events(sock, 10)
        
	for beacon in returnedList:
            beacon_str=",".join(beacon)
            arr=beacon_str.split(",")
            if(arr[2] in b_dic):            #get beacon id
                if(b_dic[arr[2]]!=arr[5]):  
                    b_dic[arr[2]]=arr[5]
            else:
                b_dic[arr[2]]=arr[5]
                
        mx_rssi=-80
        b_id = 9999
        
        for id in b_dic.keys():
            #if(bool(b_dic[id].strip()) != False):
            print(id,":",b_dic[id])
            if(mx_rssi <= int(b_dic[id])):
                b_id = id
                mx_rssi = int(b_dic[id])
               
        return [b_id,mx_rssi]
xs = []
ys = []
i = 0
while True:
    
	#print "------------------------------------------"
	
	gps_data_buffer = get_gps_data().split(',')
	beacon_data_buffer = get_beacon_data()
    
        dict_data = {'time':int(float(gps_data_buffer[0])) + 90000,'lat':gps_data_buffer[1], 'long':gps_data_buffer[3], 'settle':gps_data_buffer[6], 'b_id':beacon_data_buffer[0], 'rssi':beacon_data_buffer[1]}
        json_data = json.dumps(dict_data)
        
        
        ys.append(beacon_data_buffer[0])
        i = i+1
        xs.append(i)
        ax1.plot(xs,ys)
        #print(json_data)        
        #requests.put('https://sun-serv-demo.herokuapp.com/user/',data = json_data)
        #requests.post('http://192.168.100.24:3000/user',data = dict_data)
        

        #logging.info(json_data)
        
