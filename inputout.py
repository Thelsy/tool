#!/Users/lsy python
# coding:utf-8
# lsy
# 记录用户选择
import sys
import logging
import configserver as co
import server as ser
import time

def inputstr():
    while True:
        try:
            out = input('请选择启动项：')
            if out == '1':
                print('启动workspace')
                if co.outpath('path', 'workspace_data') != None and co.outpath('path', 'workspace_data') != '':
                    print()
                else:
                    path = co.outpath('public', 'path')
                    path1 = co.outpath('public', 'path1')
                    print(path+' '+'workspace'+''+path1)
                    so = ser.servcer(path+' '+'workspace'+''+path1)
                    work = so.strip().split(':')
                    cn = co.path(work[1].lstrip())
            elif out == '2':
                print('启动tomcat')
                if co.outpath('path', 'tomcat_data')!= None and co.outpath('path', 'tomcat_data') != '':
                    # 不为空则继续
                    print()
                else:
                    # 为空则重新记录然后继续
                    path = co.outpath('public', 'path')
                    path1 = co.outpath('public', 'path1')
                    print(path + ' ' + 'apache-tomcat' + '' + path1)
                    so = ser.servcer(path + ' ' + 'apache-tomcat' + '' + path1)
                    tomcat = so.strip().split(':')
                    cn = co.path(tomcat[1].lstrip())
            elif out == '3':
                print('启动hadoop')
                ser.servcer()
            elif out == '4':
                print('启动es')
                if co.outpath('path', 'elas_data') != None and co.outpath('path', 'elas_data') != '':
                    print()
                else:
                    path = co.outpath('public', 'path')
                    path1 = co.outpath('public', 'path1')
                    print(path + ' ' + 'elasticsearch' + '' + path1)
                    so = ser.servcer(path + ' ' + 'elasticsearch' + '' + path1)
                    elas = so.strip().split(':')
                    cn = co.path(elas[1].lstrip())
            elif out == 'n':
                print('修改配置信息')
                co.inputaes()
            elif out == '5':
                print('启动文件服务器')
                if co.outpath('path', 'file_server_data') != None and co.outpath('path', 'file_server_data') != '':
                    print()
                else:
                    path = co.outpath('public', 'path')
                    path1 = co.outpath('public', 'path1')
                    print(path + ' ' + 'node' + '' + path1)
                    so = ser.servcer(path + ' ' + 'node' + '' + path1)
                    file_server = so.strip().split(':')
                    cn = co.path(file_server[1].strip())
                    print(so)
            elif out == '6':
                print('启动zook')
                if co.outpath('path', 'zook_data') != None and co.outpath('path', 'zook_data') != '':
                    print()
                else:
                    path = co.outpath('public', 'path')
                    path1 = co.outpath('public', 'path1')
                    print(path + ' ' + 'zookeeper' + '' + path1)
                    so = ser.servcer(path + ' ' + 'zookeeper' + '' + path1)
                    zook = so.strip().split(':')
                    cn = co.path(zook[1].lstrip())
            elif out == '7':
                print('启动redis')
                if co.outpath('path', 'redis_data')!= None and co.outpath('path', 'redis_data') != '':
                    print()
                else:
                    path = co.outpath('public', 'path')
                    path1 = co.outpath('public', 'path1')
                    print(path + ' ' + 'redis' + '' + path1)
                    so = ser.servcer(path + ' ' + 'redis' + '' + path1)
                    redis = so.strip().split(':')
                    cn = co.path(redis[1].lstrip())
                    print(ser.servcer('ps -ef |grep ' + '' + cn))
            elif out == '8':
                print('启动pull')
                print('开发中')
                ser.servcer()
            elif out == '9':
                print('启动mysql')
                chown = co.outpath('public', 'chown')
                stop = co.outpath('mysql', 'mysql_stop')
                start = co.outpath('mysql', 'mysql_start')
                kill = co.outpath('public', 'kill')
                kill1 = co.outpath('public', 'kill1')
                print(chown + ';' + stop + ';' + start)
                so = ser.servcer(chown+' '+'*')
                so = ser.servcer(stop)
                so = ser.servcer(start)
                print(ser.servcer(kill + ' ' + 'mysql' + ' ' + kill1))
                print(ser.servcer('ps -ef |grep mysql'))
            elif out == '10':
                print('启动所有节点')
                print('开发中')
                ser.servcer()
            elif out == 'exit':
                logging.warning('退出')
                sys.exit()
            elif out == 'jm':
                print('获取当前配置信息')
                xi = co.hot()
                for i in xi:
                    print(i, end=' ')
                print()
            else:
                print('无效输入，请重新输入')
        except Exception :
            print('请修改配置信息后重新操作')