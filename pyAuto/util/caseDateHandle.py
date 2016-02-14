# coding=utf-8
###########################################
# File: caseDateHandle.py
# Desc: 测试用例数据处理类
# Author: caoxueqin
# History: 2015/10/16 caoxueqin 新建
###########################################

class caseDateHandle():
    u'''
        caseDateHandle是针对接口返回数据的不同格式，处理测试数据的类  
    '''
    def __init__(self,responseDataType):
        self.responseDataType=responseDataType
    
    def testCaseData(self,caseList1,caseList2):
        if type(self.responseDataType)==list:
            caselist3 = []
            for i in range(0, len(caseList2)):
                caselist3.append(caseList2[i:i + 1])
            dict_case = dict(zip(caseList1, caselist3))
            return dict_case
        else:
            dict_case = dict(zip(caseList1, caseList2))
            return dict_case