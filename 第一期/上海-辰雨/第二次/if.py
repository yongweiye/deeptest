#!/usr/bin/env python
# encoding: utf-8

var1 = int(input('请输入一个整数：'))
if var1 > 0 and var1 < 10:
	print (u'你输入一个大于0小于10的整数')
elif var1 >= 10:
	print (u'你输入一个大于等于10的整数')
else:
	print (u'你输入一个负数')

number = 28
n = 0
while n < 5:
	num = int(input('请输入一个整数：'))
	if num == number:
		print '恭喜你猜中了'
		break
	elif num > number:
		print ('你输入的数字偏大，请重新输入：')
	else:
		print ('你输入的数字偏小，请重新输入：')
	n = n + 1
else:
	print ('你输入的次数超过5次，无法输入。。。。')




