#!/usr/bin/env python
# encoding: utf-8
__author__='上海-辰雨'
import random

#第一题：加减乘除四则运算：
class Calc(object):
	'''Calc类进行四则运算'''
	def __init__(self,a,b):
		'''
		初始化传入a,b 两个参数
		:param a:
		:param b:
		'''
		self.a = a
		self.b = b

	def add(self):
		'''加法运算'''
		return self.a + self.b

	def sub(self):
		'''减法运算'''
		return self.a - self.b

	def mul(self):
		'''乘法运算'''
		return self.a * self.b

	def div(self):
		'''除法运算'''
		try:
			return self.a/self.b
		except ZeroDivisionError:
			print '除数不能为零,'


#第二题：随机生成100个10至1000之间的数，对生成的100个数进行排序，禁止使用Python自带的排序函数，要自己实现排序函数
class MySort(object):
	def __init__(self, start, end, count):
		'''
		:param start: 随机数字生成的上限
		:param end: 随机数据生成的下限
		:param count: 产生随机数字的个数
		'''
		self.start = start
		self.end = end
		self.count = count
		self.L = []
		for i in range(self.count):
			number = random.randint(self.start,self.end)
			self.L.append(number)

	def mysort(self):
		'''对列表进行排序'''
		N = []
		for i in range(len(self.L)):
			#将self.L 列表中的最小的数据插入 新的列表中
			N.append(min(self.L))
			#在self.L 列表中移除最小的数据
			self.L.remove(min(self.L))
		return N


# 主程序运行
if __name__ == "__main__":
    sorted_data = MySort(10,1000,100)
    # 打印排序后的结果
    print sorted_data.mysort()

