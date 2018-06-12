#!-*- coding:utf-8 -*-
__author__ = 'ALX LIN'
import random

class MySort():
    #初始化对象
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
    #获取生成count个数组成的列表
    def get_number(self):
        list = []
        flag = 0
        while flag < self.count:
            a = random.randint(self.start, self.end)
            list.append(a)
            flag += 1
        return list
    #冒泡排序
    def mysort(self):
        list = self.get_number()
        for i in range(len(list)-1):
            for j in range(len(list)-i-1):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]
        print(list)



if __name__ == '__main__':
    sorted_data = MySort(10, 100, 10)
    print(sorted_data.mysort())#打印排序结果