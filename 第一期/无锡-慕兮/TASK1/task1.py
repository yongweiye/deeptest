#! -*- coding:utf-8 -*-

#！__author__ == "无锡-慕兮"

import random

class Calc:
    '''
        实现任何两个数的加、减、乘、除
    '''
    def __init__(self, a, b):
        '''
        定义参数
        :param a: 
        :param b: 
        '''
        self.a = a
        self.b = b

    def set(self, a, b):
        '''
        重置a b
        '''
        self.a = a
        self.b = b

    def __add__(self):
        '''
        实现两个数的加操作并返回和
        '''
        try:
            if float(self.a) or float(self.b):
                return self.a + self.b
        except ValueError:
            return ("这是数字的加法运算，请重新输入数字")
        except Exception as others:
            return ("其他错误，请告诉程序员这是加法的锅", others)

    def __sub__(self):
        '''
        实现两个数的减操作并返回差 
        '''
        try:
            return self.a - self.b
        except TypeError:
            return ("这是数字的减法运算，请重新输入数字")
        except Exception as others:
            return ("其他错误，请告诉程序员这是减法的锅", others)

    def __mul__(self):
        '''
        实现两个数的乘操作，并返回积 
        '''
        try:
            if float(self.a) or float(self.b):
                return self.a * self.b
        except ValueError:
            return ("这是数字的乘法运算，请重新输入数字")
        except Exception as others:
            return("其他错误，请告诉程序员这是乘法的锅", others)

    def div(self):
        '''
        实现两个数的除操作，并返回商
        :return: 
        '''
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return ("被除数不能为零，请重新输入")
        except TypeError:
            return ("这是数字的除法运算，请重新输入数字")
        except Exception as others:
            return ("其他错误，请告诉程序员这是除法的锅", others)


######################################################################


class MySort():
    '''
    随机生成100个10至1000之间的数，对生产的100个数进行排序
    '''
    def __init__(self, start, end, count):
        '''
        :param start: 限制随机数生产的范围
        :param end: 生成随机数生产的范围
        :param count: 生成的随机数个数
        :mylist为生成的随机数组成的列表
        '''
        self.start = start
        self.end = end
        self.count = count
        self.mylist = []

        if type(count) != int:
            raise Exception("count 应为整数")
        elif start > end:
            raise Exception("开始数字要小于结束数字")
        else:
            mycount = 0
            while mycount < self.count:
                value = random.uniform(self.start, self.end)
                mycount = mycount + 1
                self.mylist.append(value)
            self.__mysort__()
            print(self.mylist)


    def __mysort__(self):
        '''
        使用冒泡法排序
        '''
        # mycount = self.count
        # for i in range(0, mycount):
        #     for j in range(i + 1, mycount):
        #         if self.mylist[i] > self.mylist[j]:
        #             self.mylist[i], self.mylist[j] = self.mylist[j], self.mylist[i]

        '''
        使用插入法排序, 从小到大排序
        '''
        for i in range(1, self.count):
            value = self.mylist[i]
            j = i - 1
            while j >= 0 and self.mylist[j] > value:
                self.mylist[j + 1] = self.mylist[j]
                j -= 1
            self.mylist[j + 1] = value















if __name__ == "__main__":
    '''主函数入口'''
    # a = input("请输入第1个数据：")
    # b = input("请输入第2个数据：")
    # calc = Calc(a, b)
    # calc_result = calc.__add__()
    # print(calc_result)

    myso = MySort(10, 1000, 100)
    print(myso)

