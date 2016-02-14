#coding=utf-8
import httplib
import urllib
import json
from pyAuto.util.TimeStamp import TimeStamp
from pyAuto.util.Md5 import Md5
class TestDealTemplateCrm:
    def sendTradTmpMsg(self):
        url = "http://test.ishopcity.cn/inter/pad/consumptionPoints/sendTemplatesMsg?orgid=68" ;
#生成字典
        dict_req = {
            'req_type' :'R_TRADING' ,
            'req_first' :"尊敬的会员，您的本次交易信息如下" ,
            'req_trading' :"消费积分" ,
            'req_cardno' :'0000070054' ,
            'req_fee' :"200元" ,
            'req_add_point' :"200积分" ,
            'req_reduce_point' :"100积分" ,
            'req_valid_point' :"1000积分" ,
            'req_remark' :"如有疑问，请拨打服务热线123323" ,
            'req_time' :'20150529183956'
        }
        print dict_req
        print type(dict_req)
#生成需要加密的字符串
        str1=\
            "req_add_point=" +dict_req["req_add_point"]+\
            " &req_cardno="+dict_req[ "req_cardno" ]+\
            "&req_fee ="+dict_req[ "req_fee" ]+\
            " &req_first="+dict_req[ "req_first" ]+\
            " &req_reduce_point=" +dict_req["req_reduce_point"]+\
            " &req_remark="+dict_req[ "req_remark" ]+\
            "&req_time ="+dict_req[ "req_time" ]+\
            " &req_trading="+dict_req[ "req_trading" ]+\
            "&req_type ="+dict_req[ "req_type" ]+\
            " &req_valid_point="+dict_req[ "req_valid_point" ]+\
            " &paterner_key=4E34SrAxc019y4d67692Fy34A6716s1d"
        print( "str1=" +str1+"\n" )
#md5加密
        sign=Md5.md5(str1)
        print( "sign=" +sign+"\n" )
#生成json串字典
        jsonDict= {
            'req_type' :dict_req['req_type'],
            'req_first' :dict_req['req_first'],
            'req_trading' :dict_req['req_trading'],
            'req_cardno' :dict_req['req_cardno'],
            'req_fee' :dict_req['req_fee'],
            'req_add_point' :dict_req['req_add_point'],
            'req_reduce_point' :dict_req['req_reduce_point'],
            'req_valid_point' :dict_req['req_valid_point'],
            'req_remark' :dict_req['req_remark'],
            'req_time' :dict_req['req_time'],
            'req_sign' :sign
#             'req_sign':'ca7641c7d0c15aac3b846e68b1112c4f'
        }
       
#         print(jsonStr+"\n")
        print type(jsonDict)
        print(url+ "\n" )
#         jdata=json.dumps(jsonDict)
#生成json串
        jdata=json.dumps(jsonDict,ensure_ascii=False )
        print jdata
        print type(jdata)
#         req=urllib2.Request( url,jdata)
#         response=urllib2. urlopen(req )
        headers={"Content-type" :"application/json" }
        conn=httplib.HTTPConnection("test.ishopcity.cn" )
        conn.request( "POST" , "/ inter/pad/consumptionPoints/sendTemplatesMsg? orgid=68", jdata, headers)
        response=conn.getresponse()
        print response.status
       
       
#         print("返回:"+response)
#         print("返回:"+urllib.urlencode(response))
        print response.read()
        
    def CancelBindCard(self):
        #url = "http://218.56.40.251:8087/ashx/WXInterface.ashx?card_prefix=000007" ;
#生成字典
        dict_req = {
            'openid' :"o86IHj65R6U8ZJJsBpriz1IWu4h4" ,
            'card_no' :"0000070681" ,
            'id_no' :"340101198509160071" ,
            'phone' :'18600954321'
        }
#         print type(dict_req["openid"])
#         print urllib.quote(dict_req["openid"])
#         print dict_req
#         print type(dict_req)
#生成需要加密的字符串
        #dictSortKey_req=sorted(dict_req.items(), key=lambda dict_req:dict_req[0])
#         print(dictSortKey_req)
        timestamp=TimeStamp()
#         print timestamp.timeStamp()
        str1=str(timestamp.timeStamp())+"CancelBindCard"+str(2.0)+"MDljYzJhNmE0MmM2ZjZmODdmMGIzMzU4Yjg1ZTU2MWE="
#         print( "str1=" +str1+"\n" )
#md5加密
        signStr=Md5()
        sign=signStr.md5(str1)
#         print( "sign=" +sign+"\n" )
#生成json串字典
        jsonDict= {
            'method' :'CancelBindCard',
            'dt' :timestamp.timeStamp(),
            'ver' :'2.0',
            'sign' :sign,
            'args' :{
            'openid' :urllib.quote(dict_req['openid']) ,
            'card_no' :urllib.quote(dict_req['card_no']) ,
            'id_no' :urllib.quote(dict_req['id_no']) ,
            'phone' :urllib.quote(dict_req['phone'])
                     }
         }
       
#         print type(jsonDict)
#         print(url+ "\n" )
#生成json串
        jdata=json.dumps(jsonDict,ensure_ascii=False )
#         print jdata
#         print type(jdata)
        headers={"Content-type" :"application/json" }
        conn=httplib.HTTPConnection("218.56.40.251:8087" )
        #生产
        #conn=httplib.HTTPConnection("218.56.40.251:9092" )
        conn.request( "POST" , "/ashx/WXInterface.ashx?card_prefix=000007", jdata, headers)
        response=conn.getresponse()
#         print response.status
        print response.read()
       
       
if __name__=="__main__":
    test=TestDealTemplateCrm()
    #test.CancelBindCard()
    test.sendTradTmpMsg()
