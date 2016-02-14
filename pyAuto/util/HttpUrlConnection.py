# coding=utf-8
###########################################
# File: HttpUrlConnection.py
# Desc: http接口工具类
# Author: zhangyufeng
# History: 2015/11/15 zhangyufeng 新建
###########################################
import httplib
import urllib
import json
import urllib2
import cookielib
import simplejson

class HttpUrlConnection(object):
    u''' 
        methon为请求方法
        parameter为请求参数
        cookie为获取的cookie
        headers为请求头
    '''
    # 处理预置数据
    def __init__(self, url, method="GET", parameters=None, cookie=None, headers={}):
        # 解析url
        self.__url = url
        scheme, rest = urllib.splittype(self.__url)
        # 拆分域名和路径
        self.__hostAbsolutely, self.__path = urllib.splithost(rest)
        hostList=self.__hostAbsolutely.split(":")
        if len(hostList)==1:
            self.__host=hostList[0]
            self.__port=80
        elif len(hostList)==2:
            self.__host=hostList[0]
            self.__port=hostList[1]
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
        conn = httplib.HTTPConnection(self.__host,self.__port)
        if self.__method=="GET":
            self.path=self.__path+self.__parametersUrlencodeDeal
            conn.request(self.__method, self.__path)
        if self.__method=="POST":
            conn.request(self.__method, self.__path, self.__jdata, self.__headers)
        response = conn.getresponse()
        resultOrigin=response.read()
        try:
            result = unicode(resultOrigin, "gb2312").encode("utf8")
        except :
            result = resultOrigin
        return result
    
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
