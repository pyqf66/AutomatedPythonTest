# coding=utf-8
###########################################
# File: logOutput.py
# Desc: 日志输出模块
# Author: zhangyufeng
# History: 2014/11/11 zhangyufeng 新建
###########################################
import logging
import os
class LogOutput:
    def __init__(self):
        # 切换目录至logs
        currentDir = os.getcwd()
        os.chdir(currentDir)
        os.chdir(r"logs")
        
    def basicLog(self, msg, logName=None):
        # 日志初始化配置
        if logName == None:
            logName = "log.log"
        logsDir = os.getcwd() + "\\" + logName
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(message)s',
                            datefmt='%a,%d %b %Y %H:%M:%S',
                            filename=logsDir,
                            filemode='a')                               
        logging.info(msg)
        print(msg)
