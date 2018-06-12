#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 0:45
# @Author  : caijiangchun
# @Site    : 
# @File    : two_sum.py
# @Software: PyCharm
class TwoSum(object):

    #数据初始化
    def __init__(self, a , b ):

        self.a = a
        self.b = b

    #加法
    def add(self):
        return self.a + self.b

    #减法
    def sub(self):
        return self.a - self.b

    #乘法
    def mul(self):
        return self.a * self.b

    #除法
    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error"
     #重置数据
    def reset(self, a, b):
        self.a = a
        self.b = b

def testone(TwoSum):

    add = TwoSum.add()
    sub = TwoSum.sub()
    mul = TwoSum.mul()
    div = TwoSum.div()
    print(add, sub, mul, div)

if __name__ == "__main__":
    n = 1
    while n == 1:
        try:
            a = int(input("请输入第一个数："))
            b = int(input("请输入第二个数："))
        except ZeroDivisionError:
            raise ValueError("inputerror")

        finally:
            print("try again")

        TwoSum = TwoSum(a, b)
        testone(TwoSum)




