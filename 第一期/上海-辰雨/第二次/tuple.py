#!/usr/bin/env python
# encoding: utf-8
'''元祖，使用小括号（）来标识，其特点是：元祖中的元素不可修改'''
tuple1 = (u'DeepTest',u'开源优测',u'1')
tuple2 = (1,2,3,4,5)
tuple3 = ('a','b','c','d','e')

'''
内置函数：
python中常用的内置函数：
len: 用于计算元祖的个数；
max: 用于返回元祖中元素的最大值
min: 返回元祖中元素的最小值
tuple: 将列表转换成元祖
'''
tuple_demo = ('1','2','3','4','5','6','7','8','9','0')

#计算tuple_demo中元素的个数:
print len(tuple_demo)

#计算tuple_demo中最大值：
print max(tuple_demo)

#计算tuple_demo中的最小值
print min(tuple_demo)

#将列表转换为元祖：
list_demo = [1,2,3,4,5,6]
print tuple(list_demo)


'''
切片：
因为元祖也是一个序列，所有可以使用python的切片机制来访问元祖中的指定位置的元素，也可以截取其中的一段元素
元祖可以通过下标索引的方式来读取元素；
元祖可以通过负数下标索引的方式反向读取元素；
元祖可以通过 起始:终止 方式截取一段元素
'''
data_demo = (u'DeepTest',u'appium',u'testingunion.com',u'hello',u'python3')

#读取第二个元素'appium'，注意索引下标是从0 开始的
e = data_demo[1]
print e

#读取倒数第二个元素 'hello'
e = data_demo[-2]
print e

#切片，截取从第二个元素开始后的所有元素：
e = data_demo[1:]
print e

#切片，截取第2-4个元素：
e = data_demo[1:4]
print e



'''元祖的元素的特性：不可修改。我们可以对元祖进行合并后或是连接成新的元祖'''
print (u'元祖合并或连接操作示例！')
tuple1 = (u'DeepTest',u'appium')
tuple2 = (u'testingunion.com',u'hello',u'python3')

#合并新的元祖：
tuple3 = tuple1 + tuple2

print (tuple1)
print (tuple2)
print (tuple3)


'''元祖的元素特性：不可修改。意味着我们不可以删除单个元素，但是可以把元素删除'''
print (u'元祖的删除！')
tuple4 = (u'DeepTest', u'appium')
print (tuple4)

#删除元祖
del tuple4
# print (tuple4)



'''元祖和字符串一样可以使用 + 或 * 进行运算，经过运算可以生成一个新的元祖'''
print (u'元祖的运算示例')
tuple1 = (u'DeepTest',u'开源优测')
tuple2 = (1,2,3,4)

#计算元祖的长度：
print len(tuple2)

#元祖的连接:
tuple3 = tuple1 + tuple2
print tuple3

#元祖的复制：
tuple4 = tuple1*4
print tuple4

#判断元素是否在元祖中，是则返回True,否则返回False
result = 5 in tuple2
print (result)

#遍历元祖：
for t in tuple2:
	print t


'''列表转元祖，使用内置函数tuple将list转换为元祖'''
list_demo = [1,2,3,4,5,6,7]
tuple1 = tuple(list_demo)
print tuple1
print type(tuple1)