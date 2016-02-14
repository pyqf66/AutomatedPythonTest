# coding=utf-8
import simplejson
import uniout
import urllib
import urllib2
import cookielib
from time import sleep
from selenium import webdriver
from pyAuto.util.httpInterface import HttpInterface
from pyAuto.util.logOutput import LogOutput
from pyAuto.caseManage.LoadTestCase import LoadTestCase

log = LogOutput()
class ReconciliationInterfaceTest(object):
    def __init__(self, cookieUrl):
        driver = webdriver.Chrome()
        driver.get(cookieUrl)
        driver.find_element_by_xpath(u"//input[@placeholder='请输入您的账号']").send_keys("admin@yinzuo")
        driver.find_element_by_xpath(u"//input[@placeholder='请输入您的密码']").send_keys("123456")
        driver.find_element_by_xpath("//button[@class='login']").click()
        sleep(1)
        self.cookiesInfo = driver.get_cookies()
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
    def testGetoutMallList(self, url, method=None, parameters=None, headers={}):
        conn = HttpInterface(url, method, parameters, self.cookie, headers)
        return conn.requestWithCookies()
        

if __name__ == "__main__":
    cookieUrl = "http://wbt.ishopcity.cn/reconciliation/admin"
    test = ReconciliationInterfaceTest(cookieUrl)
    url = "http://wbt.ishopcity.cn/reconciliation/financeLoan/getFinanceLoanSumDate.json"
    responseData = test.testGetoutMallList(url)
    print(responseData)
    responseDict = simplejson.loads(responseData)
    print(type(responseDict))
    #print(responseDict["result"]["data"].keys())

    log.basicLog(responseDict["baseCountBean"])
    testCaseObject_baseCountBean=LoadTestCase().ReadExcelCase("D:\workspace-sts-3.6.4.RELEASE\AutomatedPythonTest\dataTable\getFinanceLoanSumDateCase.xls",sheetNum=1)
    casedatabaseCountBean1 = testCaseObject_baseCountBean.getXlsData(1)
    casedatabaseCountBean2 = testCaseObject_baseCountBean.getXlsData(testCaseObject_baseCountBean.rowLinesNum)
    #print "casedatacollect2:",casedatacollect2
    casedatabaseCountBean3=[]
    for i in range(0, len(casedatabaseCountBean2)):
        casedatabaseCountBean3.append(casedatabaseCountBean2[i:i + 1])
    print casedatabaseCountBean3
    dict_case_baseCountBean = dict(zip(casedatabaseCountBean1, casedatabaseCountBean2))
    print "dict_case_baseCountBean:",dict_case_baseCountBean
    log.basicLog(responseDict["baseCountBean"])
    if responseDict["baseCountBean"] == dict_case_baseCountBean:
        log.basicLog( u'baseCountBean数据正确')
    else:
        log.basicLog(u"此方法行不通")
    
    # test.testGetoutMallList(url,method,headers)
        
