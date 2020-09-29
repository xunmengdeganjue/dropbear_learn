#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
# import socket
# import subprocess
import paramiko
import time


def ssh2(ip, username, passwd, cmd):
    try:
        #print(sssss1)
        ssh = paramiko.SSHClient()
        #print(sssss)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        ssh.connect(ip, 22, username, passwd, timeout=5)
        
        for k in range(1, 5):
            stdin, stdout, stderr = ssh.exec_command(cmd)
            time.sleep(1)
            print(stdout.read())
        print('%stOKn' %(cmd))
        ssh.close()
        print('close SSH, wait 5s')
        time.sleep(5)
    except:
        print('%stErrorn' % (cmd))


def pingServer(server):
    ping_result = False
    dead_time = time.time()+80
    while time.time() < dead_time:
        result = os.popen('ping '+server)
        reply = result.read()
        if reply.count('TTL') == 4:
            ping_result = True
            break
        else:
            continue
    if ping_result:
        print('ping %s ok, try to connect ssh' % server)
        ssh2("192.168.1.1", "operator", "123456", "ifconfig wifi0")
    else:
        print('SSH connect fail')
    print(result)


if __name__=='__main__':
    server = '192.168.1.1'
    i = 1
    while i > 0:
        print('#######################', i, '###############################')
        pingServer(server)
        i = i + 1


