#!/Users/lsy python
# coding:utf-8
# lsy
# linux连接
import configserver as co
import logging
import paramiko
import time
import sys

def servcer(cmd):
    '''连接操作服务器'''
    try:
        pz = co.hot()
        hostname = pz[0]
        username = pz[1]
        password = pz[2]
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, 22, username, password, compress=True, timeout=5)
        time.sleep(3)
        print(hostname + '&' + username + '&' + '连接成功')
        while True:
            print(cmd)
            stdin, stdout, stderr = client.exec_command(cmd)
            # stdin.write('Y')
            out = stdout.read()
            if not out:
                out = stderr.read()
            client.close()
            stt = out.decode()
            return stt
    except Exception as e:
        print('连接失败请检查账号密码:' + '&' + str(e))


def logout(cmd):
    if 'exit' in cmd:
        logging.warning('退出')
        time.sleep(1)
        sys.exit()


def warning(cmd):
    if 'rm -rf ' in cmd:
        logging.warning('警告删除操作!请检查命令')
        print(cmd)
        s = input('请确认是否删除(y/n)')
        if s == 'y':
            time.sleep(1)
        else:
            logging.warning('退出')
            sys.exit()

