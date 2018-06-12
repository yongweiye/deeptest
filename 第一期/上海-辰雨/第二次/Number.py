#!/usr/bin/env python
# encoding: utf-8
import math
import cmath
import random
#将数值转换为各种类型的数据
__author__='上海-辰雨'


x = 1.68
y = 10

#将x 转换为整数
print (int(x))

#将y转换为浮点数
print (float(y))

#将x 转换为复数，实数部分为x ,虚数部分为0
print (complex(x))

#将x,y 转换为复数，实数部分为x ,虚数部分为y
print (complex(x,y))


#四类常用的数值处理函数实例演示：
if __name__ == "__main__":
	x = -100
	y = 1.9

	print (u'常用数学函数')
	#返回x 的绝对值
	print (abs(x))

	#返回最大值：
	print (max(x,y))

	#返回最小值：
	print (min(x,y))

	#计算y^2
	print (pow(y,2))

	#返回平方根
	print (math.sqrt(y))

	print (u'常用随机数')
	a = [1,2,3,4,5,6,7,8,9,0]

	#从列表a 中随机选择一个：
	print (random.choice(a))

	#从指定的范围(2-100按5递增的数据集)中随机选中一个
	print (random.randrange(2,100,5))

	#从一个随机数，它在(0,1)之间：
	print (random.random())

	#常用的三角函数
	print (u'常用的三角函数')
	x = 100

	#返回x 的反余弦弧度值：
	print (cmath.acos(x))

	#返回x 的正弦函数值：
	print (cmath.sin(x))

	#返回x 的余弦函数值:
	print (cmath.cos(x))

	print (u'数学常量')
	#返回π
	print (cmath.pi)
