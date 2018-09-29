# -*- coding: utf-8 -*-
import os
import platform
import re
import time
import subprocess
from startAppTime import secondTimeFirst
from startAppTime import startTimeFirst
from startAppTime import resposeTime

system = platform.system()
if system is "Windows":
    find = "findstr"
else:
    find = "grep"

def getPackageAndActivity():
    currentFocuse = os.popen("adb shell dumpsys activity |"+find+" mFocusedActivity").read()
    pattern = re.compile(r"[a-zA-Z\.]+/[a-zA-Z\.]+")
    packageName = pattern.findall(currentFocuse)[0].split("/")[0]
    activityName = pattern.findall(currentFocuse)[0].split("/")[-1]
    return packageName, activityName

def getPid(packageName):
    packageName = getPackageAndActivity()[0]
    pid = os.popen("adb shell ps |"+find+" "+packageName).read().split()[1]
    return pid


if __name__ =="__main__":

    name = input("please input your choose:(1.startApptime; 2.activityTime; 3.app fps; "
                 "4.meminfo; 5.cpu; 6:battery; 7.data):")
    #try:
    if name==1:
        print ("请点击进入需要测试的应用页面，获取当前activity.")
        print("可继续执行按回车键。")
        os.system('pause')
        packageName = getPackageAndActivity()[0]
        activityName = getPackageAndActivity()[1]
        startTimeFirst(packageName, activityName, find)
        secondTimeFirst(packageName, activityName, find)
    elif name==2:
        print ("请点击进入需要测试的应用页面，获取当前activity.")
        print("可继续执行按回车键。")
        os.system('pause')
        packageName = getPackageAndActivity()[0]
        activityName = getPackageAndActivity()[1]
        pid = getPid(packageName)
        resposeTime(packageName, activityName, find, pid)
    elif name==3:
        input("请选择上下滑动(选A)，左右滑动(选B)"：)

