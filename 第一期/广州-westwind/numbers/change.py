#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 1:05
# @Author  : caijiangchun
# @Site    : 
# @File    : change.py
# @Software: PyCharm
import math
import cmath
import random

def change():

    x = 1.08
    y = 333

    #将x转为整型
    print(int(x))
    # 将y转为浮点数
    print(float(y))
    # 将x转为复数
    print(complex(x))
    print(complex(x, y))

def math_numbers():
    x = -1000
    y = 1.5
    print(abs(x))
    print(max(x ,y))
    print(min(x ,y))
    #计算y的平方
    print(pow(y, 2))

    g = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    #从列表中随机选择一个
    print(random.choice(g))
    print(random.randrange(1 ,100, 8))

    #圆周率
    x = math.pi
    print(x)
    x = 100
    print(cmath.sin(x))


if __name__ == "__main__":
    change()
    math_numbers()