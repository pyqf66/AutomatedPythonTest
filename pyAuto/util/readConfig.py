# coding=utf-8
###########################################
# File: readConfig.py
# Desc: 读取配置文件工具类
# Author: zhangyufeng
# History: 2015/10/13 zhangyufeng 新建
###########################################
from ConfigParser import SafeConfigParser
import os
class ReadConfig:
    u'''
        conf.ini和config.conf配置文件路径不可更改
    '''
    
    def __init__(self):
        currentDir = os.getcwd()
        self.__iniConfigFile = currentDir + "\\config\\" + "config.ini"
        self.__confConfigFile = currentDir + "\\config\\" + "config.conf"
    
    # 读取windows ini配置文件
    # 配置文件格式
    #   [table]
    #   key=value
    def iniData(self, label, key):
        config = SafeConfigParser()
        config.read(self.__configFile)
        return config.get(label, key)
    
    # 读取linux配置文件
    # 配置文件格式
    #   key=value
    def confData(self, key):
        configFile = open(self.__confConfigFile, 'r')
        result = configFile.readlines()
        resultDealList = []
        keyValueList = []
        for i in result:
            resultDealList.append(i.strip('\n'))
        for j in resultDealList:
            keyValueList.append(j.split('='))
        resultDict = dict(keyValueList)
        return resultDict[key]
