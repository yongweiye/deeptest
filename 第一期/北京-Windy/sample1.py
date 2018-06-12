#!/usr/bin/env  python
# -*- coding: UTF-8 -*-
class Sample1:
    '''有1,2,3,4四个数，能组成多少个不同且不重复的三位数。'''
    #初始化
    def __init__(self,mylist=[]):
        self.mylist=mylist
    def san(self):
        count=[]
        for i in range(1,5):
            for j in range(1,5):
                for k in range(1,5):
                    if i!=j and j!=k and i!=k:
                        count.append(i*100+j*10+k)
        return count


if __name__=='__main__':
    mySan=Sample1([1,2,3,4])
    shu=mySan.san();
    he=0
    for i in shu:
        print(i, end=" ")
        he+=1
        if(he%4==0):
            print(end="\n")
            #print(he)
    print('能组成的三位数个数为：%d'%he)

