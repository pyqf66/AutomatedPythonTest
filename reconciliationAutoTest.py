# coding=utf-8
###########################################
# File: reconciliationAutoTest.py
# Desc: 对账平台接口测试case
# Author: caoxueqin
# History: 2015/10/19 caoxueqin 新建
###########################################
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
from pyAuto.util.dataTypeHandle import DataTypeHandle
from pyAuto.util.caseDateHandle import caseDateHandle
from reconciliationInterfaceTest import ReconciliationInterfaceTest

cookieUrl = "http://wbt.ishopcity.cn/reconciliation/admin"
test = ReconciliationInterfaceTest(cookieUrl)
#查询对外商家结算列表信息接口
url = "http://wbt.ishopcity.cn/reconciliation/outMallSettleCheck/getoutMallList.json"
test.testGetoutMallList(url)
     
#查询对内商家结算对账接口
url = "http://wbt.ishopcity.cn/reconciliation/mallSettleCheck/list.json"
test.testMallSettleCheckList(url)
     
#对内商家结算对账统计页接口
url = "http://wbt.ishopcity.cn/reconciliation/mallSettleCheck/getdataBirt.json"
test.testMallSettleCheckGetdataBirt(url)
 
#查询银行对账列表接口
url = "http://wbt.ishopcity.cn/reconciliation/financeLoan/getFinanceLoan.json"
test.testFinanceLoanGetFinanceLoan(url)  
     
#银行对账列表统计页接口
url = "http://wbt.ishopcity.cn/reconciliation/financeLoan/getFinanceLoanSumDate.json"
test.testFinanceLoanGetFinanceLoanSumDate(url) 
     
#微信首付对账列表接口
url = "http://wbt.ishopcity.cn/reconciliation/firstPay/init.json"
test.testFirstPayInit(url)
     
#微信首付对账统计接口
url = "http://wbt.ishopcity.cn/reconciliation/firstPay/getdataBirt.json"
test.testFirstPayGetdataBirt(url) 
     
#用户还款对账列表接口
url = "http://wbt.ishopcity.cn/reconciliation/repayCheck/list.json"
test.testRepayCheckList(url)
     
#用户还款对账列表统计接口
url = "http://wbt.ishopcity.cn/reconciliation/repayCheck/gethuizong.json"
test.testRepayCheckGethuizong(url)
