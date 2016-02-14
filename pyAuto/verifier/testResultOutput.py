# coding=utf-8
###########################################
# File: testResultOutput.py
# Desc: 结果验证日志输出模块
# Author: zhangyufeng
# History: 2014/11/11 zhangyufeng 新建
###########################################
import logging
import os
class TestResultOutput:
    def __init__(self):
        #切换目录至logs
        currentDir = os.getcwd()
        os.chdir(currentDir)
        os.chdir(r"logs")
        
    def basicLog(self, msg, logName=None):
        #基础日志配置
        if logName == None:
            logName = "testResult.log"
        logsDir = os.getcwd() + "\\" + logName
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(message)s',
                            datefmt='%a,%d %b %Y %H:%M:%S',
                            filename=logsDir,
                            filemode='a')                               
        logging.info(msg)
        print(msg)
        
    # 验证是否相等
    def compareAnd(self, srcTest, destTest, msg, logName=None):
        resultSuccess = msg + u"校验成功"
        resultFail = msg + u"校验失败"
        if srcTest == destTest:
            self.basicLog(logName, resultSuccess)
        else:
            self.basicLog(logName, resultFail)
 
    # 验证是否不相等	    
    def compareXor(self, srcTest, destTest, msg, logName=None):
        resultSuccess = msg + u"校验成功"
        resultFail = msg + u"校验失败"
        if srcTest == destTest:
            self.basicLog(logName, resultFail)
        else:
            self.basicLog(logName, resultSuccess)

    # 验证返回是否为True	    
    def resultTrue(self, desttest, msg, logName=None):
        resultSuccess = msg + u"校验成功"
        resultFail = msg + u"校验失败"
        if desttest:
            self.basicLog(logName, resultSuccess)
        else:
            self.basicLog(logName, resultFail)

    # 验证返回是否为False	    
    def resultFalse(self, desttest, msg, logName=None):
        resultSuccess = msg + u"校验成功"
        resultFail = msg + u"校验失败"
        if desttest:
            self.basicLog(logName, resultFail)
        else:
            self.basicLog(logName, resultSuccess)
