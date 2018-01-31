# test BLE Scanning software
# jcs 6/8/2014
DEBUG = False
import blescan
import sys

import bluetooth._bluetooth as bluez
import time

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)
b_dic={}

returnedList = blescan.parse_events(sock, 10)
print "----------"
for beacon in returnedList:
        beacon_str=",".join(beacon)
        print beacon
        arr=beacon_str.split(",")
        if(arr[2] in b_dic):
                if(b_dic[arr[2]]!=arr[5]):
                        b_dic[arr[2]]=arr[5]
        else:
                b_dic[arr[2]]=arr[5]
        print(b_dic)
        mx_rssi=-90
        for Id,Rssi in b_dic.items():
                if(mx_rssi<=int(Rssi)):
                        mx_rssi=int(Rssi)
        for b_id in b_dic.keys():
                if(mx_rssi==int(b_dic[b_id])):
                        now=time.localtime()
                        s="%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year,now.tm_mon,now.tm_mday,
                                                            now.tm_hour,now.tm_min,now.tm_sec)
                        print "***",s,"=> Now the nearest beacon is ",b_id,"***"
                        




                                
