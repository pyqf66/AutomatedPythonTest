# coding=utf-8
###########################################
# File: server.py
# Desc: socketserver
# Author: zhangyufeng
# History: 2015/08/18 zhangyufeng 新建
###########################################
import socket
import time
class socketServer(object):
	def __init__(self):
		# 建立socket服务
		socketServer = socket.socket()
		host = socket.gethostname()
		print host
		port = 1234
		socketServer.bind((host, port))
		socketServer.listen(5)
		# 打印请求方数据及发送已连接的通知
		while True:
			content, addr = socketServer.accept()
			print 'Got connect from', addr
			time.sleep(20)
			content.send('Thank you for connecting')
			content.close()
if __name__ == "__main__":
	deal = socketServer()
