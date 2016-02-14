# coding=utf-8
###########################################
# File: remoteServer.py
# Desc: 远程连接服务器工具类
# Author: zhangyufeng
# History: 2015/10/13 zhangyufeng 新建
###########################################
import paramiko
class RemoteServer:
    def __init__(self, ip, port, user, pwd):
        self.ip = ip
        self.port = port
        self.user = user
        self.pwd = pwd

    def sshClient(self):
        # 此函数返回值可以直接通过exec_command方法执行linux命令，用法如下
        #     stdin,stdout,stderr=ssh.exec_command("ls")
        #     print stdout.readlines() 
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        return self.ssh.connect(self.ip, self.port, self.user, self.pwd)
        
    def ftpClient(self):
        # 此函数返回值可以直接通过get或put方法执行ftp操作，用法如下
        #sftp.get(r"/root/test/testTxt.txt", "d:\\testTxt.txt")
        #sftp.put("d:\\testTxt.txt", r"/root/test/testTxt.txt")
        self.ftp= paramiko.Transport((self.ip, self.port))
        self.ftp.connect(username=self.user, password=self.pwd)
        return paramiko.SFTPClient.from_transport(self.ftp)

    def __del__(self):
        self.ssh.close()
        self.ftp.close()
        
        
        