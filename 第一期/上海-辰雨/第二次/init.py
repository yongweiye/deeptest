#!/usr/bin/env python
# encoding: utf-8
__author__='上海-辰雨'
a = 10
b = 20
if a - b > 0:
	print ('a 大于 b')
elif a == b:
	print ('a 等于 b')
else:
	print ('a 小于 b')


def sum():
	sum = 0
	for i in range(1,100):
		sum = sum + i
	return sum

class Sum(object):
	'''sum 求和 '''
	def __init__(self):
		self.a = int(input('please input a value:'))
		self.b = int(input('please input b value:'))
		self.s = 0

	def sum(self):
		for i in range(self.a,self.b):
			self.s = self.s + i
		return self.s


if __name__ == "__main__":
	print sum()
	sum_obj = Sum()
	print sum_obj.sum()

	#input_data_split()
	#从键盘上接收空格输入：
	data = raw_input('请输入一串字符串:')
	#以空格切割输入的字符串：
	list_data = data.split(' ')
	print list_data


