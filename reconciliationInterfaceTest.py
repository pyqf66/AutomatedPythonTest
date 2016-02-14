# coding=utf-8
###########################################
# File: reconciliationInterfaceTest.py
# Desc: 对账平台接口测试程序
# Author: zhangyufeng
# History: 2015/09/29 zhangyufeng 新建
###########################################
import os
import simplejson
import uniout
import urllib
import urllib2
import cookielib
import os
from time import sleep
from selenium import webdriver
from pyAuto.util.httpInterface import HttpInterface
from pyAuto.util.logOutput import LogOutput
from pyAuto.caseManage.LoadTestCase import LoadTestCase
from pyAuto.util.dataTypeHandle import DataTypeHandle
from pyAuto.util.caseDateHandle import caseDateHandle
# 初始化日志工具类
log = LogOutput()
dataTpyeHandleObject=DataTypeHandle()
currentDir=os.getcwd()
dataTableDir=os.chdir(currentDir+"\\dataTable\\")
class ReconciliationInterfaceTest(object):
    u'''
        ReconciliationInterfaceTest为对账平台测试工具类，每个方法都为一个接口
    '''
    
    def __init__(self, cookieUrl):
        # 调用selenium进行cookie获取
        driver = webdriver.Chrome()
        driver.get(cookieUrl)
        driver.find_element_by_xpath(u"//input[@placeholder='请输入您的账号']").send_keys("admin@yinzuo")
        driver.find_element_by_xpath(u"//input[@placeholder='请输入您的密码']").send_keys("123456")
        driver.find_element_by_xpath("//button[@class='login']").click()
        sleep(1)
        self.cookiesInfo = driver.get_cookies()
        #建立http可用的cookie
        self.path = self.cookiesInfo[0]["path"]
        self.domain = self.cookiesInfo[0]["domain"]
        self.name = self.cookiesInfo[0]["name"]
        self.value = self.cookiesInfo[0]["value"]
        self.cookie = cookielib.Cookie(version=0, name=self.name, value=self.value,
                     port=None, port_specified=None,
                     domain=self.domain, domain_specified=None, domain_initial_dot=None,
                     path=self.path, path_specified=None,
                     secure=None,
                     expires=None,
                     discard=None,
                     comment=None,
                     comment_url=None,
                     rest=None,
                     rfc2109=False,
            )
        
    def getCasePath(self,filename):
        jobpath=os.getcwd()
        global casepath
        casepath=jobpath+"/dataTable/"+filename
        return casepath
    
    #查询对外商家结算列表信息接口
    def testGetoutMallList(self, url, method=None, parameters=None, headers={}):
        conn = HttpInterface(url, method, parameters, self.cookie, headers)
        responseData= conn.requestWithCookies()
        #print(responseData)
        responseDict = dataTpyeHandleObject.dictAllToUnicode(simplejson.loads(responseData))
        #print(type(responseDict))
        #print responseDict
       # print "testData:",testData
        print "测试查询对外商家结算列表信息接口:"
       #验证接口返回list部分
        testCaseObject = LoadTestCase().ReadExcelCase("D:\workspace-sts-3.6.4.RELEASE\AutomatedPythonTest\dataTable\getoutMallListCase.xls", 0, sheetNum=1)
        caseList1 = testCaseObject.getXlsData(1)
        caseList2 = testCaseObject.getXlsData(testCaseObject.rowLinesNum)
        duibidata = caseDateHandle(responseDict["result"]["data"]["list"])
        dict_case = duibidata.testCaseData(caseList1, caseList2)
        print "测试数据：",dict_case
        print "返回数据：",responseDict["result"]["data"]["list"]
        if responseDict["result"]["data"]["list"] == dict_case:
            log.basicLog( u'list数据正确')
        else:
            log.basicLog(u"list数据不正确")
            
        #验证接口返回collect部分
        testCaseObject_collect = LoadTestCase().ReadExcelCase("D:\workspace-sts-3.6.4.RELEASE\AutomatedPythonTest\dataTable\getoutMallListCase.xls", 0, sheetNum=2)
        casedatacollect1 = testCaseObject_collect.getXlsData(1)
        casedatacollect2 = testCaseObject_collect.getXlsData(testCaseObject_collect.rowLinesNum)
        duibidata = caseDateHandle(responseDict["result"]["data"]["collect"])
        dict_case_collect = duibidata.testCaseData(casedatacollect1, casedatacollect2)
        print "测试数据：",dict_case_collect
        print "返回数据：",responseDict["result"]["data"]["collect"]
        #print responseDict["result"]["data"]["collect"].keys()
        #print responseDict["result"]["data"]["collect"].values()
        if responseDict["result"]["data"]["collect"] == dict_case_collect:
            log.basicLog( u'collect数据正确')
        else:
            log.basicLog(u"collect数据不正确")
            
        #验证接口返回malllist部分
        testCaseObject_malllist = LoadTestCase().ReadExcelCase("D:\workspace-sts-3.6.4.RELEASE\AutomatedPythonTest\dataTable\getoutMallListCase.xls", 0, sheetNum=2)
        casedatamalllist1 = testCaseObject_malllist.getXlsData(1)
        casedatamalllist2 = testCaseObject_malllist.getXlsData(testCaseObject_malllist.rowLinesNum)
        duibidata = caseDateHandle(responseDict["result"]["data"]["malllist"])
        dict_case_malllist = duibidata.testCaseData(casedatamalllist1, casedatamalllist2)
        print "测试数据：",dict_case_malllist
        print "返回数据：",responseDict["result"]["data"]["malllist"]
        if responseDict["result"]["data"]["malllist"] == dict_case_collect:
            log.basicLog( u'malllist数据正确')
        else:
            log.basicLog(u"malllist数据不正确")
    
    #查询对内商家结算对账接口
    def testMallSettleCheckList(self, url, method=None, parameters=None, headers={}):
        conn = HttpInterface(url, method, parameters, self.cookie, headers)
        responseData= conn.requestWithCookies()
        #print(responseData)
        responseDict = simplejson.loads(responseData)
        #print(type(responseDict))
        #print(responseDict["rows"].keys())
        print "测试查询对内商家结算对账接口:"
        #log.basicLog(responseDict["rows"][0])
    
        testCaseO_rows=LoadTestCase().ReadExcelCase("D:\workspace-sts-3.6.4.RELEASE\AutomatedPythonTest\dataTable\mallSettleCheckListCase.xls",sheetNum=1)
        casedatarows1 = testCaseO_rows.getXlsData(1)
        casedatarows2 = testCaseO_rows.getXlsData(testCaseO_rows.rowLinesNum)
        duibidata = caseDateHandle(responseDict["rows"][0])
        dict_case_rows = duibidata.testCaseData(casedatarows1, casedatarows2)
        print "测试数据：",dict_case_rows
        print "返回数据：",responseDict["rows"][0]
        if responseDict["rows"][0] == dict_case_rows:
            log.basicLog( u'rows数据正确')
        else:
            log.basicLog(u"rows数据正不确")
            
    #对内商家结算对账统计页接口
    def testMallSettleCheckGetdataBirt(self, url, method=None, parameters=None, headers={}):
        conn = HttpInterface(url, method, parameters, self.cookie, headers)
        responseData= conn.requestWithCookies()
        print "测试对内商家结算对账统计页接口:"
        responseDict = simplejson.loads(responseData)
        #print(type(responseDict))
        #print(responseDict["result"]["data"].keys())

        #log.basicLog(responseDict["baseCountBean"])
        testCaseObject_baseCountBean=LoadTestCase().ReadExcelCase("D:\workspace-sts-3.6.4.RELEASE\AutomatedPythonTest\dataTable\mallSettleCheckgetdataBirtCase.xls",sheetNum=1)
        casedatabaseCountBean1 = testCaseObject_baseCountBean.getXlsData(1)
        casedatabaseCountBean2 = testCaseObject_baseCountBean.getXlsData(testCaseObject_baseCountBean.rowLinesNum)
        duibidata = caseDateHandle(responseDict["baseCountBean"])
        dict_case_baseCountBean = duibidata.testCaseData(casedatabaseCountBean1, casedatabaseCountBean2)
        print "测试数据：",dict_case_baseCountBean
        print "返回数据：",responseDict["baseCountBean"]
        if responseDict["baseCountBean"] == dict_case_baseCountBean:
            log.basicLog( u'baseCountBean数据正确')
        else:
            log.basicLog(u"baseCountBean数据不正确")
            
    #查询银行对账列表接口
    def testFinanceLoanGetFinanceLoan(self, url, method=None, parameters=None, headers={}):
        conn = HttpInterface(url, method, parameters, self.cookie, headers)
        responseData= conn.requestWithCookies()
        print "测试查询银行对账列表接口:" 
        responseDict = simplejson.loads(responseData)
        #print(type(responseDict))
        #log.basicLog(responseDict["rows"][0])
   
        testCaseO_rows=LoadTestCase().ReadExcelCase("D:\workspace-sts-3.6.4.RELEASE\AutomatedPythonTest\dataTable\getFinanceLoanCase.xls",sheetNum=1)
        casedatarows1 = testCaseO_rows.getXlsData(1)
        casedatarows2 = testCaseO_rows.getXlsData(testCaseO_rows.rowLinesNum)
        duibidata = caseDateHandle(responseDict["rows"][0])
        dict_case_rows = duibidata.testCaseData(casedatarows1, casedatarows2)
        print "测试数据：",dict_case_rows
        print "返回数据：",responseDict["rows"][0]
        if responseDict["rows"][0] == dict_case_rows:
            log.basicLog( u'rows数据正确')
        else:
            log.basicLog(u"rows数据不正确")   
    
    #银行对账列表统计页接口
    def testFinanceLoanGetFinanceLoanSumDate(self, url, method=None, parameters=None, headers={}):
        conn = HttpInterface(url, method, parameters, self.cookie, headers)
        responseData= conn.requestWithCookies()
        print "测试银行对账列表统计页接口:"  
        responseDict = simplejson.loads(responseData)
        testCaseObject_baseCountBean=LoadTestCase().ReadExcelCase("D:\workspace-sts-3.6.4.RELEASE\AutomatedPythonTest\dataTable\getFinanceLoanSumDateCase.xls",sheetNum=1)
        casedatabaseCountBean1 = testCaseObject_baseCountBean.getXlsData(1)
        casedatabaseCountBean2 = testCaseObject_baseCountBean.getXlsData(testCaseObject_baseCountBean.rowLinesNum)
        duibidata = caseDateHandle(responseDict["baseCountBean"])
        dict_case_baseCountBean = duibidata.testCaseData(casedatabaseCountBean1, casedatabaseCountBean2)
        print "测试数据：",dict_case_baseCountBean
        print "返回数据：",responseDict["baseCountBean"]
        if responseDict["baseCountBean"] == dict_case_baseCountBean:
            log.basicLog( u'baseCountBean数据正确')
        else:
            log.basicLog(u"baseCountBean数据不正确")   
            
    #微信首付对账列表接口
    def testFirstPayInit(self, url, method=None, parameters=None, headers={}):
        conn = HttpInterface(url, method, parameters, self.cookie, headers)
        responseData= conn.requestWithCookies()
        print "测试微信首付对账列表接口:" 
        responseDict = simplejson.loads(responseData)
        #print(type(responseDict))
        #log.basicLog(responseDict["rows"][0])
   
        testCaseO_rows=LoadTestCase().ReadExcelCase("D:\workspace-sts-3.6.4.RELEASE\AutomatedPythonTest\dataTable\FirstPayinitCase.xls",sheetNum=1)
        casedatarows1 = testCaseO_rows.getXlsData(1)
        casedatarows2 = testCaseO_rows.getXlsData(testCaseO_rows.rowLinesNum)
        duibidata = caseDateHandle(responseDict["rows"][0])
        dict_case_rows = duibidata.testCaseData(casedatarows1, casedatarows1)
        print "测试数据： ",dict_case_rows
        print "返回数据：",responseDict["rows"][0]
        if responseDict["rows"][0] == dict_case_rows:
            log.basicLog( u'rows数据正确')
        else:
            log.basicLog(u"rows数据不正确")
            
    #微信首付对账统计接口
    def testFirstPayGetdataBirt(self, url, method=None, parameters=None, headers={}):
        conn = HttpInterface(url, method, parameters, self.cookie, headers)
        responseData= conn.requestWithCookies()
        print "测试微信首付对账统计接口:" 
        responseDict = simplejson.loads(responseData)
        testCaseObject_baseCountBean=LoadTestCase().ReadExcelCase("D:\workspace-sts-3.6.4.RELEASE\AutomatedPythonTest\dataTable\FirstPaygetdataBirt.xls",sheetNum=1)
        casedatabaseCountBean1 = testCaseObject_baseCountBean.getXlsData(1)
        casedatabaseCountBean2 = testCaseObject_baseCountBean.getXlsData(testCaseObject_baseCountBean.rowLinesNum)
        duibidata = caseDateHandle(responseDict)
        dict_case_baseCountBean = duibidata.testCaseData(casedatabaseCountBean1, casedatabaseCountBean2)
        
        print "测试数据： ", dict_case_baseCountBean
        print "返回数据：",responseDict
        if responseDict == dict_case_baseCountBean:
            log.basicLog(u'baseCountBean数据正确')
        else:
            log.basicLog(u"baseCountBean数据不正确")
            
    #用户还款对账列表接口
    def testRepayCheckList(self, url, method=None, parameters=None, headers={}):
        conn = HttpInterface(url, method, parameters, self.cookie, headers)
        responseData= conn.requestWithCookies()
        print "测试用户还款对账列表接口:" 
        responseDict = simplejson.loads(responseData)
        responsedata=dataTpyeHandleObject.dictAllToUnicode(responseDict["rows"][0])
        testCaseO_rows=LoadTestCase().ReadExcelCase("D:\workspace-sts-3.6.4.RELEASE\AutomatedPythonTest\dataTable\RepayCheckListCase.xls",sheetNum=1)
        casedatarows1 = testCaseO_rows.getXlsData(1)
        casedatarows2 = testCaseO_rows.getXlsData(testCaseO_rows.rowLinesNum)
        duibidata = caseDateHandle(responsedata)
        dict_case_rows = duibidata.testCaseData(casedatarows1, casedatarows2)
        print "测试数据：",dict_case_rows
        print "返回数据：",responsedata
        if responsedata == dict_case_rows:
            log.basicLog( u'rows数据正确')
        else:
            log.basicLog(u"rows数据不正确")
            
    #用户还款对账列表统计接口
    def testRepayCheckGethuizong(self, url, method=None, parameters=None, headers={}):
        conn = HttpInterface(url, method, parameters, self.cookie, headers)
        responseData= conn.requestWithCookies()
        print "测试用户还款对账列表统计接口:" 
        responseDict = simplejson.loads(responseData)
        testCaseObject_collect=LoadTestCase().ReadExcelCase("D:\workspace-sts-3.6.4.RELEASE\AutomatedPythonTest\dataTable\RepayCheckgethuizongCase.xls",sheetNum=1)
        casedatacollect1 = testCaseObject_collect.getXlsData(1)
        casedatacollect2 = testCaseObject_collect.getXlsData(testCaseObject_collect.rowLinesNum)
        duibidata = caseDateHandle(responseDict["collect"])
        dict_case_baseCountBean = duibidata.testCaseData(casedatacollect1, casedatacollect2)
       
        print "测试数据：",dict_case_baseCountBean
        print "返回数据：",responseDict["collect"]
        if responseDict["collect"] == dict_case_baseCountBean:
            log.basicLog( u'collect数据正确')
        else:
            log.basicLog(u"collect数据不正确")
            
if __name__ == "__main__":
    