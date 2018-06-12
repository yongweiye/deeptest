#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 23:47
# @Author  : caijiangchun
# @Site    : 
# @File    : numbers.py
# @Software: PyCharm

#数分为整数，长整数，浮点数和复数

def  number_int():
    #整数
    a = 2
    b = 3
    c = a + b
    return c

def number_float():
    #浮点数
    a  = 12.0
    b = 333.99
    c = a * b
    #计算9的n次方
    f = 9 ** 8
    e = 1.2e2
    return c, e, f

def number_complex():
    #复数
    a = 9 + 2j
    return a

if __name__ == "__main__":

    a = number_int()
    #a的值
    print(a)
    #a的数据类型
    print(type(a))

    b = number_float()
    # b的值
    print(b)
    # b的数据类型
    print(type(b))

    c = number_complex()
    #c的值
    print(c)
    #c的数据类型
    print(type(c))
