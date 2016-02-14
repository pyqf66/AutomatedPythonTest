# coding=utf-8
###########################################
# File: httpInterface.py
# Desc: http接口工具类
# Author: zhangyufeng
# History: 2015/09/28 zhangyufeng 新建
###########################################
import httplib
import urllib
import json
import urllib2
import cookielib

class HttpInterface(object):
    u''' 
        methon为请求方法
        parameter为请求参数
        cookie为获取的cookie
        headers为请求头
    '''
    # 处理预置数据
    def __init__(self, url, method=None, parameters=None, cookie=None, headers={}):
        # 解析url
        self.__url = url
        scheme, rest = urllib.splittype(self.__url)
        # 拆分域名和路径
        self.__host, self.__path = urllib.splithost(rest)
        # 对所传参数进行处理
        self.__method = method
        self.__data = parameters
        self.__cookie = cookie
        if parameters != None:
            self.__parametersUrlencodeDeal = urllib.urlencode(parameters)
        else:
            self.__parametersUrlencodeDeal = None
        self.__jdata = json.dumps(parameters, ensure_ascii=False)
        self.__headers = headers
        
    # 发送普通请求,要求完全满足http协议规则
    def request(self):
        conn = httplib.HTTPConnection(self.__host)
        conn.request(self.__method, self.__path, self.__parametersUrlencodeDeal, self.__headers)
        response = conn.getresponse()
        resultDict = {}
        resultDict["status"] = response.status
        resultDict["reason"] = response.reason
        resultDict["data"] = response.read()
        return resultDict
        
    # 发送json请求
    def requestJson(self):
        conn = httplib.HTTPConnection(self.__host)
        conn.request(self.__method, self.__path, self.__jdata, self.__headers)
        response = conn.getresponse()
        resultDict = {}
        resultDict["status"] = response.status
        resultDict["reason"] = response.reason
        resultDict["data"] = response.read()
        return resultDict
    
    # 使用urllib2发送请求,对协议的格式要求不像httplib那么严格
    def requestUrllib2(self):
        if type(self.__data) == dict:
            self.__data = urllib.urlencode(self.__data)
        req = urllib2.Request(self.__url, self.__data, self.__headers)
        response = urllib2.urlopen(req)
        data = response.read()
        # 处理urllib2抓取内容乱码问题
        try:
            return unicode(data, "gb2312").encode("utf8")
        except:
            return data
    
    # 使用urllib2发送带cookie的请求
    def requestWithCookies(self):
        cookiejar = cookielib.CookieJar()
        cookiejar.set_cookie(self.__cookie)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
        if self.__data == None:
            request = urllib2.Request(self.__url)
        else:
            request = urllib2.Request(self.__url, self.__data)
        html = opener.open(request).read()
        return html
    
    # 提供外部host数据    
    def getHost(self):   
        return self.__host
    
    # 提供外部path数据
    def getPath(self):
        return self.__path
    
    # 提供外部经过ulrencode处理后的数据
    def getParametersUrlencodeDeal(self):
        return self.getParametersUrlencodeDeal
