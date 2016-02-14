#coding=utf-8
from pyAuto.util.httpInterface import HttpInterface
from pyAuto.util.TimeStamp import TimeStamp
from pyAuto.util.Md5 import Md5
from pyAuto.util.logOutput import LogOutput
import urllib
class InterfaceTest2(object):
    def __init__(self):
        log=LogOutput()
        dtObject=TimeStamp()
        url="http://test.ishop-city.com/admin/getUserInfo.action"
        timeStamp=dtObject.timeStamp()
        method="GET"
        dataDict={
                    "mcode":"hfbh",
                    "dt":timeStamp,
                    "ver":"1.0",
                    "method":"info",
                    "url":"http://www.baidu.com"
                    }
        headers={"Content-type" :"application/json" }
        dictSortKey_req=sorted(dataDict.items(), key=lambda dataDict:dataDict[0])
        listSortKey_req=[]
        for i in dictSortKey_req:
            listSortKey_req.append("=".join(i))
        md5Str="&".join(listSortKey_req)+"&key=526ca4b758aea23d95725280bdef812e"
        log.basicLog(md5Str)
        md5=Md5()
        sign=md5.md5(md5Str)
        parameters={
                    "mcode":urllib.quote(dataDict["mcode"]),
                    "dt":urllib.quote(dataDict["dt"]),
                    "ver":urllib.quote(dataDict["ver"]),
                    "method":urllib.quote(dataDict["method"]),
                    "url":urllib.quote(dataDict["url"]),
                    "sign":sign
                    }
        log.basicLog(parameters)
        urlAbsolutely=url+"?"+urllib.urlencode(parameters)
        log.basicLog(urlAbsolutely)
        conn=HttpInterface(urlAbsolutely, method)
        log.basicLog(conn.getHost())
        log.basicLog(conn.getPath())
        log.basicLog(conn.getParametersUrlencodeDeal())
        data=conn.request()
        log.basicLog(data)
if __name__=="__main__":
    test=InterfaceTest2()