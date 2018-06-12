# -*- coding:utf-8 -*-
import math
import random

import cmath

__author__ = 'beck'

if __name__ == '__main__':
#数据类型转换
    x=1.68
    y=10
    print(int(x))
    print(float(y))
    print(complex(x))
    print(complex(x,y))

#常用数学函数
    i=-100
    j=8.89

    print(abs(i))
    print(pow(j,2))#求j的2次方的值
    print(math.sqrt(j))
    print(min(i,j))
    print(max(i,j))

#随机函数
    print(u"常用随机函数")
    a = ['uie',2,4,5,6,7,'yui','ywe','yuwe783iop']
    print(random.choice(a))#从序列中随机获取到一个元素，序列可以是list，tuple

    print(random.random()) #输出0-1的浮点数
    print(random.randrange(10,20,2))#生成指定范围内的按一定长度的数
    print(random.uniform(10,20))#指定范围内的随机浮点数
    print(random.uniform(20,10))
    random.shuffle(a) #将a中的元素打乱
    print(a)

    list=['test','001',2,3,7,9,'testone','tet','uisfs']
    newlist = random.sample(list,3)#随机截取3个长度的元素组成一个片断并返回，新序列无序，原序列有序且不变
    print(newlist)
    print(list)

#三角函数
    q=99
    print(cmath.sin(q))
    print(cmath.cos(q))
    print(cmath.asin(q))
    print(cmath.pi)