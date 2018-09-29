# -*- coding: utf-8 -*-
import os
from time import sleep
import re


def secondTimeFirst(packageName, activityName, find):
    k=0
    print ("热启动时间为：")
    for i in range(10):
        os.popen("adb shell input keyevent 3")
        sleep(2)
        totalTimeL = os.popen("adb shell am start -W -n "+packageName+
                             "/"+activityName+" |"+find+" TotalTime").read().split(":")[-1]
        totalTime = int(totalTimeL)
        print totalTime
        k += totalTime
        sleep(5)
    print ("平均值为："),k/10

def startTimeFirst(packageName, activityName, find):
    j=0
    print ("冷启动时间为：")
    for i in range(10):
        totalTimeL = os.popen("adb shell am start -W -S -n "+packageName+
                             "/"+activityName+" |"+find+" TotalTime").read().split(":")[-1]
        totalTime = int(totalTimeL)
        print totalTime
        j += totalTime
        sleep(5)
    print ("平均值为："),j/10

def resposeTime(packageName, activityName, find, pid):
    j=0
    print ("响应时间为：")
    for x in range(10):
        os.system('adb shell input keyevent 4')
        sleep(3)
        os.popen("adb shell am start -W -n "+packageName+"/"+activityName)
        result = os.popen("adb logcat -v time -d|"+find+" Displayed").read().split()[-1:]
        result0 = result[0]
        pattern = re.compile("[0-9]+")
        resposeTime = pattern.findall(result0)[0]
        os.system('adb shell input keyevent 4')
        sleep(3)
        os.system('adb logcat -c')
        print resposeTime
    j += resposeTime
    sleep(5)
    print ("平均值为："),j/10
