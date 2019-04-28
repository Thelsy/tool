#!/Users/lsy python
# coding:utf-8
# lsy
# 进入主方法
import configserver as co
import inputout as out
from toolif import Server as s

if __name__ == '__main__':
    print('''                               ***请选择启动节点***
#############################################################################################
                                                                                           
       1、workspace     2、tomcat    3、hadoop    4、es        n、修改配置信息                          
                                                                                           
       5、fileserver    6、zook      7、redis     8、pull      10、all(所有服务)              
                                                                                          
#############################################################################################
''')
# 验证配置连接是否为空
co.configserver()
# 验证配置连接是否为加密
co.hot()
# 初始化

# 接收用户选择
out.inputstr()
