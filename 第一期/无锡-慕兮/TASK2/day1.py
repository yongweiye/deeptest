# -*- coding:utf-8 -*-

__author__ = 'liqi'

class Formatting():
    '''
    定义格式化的类
    '''
    def __init__(self,fmat,*data):
        '''
        定义初始参数
        '''
        self.fmat = fmat
        self.data = data

    def set_data(self,data):
        self.data = data

    def old_formatting(self):
        '''文本格式化显示 
        %s：字符串 %d: 十进制整数 %x：十六进制整数 %o：八进制整数
        %f:十进制浮点数 %e: 以科学计数法表示的浮点数
        %%：文本%本身 不能单独使用，要和其他搭配使用 "%s%%" %data
        '''
        fmat = self.fmat
        data = self.data
        try:
            if fmat == "dem":
                fmt = "%d"
            elif fmat == "strg":
                fmt = "%s"
            elif fmat == "oxm":
                fmt = "%o"
            elif fmat == "hexm":
                fmt = "%x"
            elif fmat == "flom":
                fmt = "%f"
            elif fmat == "scim":
                fmt = "%e"
            else:
                print ("没有这个格式哦，请检查")
            print("你的data是"+ fmt %data)
        except Exception as e:
            print("异常，请排查")

if __name__ == "__main__":
    '''主程序入口'''
    data = Formatting("dem", 100)
    # data.set_data(150)
    data.old_formatting()

