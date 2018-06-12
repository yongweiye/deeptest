#!-*- coding:utf-8 -*-
__author__ = 'ALX LIN'

class Calc():
    #初始化对象
    def __init__(self, a, b):
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
        if self.b == 0:
            return "除数不能为0"
        else:
            return self.a/self.b
