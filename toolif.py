#!/Users/lsy python
# coding:utf-8
# lsy
# 条件控制
import configparser
import aes_encrypt as a
import configserver as co
class Server(object):
    def __init__(self, host, user, password):
        # 初始化属性
        self.host = host
        self.user = user
        self.password = password

    # 配置更新加密方法
    def copy(self):
        # 获取属性执行加密，并写入配置文件，如
        ip = a.encrypt(self.host)
        username = a.encrypt(self.user)
        password = a.encrypt(self.password)
        co.file_data(ip, username, password)


