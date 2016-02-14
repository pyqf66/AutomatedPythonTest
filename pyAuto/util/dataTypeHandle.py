#coding=utf-8
###########################################
# File: dataTypeHandle.py
# Desc: 数据类型处理工具类
# Author: zhangyufeng
# History: 2015/10/15 zhangyufeng 新建
###########################################

class DataTypeHandle:
    u'''
        DataTypeHandle为容器数据进行unicode编码处理的统一类
        dictValueToUnicode为对字典值数据进行unicode处理的方法
        listValueToUnicode为对列表值数据进行unicode处理的方法
        dictAllToUnicode为对字典全部数据（键和值）数据进行unicode处理的方法
        listAllToUnicode为对列表全部数据进行unicode处理的方法
    '''
    def __init__(self):
        pass
    
    #参数dictParam必须为字典
    def dictValueToUnicode(self,dictParam):
        for k,v in dictParam.items():
            if type(v)==dict:
                dictParam[k]=self.dictValueToUnicode(v)
            elif type(v)==list:
                dictParam[k]=self.listValueToUnicode(v)
            elif v==None:
                pass
            elif type(v)==unicode:
                pass
            else:
                dictParam[k]=str(dictParam[k]).decode("utf-8")
        return dictParam
    
    #参数listParam必须为列表
    def listValueToUnicode(self,listParam):
        lastList=[]
        for i in listParam:
            if type(i)==dict:
                lastList.append(self.dictValueToUnicode(i))
            elif type(i)==list:
                lastList.append(self.listValueToUnicode(i))
            elif i==None:
                pass
            elif type(i)==unicode:
                pass
            else:
                lastList.append(str(i).decode("utf-8"))
        return lastList
        
    #参数dictParam必须为字典
    def dictAllToUnicode(self,dictParam):
        dictAllUnicode=dict()
        for k,v in dictParam.items():
            if type(v)==dict:
                dictAllUnicode[str(k).decode("utf-8")]=self.dictAllToUnicode(v)
            elif type(v)==list:
                dictAllUnicode[str(k).decode("utf-8")]=self.listAllToUnicode(v)
            elif v==None:
                dictAllUnicode[str(k).decode("utf-8")]=None
            elif type(v)==unicode:
                dictAllUnicode[str(k).decode("utf-8")]=v
            else:
                dictAllUnicode[str(k).decode("utf-8")]=str(dictParam[k]).decode("utf-8")
        return dictAllUnicode

    #参数listParam必须为列表
    def listAllToUnicode(self,listParam):
        lastList=[]
        for i in listParam:
            if type(i)==dict:
                lastList.append(self.dictAllToUnicode(i))
            elif type(i)==list:
                lastList.append(self.listAllToUnicode(i))
            elif i==None:
                pass
            elif type(i)==unicode:
                pass
            else:
                lastList.append(str(i).decode("utf-8"))
        return lastList
