# -*- coding:utf-8 -*-
import random
'''
随机生成100个10至1000之间的数，对生成的100个数进行排序，禁止使用Python自带的排序函数，要自己实现排序函数
class MySort:
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # count为生成的随机数个数
    def __init__(self, start, end，count):
        pass

    # 实现排序，内部函数
    def __mysort__(selg):
        pass

# 使用示例
if __name__ == "__main__":
    sorted_data = MySort(10， 1000， 100)
    # 打印排序后的结果
    print(sorted_data)
'''
class MySort(object):
    '''
    生成随机数,返回排序后的结果
    start, end为限制随机数生成的范围
    count为生成的随机数个数
    '''
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.randomList = []
        for i in range(self.count):
            self.randomList.append(random.randint(self.start, self.end))
        print(self.randomList)
        print(self.__mysort__())

    def __mysort__(self):
        count = len(self.randomList)
        for i in range(count):
            for j in range(i+1, count):
                if self.randomList[i] > self.randomList[j]:
                    self.randomList[i], self.randomList[j] = self.randomList[j], self.randomList[i]
        return self.randomList

if __name__ == '__main__':
    mysort = MySort(10, 1000, 100)
