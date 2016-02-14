#coding=utf-8
import cookielib
import urllib2
import urllib

post_data = {'username':'admin@suolong','password':'123456'}
post_data_urlencode = urllib.urlencode(post_data)
loginUrl = "http://test2.ishop-city.com/reconciliation/admin/user/login.json"
testUrl= 'http://test2.ishop-city.com/reconciliation/repayCheck/gethuizong.json'
cj = cookielib.CookieJar()
openner = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#伪装成一个正常的浏览器，避免有些web服务器拒绝访问。
openner.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
tmp1=openner.open(loginUrl,post_data_urlencode)
tmp2=openner.open(testUrl)
print tmp2.read()

# 查看具体的值
# for cookiedata in enumerate(cj):
#     print cookiedata[1]