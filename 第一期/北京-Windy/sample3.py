#!/usr/bin/env  python
# -*- coding: UTF-8 -*-
class Sample3:
    '''一个数加100后是一个完全平方数，再加上168还是一个完全平方数，请问这个数是多少'''

    def mySam(self):
        arr=[]
        for i in range(1,100):
            if 168%i==0:
                j=168/i
                if i>j and (i+j) %2 == 0 and (i-j) %2 ==0:
                    m=(i+j)/2
                    n=(i-j)/2
                    x=m*n-100
                    arr.append(x)
        return arr


if __name__=='__main__':
    sam=Sample3()
    q=sam.mySam()
    print(q)
