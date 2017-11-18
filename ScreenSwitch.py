#python 3.4 win7
#关闭显示器
from ctypes import *
import sys
import time

#定义变量
HWND_BROADCAST = 0xffff
WM_SYSCOMMAND = 0x0112
SC_MONITORPOWER = 0xf170
MonitroPowerOn = -1    #打开显示器
MonitorGoLowPower = 1    #进入低电量
MonitorPowerOff = 2    #关闭显示器

def PowerOn():
    windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND,SC_MONITORPOWER, MonitroPowerOn)

def GoLowPower():
    windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND,SC_MONITORPOWER, MonitorGoLowPower)

def PowerOff():
    windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND,SC_MONITORPOWER, MonitorPowerOff)

if len(sys.argv) == 2:
    if sys.argv[1] == 'on':
        PowerOn()
        exit()
    elif sys.argv[1] == 'low':
        GoLowPower()
        exit()
    elif sys.argv[1] == 'off':
        PowerOff()
        exit()

if len(sys.argv) == 3:
    startime = sys.argv[1].split(':')
    endtime = sys.argv[2].split(':')
    
    #获取开始/结束分钟
    if len(startime) >= 2 and int(startime[1]) >= 0 and int(startime[1]) < 60:
        startm = int(startime[1])
    else:
        startm = 0

    if len(endtime) >= 2 and int(endtime[1]) >= 0 and int(endtime[1]) < 60:
        endm = int(endtime[1])
    else:
        endm = 0
        
    #获取开始/结束小时
    if int(startime[0]) >= 0 and int(startime[0]) < 24:
        starth = int(startime[0])

    if int(endtime[0]) >= 0 and int(endtime[0]) < 24:
        endh = int(endtime[0])

    #程序开始
    while True:
        #获取当前时间（小时/分钟），用于关屏
        nowtime = time.asctime().split(' ')[3]
        nowh = int(nowtime.split(':')[0])
        nowm = int(nowtime.split(':')[1])
        #关闭屏幕
        if nowh > starth or (nowh == starth and nowm >= startm):
            PowerOff()
            
            while True:
                #获取当前时间（小时/分钟），用于开屏
                nowtime = time.asctime().split(' ')[3]
                nowh = int(nowtime.split(':')[0])
                nowm = int(nowtime.split(':')[1])
                #开启屏幕
                if nowh == endh and nowm == endm:
                    PowerOn()
                    exit()
                else:
                    time.sleep(50)
else:
    print('Effect:Screen switch or Timing Screen Switch.\n\
\n\
 Usage:\n\
    (1)Screen Switch\n\
    Format:\n\
        ToolName [on] [off] [low]\n\
    Parameter:\n\
        on  - Switch on\n\
        off - Switch off\n\
        low - Monitor low power\n\
\n\
    (2)Timing Screen Switch\n\
    Format:\n\
        ToolName OffTime OnTime\n\
    Parameter:\n\
        OffTime - Screen power off time.\n\
                    (Time format(00:00), or just hour integer(0~23))\n\
        OnTime  - Screen power on time.\n\
                    (Time format(00:00), or just hour integer(0~23))')
    input()
    exit()
