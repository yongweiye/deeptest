#!/usr/bin/env python
#__author__ = '北京-Windy'
import random
class Sort:
    def __init__(self,start,end,count):
        self.start=start
        self.end=end
        self.count=count
    def __MySort__(self):
        mylist=random.sample(range(self.start,self.end),self.count)
        for i in range(len(mylist)):
            for j in range(i):
                if mylist[j]>mylist[j+1]:
                    mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
        return mylist


if __name__=='__main__':
    sort_list=Sort(10,1000,100)
    sort_data=sort_list.__MySort__()
    sum=0
    for a in sort_data:
        print('%3d'%a,end=' ')
        sum+=1
        if(sum%10==0):
            print(end='\n')
