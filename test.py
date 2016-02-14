# #coding=utf-8
# import json
# import urllib
# import urllib2
# import cookielib
# from time import sleep
# from selenium import webdriver
# from pyAuto.util.httpInterface import HttpInterface
# from pyAuto.util.logOutput import LogOutput
# 
# # class ReconciliationInterfaceTest(object):
# #     def __init__(self,cookieUrl):
# #         log=LogOutput()
# #         driver=webdriver.Chrome()
# #         driver.get(cookieUrl)
# #         driver.find_element_by_xpath(u"//input[@placeholder='请输入您的账号']").send_keys("admin@yinzuo")
# #         driver.find_element_by_xpath(u"//input[@placeholder='请输入您的密码']").send_keys("123456")
# #         driver.find_element_by_xpath("//button[@class='login']").click()
# #         sleep(1)
# #         self.cookiesInfo=driver.get_cookies()
# #         self.path=self.cookiesInfo[0]["path"]
# #         self.domain=self.cookiesInfo[0]["domain"]
# #         self.name=self.cookiesInfo[0]["name"]
# #         self.value=self.cookiesInfo[0]["value"]
# #         self.cookie= cookielib.Cookie(version=0, name=self.name,value=self.value,
# #                      port=None, port_specified=None,
# #                      domain=self.domain, domain_specified=None, domain_initial_dot=None,
# #                      path=self.path, path_specified=None,
# #                      secure=None,
# #                      expires=None,
# #                      discard=None,
# #                      comment=None,
# #                      comment_url=None,
# #                      rest=None,
# #                      rfc2109=False,
# #             )
# #     def testGetoutMallList(self,url,method=None,parameters=None,headers={}):
# #         tmp
# #         conn=HttpInterface(url, method, parameters, self.cookie,headers)
# #         return conn.requestWithCookies()
# #         
# 
# # if __name__=="__main__":
# #     cookieUrl="http://test.ishopcity.cn/reconciliation/admin"
# #     test=ReconciliationInterfaceTest(cookieUrl)
# #     url="http://test.ishopcity.cn/reconciliation/outMallSettleCheck/getoutMallList.json"
# #     responseData=test.testGetoutMallList(url)
# #     #test.testGetoutMallList(url,method,headers)
# class SmartRedirectHandler(urllib2.HTTPRedirectHandler):     
#     def http_error_301(self, req, fp, code, msg, headers):  
#         result = urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)              
#         result.status = code                                 
#         return result                                       
# 
#     def http_error_302(self, req, fp, code, msg, headers):   
#         result = urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)              
#         result.status = code                                
#         return result              
# if __name__=="__main__":
#     debug_handler = urllib2.HTTPHandler(debuglevel = 1)
#     log=LogOutput()
#     request="http://test.ishopcity.cn/reconciliation/"
#     opener1=urllib2.build_opener(debug_handler,SmartRedirectHandler)
#     opener2=urllib2.build_opener()
#     f1=opener1.open(request)
#     log.basicLog(type(f1))
#     log.basicLog(f1)
#     log.basicLog(f1.status)
#     log.basicLog(f1.code)
#     log.basicLog(dir(f1))
#     log.basicLog(f1.headers)
#     log.basicLog(f1.info)
#     log.basicLog(f1.msg)
#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
#Filename:states_code.py
  
# import urllib2
#   
# class RedirctHandler(urllib2.HTTPRedirectHandler):
#     """docstring for RedirctHandler"""
#     def http_error_301(self, req, fp, code, msg, headers):
#         pass
#     def http_error_302(self, req, fp, code, msg, headers):
#         pass
#   
# def getUnRedirectUrl(url,timeout=10):
#     req = urllib2.Request(url)
#     debug_handler = urllib2.HTTPHandler(debuglevel = 1)
#     opener = urllib2.build_opener(debug_handler, RedirctHandler)
# 
#     html = None
#     response = None
#     try:
#         response = opener.open(url,timeout=timeout)
#         html = response.read()
#     except urllib2.URLError as e:
#         if hasattr(e, 'code'):
#             error_info = e.code
#         elif hasattr(e, 'reason'):
#             error_info = e.reason
#     finally:
#         if response:
#             response.close()
#         if html:
#             return html
#         else:
#             return error_info
#   
# html = getUnRedirectUrl('http://jb51.net')
# print type(html)
# from pyAuto.util.remoteServer import RemoteServer
# import os
# from pyAuto.util.readConfig import ReadConfig
# test=ReadConfig("ipAddress","IP")
# print test.iniData()
# def toDict(**kwargs):
#     return kwargs
# tmpList1=['a=b','c=d']
# tmpList2=[['a','b'],['c','d']]
# print tmpList1[0].split("=")
# print dict(tmpList2)
# import os
# currentDir = os.getcwd()
# configFile = currentDir + "\\config\\" + "config.conf"
# file=open(configFile,'r')
# resultList=file.readlines()
# resultDealList=[]
# for i in resultList:
#     resultDealList.append(i.strip('\n'))
# print resultDealList
# from pyAuto.util.readConfig import ReadConfig
# config=ReadConfig()
# print config.confData('code'))
from pyAuto.util.dataTypeHandle import DataTypeHandle
a={'a':1,'b':{'c':2,'d':{'e':3}},'f':[4,[5,6],{'g':7},[8,{'h':9}]]}
dataTypeHandleObject=DataTypeHandle()
print dataTypeHandleObject.dictValueToString(a)