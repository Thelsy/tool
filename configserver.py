#!/Users/lsy python
# coding:utf-8
# lsy
# 获取配置文件方法
import configparser
import os
import time
import aes_encrypt as a
from toolif import Server


def configserver():
    # 获取配置信息方法
    try:
        L = []
        cf = configparser.ConfigParser()
        filename = cf.read('config/server.ini')
        ip = cf.get('server', 'ip')
        if ip != '':
            L.append(ip)
            username = cf.get('server', 'user')
            if username != '':
                L.append(username)
                password = cf.get('server', 'password')
                if password != '':
                    L.append(password)

                    return L
                else:
                    raise RuntimeError('密码为空')
            else:
                raise RuntimeError('账号为空')
        else:
            raise RuntimeError('ip为空')
    except Exception as e:
        print(e)
        # 异常时重新记录连接信息
        inputaes()

def file_data(ip, user,password):
    # 写入连接配置方法
    # 获取当前程序目录
    st = os.getcwd()
    stdate = st + '/' +'config/server.ini'
    cf = configparser.ConfigParser()
    filename = cf.read('config/server.ini')
    cf.set("server", 'ip', ip)
    cf.set('server', 'user', user)
    cf.set('server', 'password', password)
    cf.write(open(stdate, 'w'))
    return stdate

def path(path):
    # 写入path路径方法
    try:
        # 获取当前程序目录
        st = os.getcwd()
        stdate = st + '/' + 'config/server.ini'
        cf = configparser.ConfigParser()
        filename = cf.read('config/server.ini')
        if 'workspace' in path:
            cf.set("path", 'workspace_data', path)
            cf.write(open(stdate, 'w'))
        elif 'elasticsearch' in path:
            cf.set("path", 'elas_data', path)
            cf.write(open(stdate, 'w'))
        elif 'file_server' in path:
            cf.set("path", 'file_server_data', path)
            cf.write(open(stdate, 'w'))
        elif 'redis' in path:
            cf.set("path", 'redis_data', path)
            cf.write(open(stdate, 'w'))
        elif 'tomcat' in path:
            cf.set("path", 'tomcat_data', path)
            cf.write(open(stdate, 'w'))
        elif 'zook' in path:
            cf.set("path", 'zook_data', path)
            cf.write(open(stdate, 'w'))
        return stdate
    except Exception:
        print('配置文件异常')

def hot():
    # 解密方法
    try:
        # 获取属性进行解密连接
        cn = configserver()
        L = []
        for i in cn:
            L.append(a.decrypt(i))
        return L
    except Exception:
        print('不是加密配置，请先执行加密')
        inputaes()



def inputaes():
    # 重新记录信息方法
    print('重新记录信息')
    host = input("请输入ip地址：")
    user = input("请输入账号:")
    password = input("请输入密码:")
    Server(host, user, password).copy()

def config():
    # 读取全局配置方法
    try:
        # 获取属性
        cn = configparser.ConfigParser()
        filename = cn.read('config/server.ini')
        return cn
    except Exception:
        print('配置文件异常，请检查')


def outpath(path, name):
    # 接收用户选择并读取配置方法
    try:
        cn = configparser.ConfigParser()
        filename = cn.read('config/server.ini')
        cmd = cn.get(path, name)
        return cmd
    except Exception:
        print('配置异常,重新记录')
        return None

def yyuser():
    try:
        L = []
        cf = configparser.ConfigParser()
        filename = cf.read('config/server.ini')
        yyuser = cf.get('yyuser', 'yyuser')
        L.append(yyuser)
        yyuser_password = cf.get('yyuser', 'yyuser_password')
        L.append(yyuser_password)
        return L
    except Exception:
        print()


