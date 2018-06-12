#!/usr/bin/env python
# encoding: utf-8
'''List(列表)是python最常用的数据类型，它使用方括号[]来标识'''
'''
len: 用于计算列表元素的个数；
max：返回列表中元素的最大值；
min: 返回列表中元素的最小值
list:将元祖转换成列表
'''
list_demo = [1,2,3,4,5,6,7,8,9,0]
#计算list_demo中元素个数：
print (len(list_demo))

#返回list_demo列表中最大值：
print (max(list_demo))

#返回list_demo列表中最小值：
print (min(list_demo))

#将list转换为元祖：
list_demo = (1,2,3,4,5,6)
list1 = list(list_demo)
print list1



'''
list 常用方法：
append(obj):在列表的末尾添加新的元素；
count(obj): 统计列表中元素出现的次数
extent(seq):在列表的末尾追加另一个序列【即列表的扩展】
index(obj):返回列表中第一个匹配到的元素的索引
insert(index,obj):将在列表指定位置插入一个对象；
pop(obj=list[-1]):移除列表中的最后一个元素，并返回该元素
remove(obj):删除列表中第一个匹配到的元素；
reverse():将列表中的元素反向；
sort([func]):对列表中的元素进行排序；
clear():清空列表中的元素；[python2.7 中list没有clear()这个方法]
copy():复制列表[python2.7 中list没有copy()这个方法]
'''
print (u'list方法代码实例:')
list1 = [1,1,2,2,2,3,3,4,5,6]
list2 = [7,8,9,0,10,11]

#append 追加一个元素100
list1.append(100)
print list1

#count 统计1 出现的次数：
count = list1.count(1)
print count

#extend，将list2 追加到list1中
list1.extend(list2)
print (list1)

#index,返回第一个2的索引：
index = list1.index(2)
print index

#insert，在列表的第一个位置插入200
list1.insert(0,200)
print list1

#pop,删除最后一个元素：
list1.pop()
print list1

#reverse,把列表反向一下：
list1.reverse()
print list1

#sort，对列表进行排序：
list1.sort()
print list1

'''列表是一个序列，使用python 的切片机制来访问元祖中指定位置的元素，可以截取其中的一段元素'''
print (u'列表切片操作示例')
data_demo = [u"DeepTest", u"appium", u"testingunion.com", u"hello", u"python3"]

#读取第二个元素appium,索引下标是从0 开始的；
e = data_demo[1]
print e

#读取倒数第二个 hello
e = data_demo[-2]
print e

#切片，截图从第2个元素开始后的所有元素：
e = data_demo[1:]
print e

#切片，截取从第2个元素开始后的所有元素：
e = data_demo[1:4]
print e

'''
更新
列表不同于元祖，列表中的元素是可以进行修改或更新的，除了之前提到的append,insert 新增方法外，
还可以对列表中原有的数据进行修改：
'''
print (u'列表的更新操作示例：')
data_demo = [u"DeepTest", u"appium", u"testingunion.com", u"hello", u"python3"]
print data_demo

#把hello 改为hello world [列表中的元素修改时通过索引进行修改的]
data_demo[3] = u'hello world'
print data_demo