#!/usr/bin/env python
class Sample4:

    '''输入某年某月某日，判断这一天是这一年的第几天'''

    #初始化
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    #判断是这一年中的哪一天
    def cal(self):
        arr1 = (0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 336) #闰年
        if( 0<self.month <=12):
            dth=arr1[self.month-1]
        else:
            print("输入错误，请重新输入！")

        dth+=self.day
        leap=0
        if(self.year%400==0) or ((self.year%4==0) and (self.year%100!=0)):
            leap=1
        if(leap==1) and (self.month>2):
            dth+=1

        return dth


if __name__=='__main__':
    print("请分别输入年、月、日：")
    mySam=Sample4(int(input()),int(input()),int(input()))
    dt=mySam.cal()
    print(dt,"天")

