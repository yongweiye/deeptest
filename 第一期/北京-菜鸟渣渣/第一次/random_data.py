# coding=utf-8

import random

'''
    随机生成100个10至1000之间的数，对生成的100个数进行排序，
    禁止使用Python自带的排序函数，要自己实现排序函数
'''

class NumSort:

    def __init__(self,start,end,count):
        self.start=start
        self.end=end
        self.count=count

        self.numList =[]

    def generatData(self):

        for i in range(1,self.count,1):
            self.numList.append(random.uniform(self.start,self.end))


    def sort(self):

        self.generatData()
        print
        print "打印排序之前列表数据\n",self.numList
        for i in range(len(self.numList)-1,0,-1):

            for j in range(0,i,1):

                if self.numList[j]>self.numList[j+1]:
                    self.numList[j],self.numList[j+1]=self.numList[j+1],self.numList[j]

        return  self.numList


if __name__ == "__main__":
    initData=NumSort(10,1000,100)
    sort_data=initData.sort()
    print "打印排序之后的列表数据\n",sort_data
    #迭代器使用
    item_data=[x*2 for x in sort_data]
    print "打印迭代器生成的数据"
    print item_data
