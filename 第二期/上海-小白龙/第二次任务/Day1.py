#!/usr/bin/python
#encoding=utf-8
import math
import random
import cmath

__author__=u'小白龙'
class Numbers:
    def mathFuc(self):
        print(math.sqrt(9))#求平方
        print(math.fabs(-5))
        print(math.pi)#pai
        print(math.log10(100))
    def randomFuc(self):
        print(random.randint(1,10))#返回int数值
        print(random.random())#返回0-1之间的float型数值
        print(random.choice([u"小白龙",u"慧慧",u"五娃"]))#Return a random element from the non-empty sequence seq
    def cmathFuc(self):
        print(cmath.cos(45))
        print(cmath.log10(100))
        print(cmath.e)
class Strings:
    pass
if __name__=="__main__":
    x = 12.83
    y = 3
    print(x)
    print(y)
    print(int(x))
    print(float(y))
    print(complex(x,y))
    print("==========math==========")
    num = Numbers()
    num.mathFuc()
    print("==========random==========")
    num.randomFuc()
    print("==========cmath==========")
    num.cmathFuc()