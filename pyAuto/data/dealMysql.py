# coding=utf-8
###########################################
# File: dealMysql.py
# Desc: 数据库处理
# Author: zhangyufeng
# History: 2014/11/11 zhangyufeng 新建
###########################################
import mysql.connector
class DealDb:
    '''
        Dealing with database like select,insert,delete and so on.
    '''
    def __init__(self): 
        self.conn = mysql.connector.connect(host='117.121.26.70', user='kaifa', password='99754106633f94d350db34d548d6091a', database='wx_cloud', port=3305, charset='utf8')
        self.cur = self.conn.cursor()
    def queryDb(self, sqlCode):
        '''
            This function is about only one line.
        '''
        self.linesNum = self.cur.execute(sqlCode)
        # 游标定位到首行
        self.dbData = self.cur.fetchone()
        return self.dbData
    def __del__(self):
        self.cur.close()
        self.conn.close()
