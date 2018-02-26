# -* coding:utf-8 *-
__author__ = 'nancy'

import configparser
import os

# ini文件操作类
class iniconf():
    def __init__(self,inipath):
        self.inipath  = inipath
        if os.path.exists(self.inipath):
            self.cf = configparser.ConfigParser()
            self.cf.read(self.inipath, "utf-8")
        else:
            raise "file not exit"

    def get_conf_data(self, section):
        '''
        获取配置文件指定section下全部内容
        :param section: 待获取的section
        :return: 以字典形式返回section全部参数
        '''
        try:
            cfData = {}
            for val in self.cf.options(section):
                cfData[val] = self.cf.get(section, val)
            return cfData
        except Exception as e:
            print(e)
