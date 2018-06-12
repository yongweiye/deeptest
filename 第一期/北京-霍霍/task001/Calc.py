# -*- coding:utf-8 -*-

__author__= "huohuo"

import random

class CalCu:
    """
    实现一个四则运算的类，要求实现任意两个数的加减乘除运算
    """
    def __init__(self):
        #初始化
        print("初始化")
  
    def add(self, a, b):
        #加法
        return a + b

    def subtract(self, a, b):
        # 减法
        return a - b

    def multiply(self, a, b):
        # 乘法
        return a * b

    def divide(self, a, b):
        # 除法
        return a / b

class Short:

    def __init__(self):
        #初始化
        print("排序初始化")

    def paixu(self):

        a_list = range(10, 1000)
        b_list = random.sample(a_list, 100)
        print("排序前：")
        print(b_list)
        print("排序后：")
        for i in range(100):
            for j in range(1, 100 - i):
                if b_list[j - 1] > b_list[j]:
                    b_list[j - 1], b_list[j] = b_list[j], b_list[j - 1]
        print(b_list)




if __name__=="__main__":
    """
    主函数入口
    """
    a = CalCu()

    print("第一个数要大于第二个数！")

    num1 = int(input("第一个数字："))
    num2 = int(input("第二个数字："))

    print("函数调用")
    print("和：", a.add(num1,num2))
    print("差：", a.subtract(num1,num2))
    print("积：", a.multiply(num1,num2))
    print("商：", a.divide(num1,num2))

    b = Short()
    b.paixu()


