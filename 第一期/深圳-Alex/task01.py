# -*- coding:utf-8 -*-

__author__ = 'AlexZz2'

import random

'''
    实现一个四则运算的类
    要求：实现两个数的加减乘除运算
'''
class Calc:
    # 初始化
    def __init__(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError('bad operand type!')
        self.a = a
        self.b = b
    
    # 实现加法运算
    def add(self):
        return self.a+ self.b

    # 实现减法运算
    def sub(self):
        return self.a- self.b

    # 实现乘法运算
    def mul(self):
        return self.a* self.b

    # 实现除法运算
    def div(self):
        try:
            return self.a/ self.b
        except ZeroDivisionError as e:
            print('Division is Zero!')
            raise

'''
    随机生成count个start~end之间的数，并对生成的count个数进行排序
'''
class MySort:
    '''
        start, end  随机数范围
        count   生成的随机数的个数
    '''
    def __init__(self, start, end, count):
        if not(isinstance(start, (int, float))):
            raise TypeError('bad operand type!')
        elif not (isinstance(end, (int, float))):
            raise TypeError('bad operand type!')
        elif not(isinstance(count, (int))):
            raise TypeError('bad operand type!')
        else:
            self.start = start
            self.end = end
            self.count = count
            self.a = []
        # 生成若干个指定范围的随机数并添加入列表中
        if self.count <= 0:
            print('不生成随机数!')
        else: 
            for i in range(self.count):
                self.a.append(random.uniform(self.start, self.end))
            print(self.a)

    # 实现排序功能并返回列表
    def __mysort__(self):
        for i in range(len(self.a)):
            for j in range(len(self.a)-i-1):
                if self.a[j] > self.a[j+1]:
                    self.a[j], self.a[j+1] = self.a[j+1], self.a[j]
        return self.a
             
if __name__ == '__main__':
    # Clac对象实例化
    result = Calc(4, 2)
    print('四则运算结果：', result.div())
    # MySort对象实例化
    print('初始化：')
    mylist = MySort(1, 10, 3)
    print('排序后：\n{0}'.format(mylist.__mysort__()))
    