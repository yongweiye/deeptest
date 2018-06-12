# -*- coding:utf-8 -*-

__author__ = 'VV'

if __name__ == '__main__':
    x = 1.87
    y = 20

    # 将x转换为整数
    print(int(x))

    # 将y转换为浮点数
    print(float(y))

    # 将x转换为复数，实数部分为x，虚数部分为y
    print(complex(x))

    # 将x，y转换为复数， 实数部分为x， 虚数部分为y
    print(complex(x, y))


import math
import cmath
import random

if __name__ == '__main__':
    x = -90
    y = 1.8

    print("常用数学函数")

    # 返回x的绝对值
    print(abs(x))

    # 返回最大值
    print(max(x, y))

    # 返回最小值
    print(min(x, y))

    # 计算y^2
    print(pow(y, 2))

    # 返回平方根
    print(math.sqrt(y))

    print("常用随机函数")
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    # 从列表a中随机选中一个
    print(random.choice(a))

    # 从指定的范围（2-100按5递增的数据集）中随机选中一个
    print(random.randrange(2, 100, 5))

    # 生成一个随机数，它在（0,1）之间
    print(random.random())

    print("常用三角函数")
    x = 88

    # 返回x的反余弦弧度制
    print(cmath.acos(x))

    # 返回x的正弦弧度制
    print(cmath.sin(x))

    # 返回x的余弦弧度制
    print(cmath.cos(x))

    print("数学常量")
    print(cmath.pi) # 返回π



if __name__ == '__main__':
    t = ('1', '2', '3', '4', '5', 'a', 'b', "efg")

    # 用 - 将t中元素合并成一个新的字符串
    str_demo = '-'.join(t)
    print(str_demo)

    # 将str_demo以-进行分割
    str_set = str_demo.split('-')
    print(str_set)

    # 将t中元素合并成一个新的字符串
    str_demo = ''.join(t)
    print(str_demo)



if __name__ == '__main__':
    source_str = "it's my book, please show it, wa ka ka, yo yo yo!"

    # 从左往右查找yo
    print("从左往右查找yo")
    print(source_str.find("yo"))
    print(source_str.index("yo"))

    # 从右往左查找yo
    print("从右往左查找 yo")
    print(source_str.find("yo"))
    print(source_str.rindex("yo"))

    # 替换所有的 yo
    des_str = source_str.replace("yo", "ha")
    print(des_str)

    # 替换两次 yo
    des_str = source_str.replace("yo", "ha", 2)
    print(des_str)



if __name__ == '__main__':
    # 去字符串空格实例
    demo_str = "  我的前  后  和  中  间  都有空格  "
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


if __name__ == '__main__':
    str_1 = "1234567890"
    str_2 = "abcdefABCDEF"
    str_3 = "12345abcdeABCDE"
    str_4 = "abcdef"
    str_5 = "ABCDEF"
    str_6 = "     "
    str_7 = " sfsdf  "

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



if __name__ == '__main__':
    tuple_demo = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

    # count number of tuple_demo
    print(len(tuple_demo))

    # max of tuple_demo
    print(max(tuple_demo))

    # min of tuple_demo
    print(min(tuple_demo))

    # turn list to tuple
    list_demo = [1, 2, 3, 4, 5, 6]
    tuple1 = tuple(list_demo)
    print(tuple1)


if __name__ == '__main__':
    print("demo of slice tuple")

    data_demo = ("DeepTest", "appium", "testing.com", "hello", "python3")

    # read second element
    e = data_demo[1]
    print(e)

    # read second from end
    e = data_demo[-2]
    print(e)

    # from second to end
    e = data_demo[1:]
    print(e)

    # from second to fourth
    e = data_demo[1:4]
    print(e)



if __name__ == '__main__':
    print("demo of merge tuple")
    tup1 = ("ukulele", "dance")
    tup2 = ("oil paiting", "hello", "python3")

    # merge
    tup3 = tup1 + tup2

    # print to see
    print(tup1)
    print(tup2)
    print(tup3)


if __name__ == '__main__':
    print("demo of delete tuple")
    tup1 = ("dance", "ukulele")
    print(tup1)

    # delete tuple
    del tup1
    # print(tup1)


if __name__ == '__main__':
    print("calc for tuple")
    tup1 = ("ukulele", "dance")
    tup2 = (1, 2, 3, 4)

    # length of tuple
    print(len(tup1))

    # merge tuple
    tup3 = tup1 + tup2
    print(tup3)

    # copy tuple
    tup4 = tup1 * 2
    print(tup4)

    # judge
    result = 5 in tup2
    print(result)

    # traverse tuple
    for t in tup2:
        print(t)


# done for today
