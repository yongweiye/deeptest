# -*- coding: UTF-8 -*-
# @Date     : 2018-01-08 23:56
import random
class MySort:
    #初始化
    def __init__(self,start,end,count):
        self.start = start
        self.end = end
        self.count = count
    def mysort(self):
        if type(self.start) != int or type(self.count) != int or type(self.end) != int:
            raise Exception("参数必须为int型！")
        if self.start > self.end:
            raise Exception("起始数不能大于终止数！")
        #生成数字列表，并排序
        testa = []
        for i in range(self.count):
            testa.append(random.randint(self.start,self.end))
        #从大到小排序列表
        for i in range(self.count):
            for j in range(i):
                if testa[j] < testa[j+1]:
                    temp = testa[j]
                    testa[j] = testa[j+1]
                    testa[j+1] = temp
        return testa
#使用示例
if __name__ == '__main__':
    sorted_Data = MySort(10,1000,100).mysort()
    #打印排序后的结果
    print(sorted_Data)