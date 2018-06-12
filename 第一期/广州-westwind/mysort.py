#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 20:48
# @Author  : caijiangchun
# @Site    : 
# @File    : mysort.py
# @Software: PyCharm
import random


#随机生成100个10至1000之间的数，对生成的100个数进行排序
class Mysort():

    def __init__(self, start, end, count):

        self.start = start
        self.end = end
        self.count = count
        self.data = []
    #生成随机数
    def __randomnumber(self):

        self.data = [random.randint(self.start,self.end) for i in range(self.count)]

    #冒泡排序，从小到大排
    def mysort(self):

        self.__randomnumber()

        n = len(self.data)

        for i in range(n):
            for j in range(1, n - i):
                if self.data[j - 1] > self.data[j]:
                    self.data[j - 1], self.data[j] = self.data[j], self.data[j - 1]
        return self.data


if __name__ == "__main__":

    sortdata = Mysort(10, 1000, 100)
    dataone = sortdata.mysort()
    d = []
    for i in dataone:
        d.append(i)
    print(d)
    a = [random.randint(10, 1000) for i in range(100)]

    #调试
    n = len(a)

    for i in range(n):
        for j in range(1, n - i):
            if a[j-1]>a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    print(a)


