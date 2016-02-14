# coding=utf-8
###########################################
# File: TimeStamp.py
# Desc: 时间戳生成工具
# Author: zhangyufeng
# History: 2015/08/18 zhangyufeng 新建
###########################################
import time
class TimeStamp(object):
    @classmethod
    def timeStamp(cls):
        # 格式化
        timeFormat1 = '%Y%m%d%H%M%S'
        return time.strftime(timeFormat1)
