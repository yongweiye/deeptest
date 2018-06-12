#  -*- coding:utf-8 -*-

__author__ = u'linan'

if __name__ == "__main__":
    x = 1.68
    y = 10

    #将x转换为整数
    print(int(x))

    #将y转为浮点数
    print(float(y))

    #将x转换为复数，实数部分为x,虚数部分为0
    print(complex(x))

    #将x，y转换为复数，实数部分为x,实数部分为y
    print(complex(x,y))

#执行结果如下：
#1
#10.0
#(1.68+0j)
#(1.68+10j)

__author__ = u'linan'

import math
import cmath
import random

if __name__ == "__main__":
    x = -100
    y = 1.9

    print(u"常用数学函数")
    
    #返回x绝对值
    print(abs(x))

    #返回最大值
    print(max(x,y))

    #返回最小值
    print(min(x,y))

    #计算y^2
    print(pow(x,y))

    #返回平方根
    print(math.sqrt(y))

    print(u'常用随机函数')
    a = [1,2,3,4,5,6,7,8,9,0]

    #从a列表中随机选中一个数
    print(random.choice(a))

    #从指定的范围（2-100按5递增的数据集）中随机选择一个
    print(random.randrange(2,100,5))

    #生成一个数，使它在0和1之间
    print(random.random())

    print(u'常用三角函数')
    x = 100
    
    #返回x的反余弦弧度值
    print(cmath.acos(x))

    #返回x正弦弧度值
    print(cmath.sin(x))

    #返回x的余弦弧度值
    print(cmath.cos(x))

    print(u'数学常亮')

    #返回π
    print(cmath.pi)   
