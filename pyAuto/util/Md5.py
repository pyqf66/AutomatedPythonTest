# coding=utf-8
###########################################
# File: Md5.py
# Desc: md5加密
# Author: zhangyufeng
# History: 2015/08/18 zhangyufeng 新建
###########################################
import hashlib
class Md5(object):
    @classmethod
    def md5(cls, strVar):
        # md5加密并小写化
        md5Var = hashlib.md5()
        md5Var.update(strVar.encode("utf-8"))
        #md5Var.update(strVar)
        sign = md5Var.hexdigest().lower()
        return sign
