#!/usr/bin/env python
# -*- coding`: utf-8 -*
import binascii
import serial
import serial.tools.list_ports
import platform
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# 关
off = [0xA0, 0x01, 0x01, 0xA2]
# 开
on = [0xA0, 0x01, 0x00, 0xA1]

serialName = ''
def sendCmd(cmd):
    sysstr = platform.system()
    if (sysstr == "Windows"):
        serialName = 'COM3'
    elif (sysstr == "Linux"):
        serialName = '/dev/ttyS0'
    else:
        print("Other System tasks")
    serialFd = serial.Serial(serialName, 9600, timeout=60)

    serialFd.write(cmd)

def turnOn():
    sendCmd(on)

def turnOff():
    sendCmd(off)
def startJobs():
    # 输出时间
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # BlockingScheduler
    scheduler = BlockingScheduler()
    scheduler.add_job(turnOn, 'cron', day_of_week='1-5', hour=22, minute=4)
    scheduler.add_job(turnOff, 'cron', day_of_week='1-5', hour=22, minute=5)
    scheduler.start()


if __name__ == '__main__':
    startJobs()