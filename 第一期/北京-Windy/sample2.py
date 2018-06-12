#!/usr/bin/env  python
# -*- coding: UTF-8 -*-
class Sample2:
    '''根据不同的利润和奖励梯度，计算奖金'''

    def __init__(self,profit):
        self.profit=profit

    def salary(self):

        if(self.profit<100000):
            salary=self.profit*0.1
        elif(self.profit>=100000 and self.profit<200000):
            salary=(self.profit-100000)*0.075+100000*0.1
        elif(self.profit>=200000 and self.profit<400000):
            salary=(self.profit-200000)*0.05
        elif (self.profit >= 400000 and self.profit < 600000):
            salary = (self.profit - 400000) * 0.03
        elif (self.profit >= 600000 and self.profit < 1000000):
            salary = (self.profit - 600000) * 0.015
        elif (self.profit >= 1000000 ):
            salary = (self.profit - 1000000) * 0.01
        return salary


if __name__=='__main__':
    print("请输入利润：",end=' ')
    myPro=Sample2(int(input()))
    mySal=myPro.salary()
    print('%.2f'%mySal)
