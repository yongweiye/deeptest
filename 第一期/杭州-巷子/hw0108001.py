#! -*- coding:utf-8 -*-

# author
__author__ == "author"

import random


class MySort:

    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count

    def mysort(self):
        a = []
        '''
        生成一个随机数组列表
        '''
        for i in range(self.count):
            c = random.randint(self.start, self.end)
            a.append(c)
        '''
        每个值不断和后面一个值做比较，最大的值放到最末
        '''
        for i in range(self.count - 1):
            for j in range(i, self.count - 1):
                if a[j + 1] < a[i]:
                    a[i], a[j + 1] = a[j + 1], a[i]
        return a


if __name__ == '__main__':
    sorted_data = MySort(1, 100, 10)
    print(sorted_data)
