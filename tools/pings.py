# coding:utf-8
import time
import subprocess
import os
true_count = 0
false_count = 0

def ipStrip():
    ips = []
    ip_file = open("ips.txt", 'r')
    for w in ip_file:
        ips.append(w.strip())
    ip_file.close()
    return ips

def IPing(arr):
    ip_log = open("ip_log.txt", 'w+')
    for i in arr:
        result = os.system("ping -n 1 -w 1 %s"%i)
        if result:
            print "ping %s is fail!"%i
            ip_log.write(i + ' fail!' + '\n')
        else:
            print "ping %s is OK!"%i
            ip_log.write(i + ' OK' + '\n')
    ip_log.close()

if __name__ == '__main__':
    # "ip whether ping"
    start_Time = int(time.time())
    ips = ipStrip()
    IPing(ips)
    end_Time = int(time.time())
