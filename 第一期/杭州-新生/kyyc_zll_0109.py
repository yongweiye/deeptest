# -*- coding: utf-8 -*-

__author__ = "zhonglinglong"

import sys
import math
import cmath
import random

if __name__ == "__main__":
    data = input("请输入一串字符串")
    print("您输入了: %s" % data)
    list_data = data.split(" ")
    print("空格分割后的数：%s" % list_data)

    print("命令行参数个数： %d" % len(sys.argv))
    print("命令行参数列表： %s" % str(sys.argv))

    #打印数据类型
    x = 1.68
    y = 10
    print(int(x))
    print(float(y))
    print(complex(x))
    print(complex(x, y))

    x = -100
    y = 1.9

    print(u"常用数学函数")
    # 返回x的绝对值
    print(abs(x))

    # 反回最大值
    print(max(x, y))

    # 返回最小值
    print(min(x, y))

    # 计算y^2
    print(pow(y, 2))

    # 返回平方根
    print(math.sqrt(y))

    print(u"常用随机函数")
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    # 从列表a中随机选中一个
    print(random.choice(a))

    # 从指定的范围(2-100按5递增的数据集)中随机选中一个
    print(random.randrange(2, 100, 5))

    # 生成一个随机数，它在(0,1)之间
    print(random.random())

    print(u"常用三角函数")
    x = 100

    # 返回x的反余弦弧度值
    print(cmath.acos(x))

    # 返回x的正弦弧度值
    print(cmath.sin(x))

    # 返回x的余弦弧度值
    print(cmath.cos(x))

    print(u"数学常量")
    print(cmath.pi)

    t = ('1', '2', '3', '4', '5', 'a', 'b', "efg")

    # 用 - 将t中元素合并成一个新的字符串
    str_demo = '-'.join(t)
    print(str_demo)

    # 将str_demo以-进行切割
    str_set = str_demo.split('-')
    print(str_set)

    # 将t中元素合并成一个新的字符串
    str_demo = ''.join(t)
    print(str_demo)

    source_str = u"it's my book, please show it, wa ka ka, yo yo yo!"

    # 从左往右查找yo
    print(u"从左往右查找 yo")
    print(source_str.find("yo"))
    print(source_str.index("yo"))

    # 从右往左查找yo
    print(u"从右往左查找 yo")
    print(source_str.find("yo"))
    print(source_str.rindex("yo"))

    # 替换所有的 yo
    des_str = source_str.replace("yo", "ha")
    print(des_str)

    # 替换两次 yo
    des_str = source_str.replace("yo", "ha", 2)
    print(des_str)

    # 去字符串空格示例
    demo_str = "  我的前  后 和 中 间  都有空格  "
    print(demo_str)

    # 去除前面的空格
    lstr = demo_str.lstrip()
    print(lstr)

    # 去除后面的空格
    rstr = demo_str.rstrip()
    print(rstr)

    # 去除前后的空格
    str = demo_str.strip()
    print(str)

    str_1 = "1234567890"
    str_2 = "abcdefABCDEF"
    str_3 = "12345abcdeABCDE"
    str_4 = "abcdef"
    str_5 = "ABCDEF"
    str_6 = "    "
    str_7 = " sfsdf "

    # isalnum
    print(str_3.isalnum())

    # isalpha
    print(str_2.isalpha())

    # isdigit
    print(str_1.isdigit())

    # islower
    print(str_4.islower())
    print(str_2.islower())

    # isupper
    print(str_4.isupper())
    print(str_2.isupper())

    # isspace
    print(str_6.isspace())
    print(str_7.isspace())

    tuple_demo = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

    # 计算tuple_demo中元素个数
    print(len(tuple_demo))

    # 返回tuple_demo中最大值的元素
    print(max(tuple_demo))

    # 返回tuple_demo中最小值的元素
    print(min(tuple_demo))

    # 将list转换成元组
    list_demo = [1, 2, 3, 4, 5, 6]
    tuple1 = tuple(list_demo)

    # 打印转换后的元组
    print(tuple1)

    print(u"元组切片操作示例!")

    data_demo = (u"DeepTest", u"appium", u"testingunion.com", u"hello", u"python3")

    # 读取第二个元素appium, 注意索引下标从0开始
    e = data_demo[1]
    print(e)

    # 读取倒数第二个hello
    e = data_demo[-2]
    print(e)

    # 切片，截取从第2个元素开始后的所有元素
    e = data_demo[1:]
    print(e)

    # 切片，截取第2-4个元素
    e = data_demo[1:4]
    print(e)

    print(u"元组合并或连接操作示例!")
    tup1 = (u"DeepTest", u"appium")
    tup2 = (u"testingunion.com", u"hello", u"python3")

    # 合并成新的元组
    tup3 = tup1 + tup2

    # 打印看看效果
    print(tup1)
    print(tup2)
    print(tup3)

    print(u"元组合并或连接操作示例!")
    tup1 = (u"DeepTest", u"appium")
    print(tup1)

    # 删除元组
    del tup1
    #print(tup1)

    print(u"元组运算示例")
    tup1 = (u"DeepTest", u"开源优测")
    tup2 = (1, 2, 3, 4)

    # 计算元组长度
    print(len(tup1))

    #  元组连接
    tup3 = tup1 + tup2
    print(tup3)

    # 元组复制
    tup4 = tup1 * 2
    print(tup4)

    # 判断元素是否在元组中, 是则返回True, 否则返回
    result = 5 in tup2
    print(result)

    # 遍历元组
    for t in tup2:
        print(t)

    # 将list转换成元组
    list_demo = [1, 2, 3, 4, 5, 6]
    tuple1 = tuple(list_demo)

    # 打印转换后的元组
    print(tuple1)