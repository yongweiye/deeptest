# -*- coding: utf-8 -*-
import random

class Calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __check__(self):
        if type(self.a) != int or type(self.b) != int:
            return "参数输入的非数字,请重新输入"
    def add(self):
        if self.__check__():
            return self.__check__()
        else:
            return self.a + self.b
    def sub(self):
        if self.__check__():
            return self.__check__()
        else:
            return self.a - self.b
    def mul(self):
        if self.__check__():
            return self.__check__()
        else:
            return self.a * self.b
    def div(self):
        if self.__check__():
            return self.__check__()
        else:
            return self.a / self.b

print (Calc("1",2).add())
print (Calc(1,2).sub())
print (Calc(1,2).mul())
print (Calc(1,2).div())

class MySort(object):
    def __init__(self,start,end,count):
        self.start = start
        self.end = end
        self.count = count
    def mysort(self):
        data = []

        for i in range(self.count):
            data.append(random.randint(self.start,self.end))
        for i in range(len(data)-1):
            for j in range(len(data)-i-1):
                if data[j] > data[j+1]:
                    data[j],data[j+1] = data[j+1],data[j]

        return str(data)
    def __str__(self):
        return self.mysort()
if __name__ == "__main__":
    data = MySort(10,100,10)
    print(data)
