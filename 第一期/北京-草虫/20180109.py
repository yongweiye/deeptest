#! -*- coding:utf-8 -*-


import random

#实现一个基础运算功能

class operation:
    #初始化
    def __init__(self,a,b):
        self.a=a
        self.b=b

    #计算两个数相加
    def add(self):
        return self.a+self.b
        
    #计算两个数相减
    def sub(self):
        return self.a-self.b

    #计算两个数相乘
    def mul(self):
        return self.a*self.b

    #计算两个数相除
    def div(self):
        return self.a/self.b

#随机产生100个10-1000 个随机数，并对其进行排序       
class red:
    def __init__(self,sm,max,count):
        self.sm=sm              #初始化随机数最小值
        self.max=max            #初始化随机数最大值
        self.count=count        #初始化生成随机数的数量
        self.randlist=[]        #初始化储存生成的随机数数组
        lists=self.randlist     #将定义的数据保存到lists中，方便后面使用时书写简单方便
        for i in range(self.count):         #使用for循环随机产生count个随机数
            lists.append(random.randint(self.sm,self.max))
        print("排序前数据:",lists)

        #对生成的随机数进行排序，调用下方的red
        self.__red__()
        
    #对生成的随机数进行冒泡排序
    def __red__(self):
        lists=self.randlist
        count = len(lists)
        for i in range(count):
            for j in range(i+1, count):
                if lists[i] > lists[j]:
                    lists[i], lists[j] = lists[j], lists[i]
        print("排序后结果：",lists) 

if __name__ == "__main__":
    #四则运算
    result=operation(4,2)
    print("a+b=",result.add())
    print("a-b=",result.sub())
    print("a*b=",result.mul())
    print("a/b=",result.div())
    
    #100位随机数排序
    red(10,1000,100)
    
   