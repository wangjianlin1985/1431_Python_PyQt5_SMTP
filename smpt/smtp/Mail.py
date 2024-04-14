import smtplib#邮箱发送程序的核心库
import configparser#用来管理配置文件的库
import os


class MailConfig:
    def __init__(self):
        # yagmail库基本参数设置
        self.config = configparser.ConfigParser()
        self.config.read('D:\smpt\MailConfig.ini',encoding='utf8')  # 读取配置文件,文件路径最好为绝对路径，程序打开前需保证该文件存在打开，程序后按相应功能可重新生成初始化配置文件
        self.smtpConfig=self.config['DEFAULT'];

        self.user = self.smtpConfig["user"]  # 对应自己的邮箱账号
        self.password = self.smtpConfig['password']  # 对应自己邮箱申请的服务密码，博客有介绍步骤的链接，不是自己邮箱的登录密码
        self.port = self.smtpConfig['port']  # 邮箱服务器端口,qq邮箱固定此端口465
        self.host = self.smtpConfig['host']  # 对应自己邮箱服务的服务器地址,qq邮箱固定此地址smtp.qq.com
        print(self.host)
        print(self.port)
        #self.mail = smtplib.SMTP(user, password, host, port)  # yagmail库初始化实例
        # 为了保证程序代码的安全性和移植性，在程序同目录下，打开配置文件（手动或程序功能上打开），填写好配置信息即可


    @staticmethod
    def creatconfig():  # 恢复成默认的配置文件的方法
        config=configparser.ConfigParser();
        config['DEFAULT'] = {'user': 'user',
                                  'password': 'password',
                                  'port': 'port',
                                  'host': 'hosts'
                                  }
        with open('MailConfig.ini', 'w+') as configfile:  # 向配置文件写入默认配置，相当恢复出厂设置！
            config.write(configfile)

    def openconfig(self):  # 程序上自动打开配置文件的方法
        os.startfile('MailConfig.ini')

