#!/usr/bin/env python
# encoding: utf-8
__author__ = '上海-辰雨'
#字符串的连接和切割：
'''
join:以指定的字符串将元组、列表中的所有的元素合并为一个新的字符串；
split:以指定的分隔符来截取字符串，返回一个list 对象
'''
t = ('m','1','9','u','8','w','8','d','2','a')

#用 - 将t 中的元素合并成一个新的字符串：
str_demo = '-'.join(t)
print str_demo

#用 - 对str_demo 字符串进行切换：
str_set = str_demo.split('-')
print str_set

#将t 中的元素合并成一个新的字符串：
str_demo = ''.join(str_set)
print str_demo

'''
字符串查找和替换：
find:find(str,beg=0,end=len(string)),查找str 是否包含在字符串中，若指定了beg和end,则在beg和end 范围中查找，若找到则返回开始的索引值，否则返回-1
index:通find 方法，不同的是，index若未查找到，抛出一个异常的信息，而不是返回-1；
rfing:通find 方法，不过rfind是从右边往左边查找。；
rindex:通index 方法，不过rindex 是从右边往左边查找的；
replace:将字符串中指定的子串替换成目标字符串，如果指定了替换的次数，则替换不超过指定的次数：
'''
source_str = u"it's my book,please show it,wa ka ka,yo yo yo !"
#从左往右查找：
print (u'从左往右查找 yo')
print (source_str.find('yo'))
print (source_str.index('yo'))

#从右往左查：
print (u'从右往左查 yo')
print (source_str.rfind('yo'))
print (source_str.rindex('yo'))

print (u'替换所有的yo')
des_str = source_str.replace('yo','ha')
print des_str

print (u'替换两次yo')
des_str = source_str.replace('yo','ha',2)
print (des_str)

'''
取出字符串前后空格：
lstrip:取出字符串左边的空格；
rstrip:去除字符串右边的空格
strip:去除字符串左右两边的空格，即把lstrip和rstrip都执行一遍
'''
#去字符串空格示例：
demo_str = '  我的前  后和 中 间  都有空格  '
print (demo_str)

#取出前面的空格：
lstr = demo_str.lstrip()
print (lstr)

#去除后面的空格：
rstr = demo_str.rstrip()
print (rstr)

#去除前后的空格：
str = demo_str.strip()
print (str)

'''
判断字符串的类型：
isalnum: 判断字符串是否由字母或数字组成，是则返回true,否则返回false
isalpha: 判断字符串是否都是字母，是则返回true,否则返回false
isditgit: 判断字符串是否都是数字，是则返回true,否则返回false
islower: 判断字符串是否都是小写，是则返回true,否则返回false
isnumeric: 判断字符串是否都是数字，是则返回true，否则返回false
isspace: 判断字符串是否都是空格，是则返回true，否则返回false
isupper: 判断字符串是否都是大写，是则返回true，否则返回false
'''
str_1 = "1234567890"
str_2 = "abcdefABCDEF"
str_3 = "12345abcdeABCDE"
str_4 = "abcdef"
str_5 = "ABCDEF"
str_6 = "    "
str_7 = " sfsdf "

#isalnum
print str_3.isalnum()

#isalpha
print str_2.isalpha()

#isditgit
print str_1.isdigit()

#islower
print str_4.islower()
print str_2.islower()

#isupper
print str_5.isupper()
print str_4.isupper()

#isspace
print str_6.isspace()
print str_7.isspace()
