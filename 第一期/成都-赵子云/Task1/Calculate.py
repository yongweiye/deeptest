# -*- coding:utf-8 -*-
import sys

class Calc:
    '''
    一个四则运算的类，实现任意两个数的加减乘除运算。
    '''
    # 初始化
    def __init__(self, *args):
        if len(args) == 2:
            for i in args:
                try:
                    float(i)
                except ValueError:
                    print('您输入有误，您输入的参数包含非数字...')
                    sys.exit()
            self.a = args[0]
            self.b = args[1]
        else:
            print("您输入有误，请输入两个数字...")
            sys.exit()

    # 加法
    def add(self):
        result = self.a + self.b
        return result

    # 减法
    def sub(self):
        result = self.a - self.b
        return result

    # 乘法
    def mul(self):
        result = self.a * self.b
        return result

    # 除法
    def div(self):
        try:
            result = self.a/self.b
            if not self.a % self.b:
                result = int(result)
            return result
        except ZeroDivisionError:
            print("您好，被除数不能为零哦")
if __name__ == '__main__':
    calc = Calc(25)
    print('和：', calc.add())
    print('差：', calc.sub())
    print('积:', calc.mul())
    print('商:', calc.div())

