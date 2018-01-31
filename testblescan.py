# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys

import bluetooth._bluetooth as bluez

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)
b_dic={'id':'rssi'}
while True:
	returnedList = blescan.parse_events(sock, 10)
	print "----------"
	for beacon in returnedList:
                beacon_string=",".join(beacon)
                arr=beacon_string.split(",")
                if(arr[2] in b_dic):
                        print "yes"
                        if(b_dic[arr[2]]<=arr[5]):
                                b_dic[arr[2]]=arr[5]
                else:
                        print "no"
                        b_dic[arr[2]]=arr[5]
                print(b_dic)
                               

                                      
                
