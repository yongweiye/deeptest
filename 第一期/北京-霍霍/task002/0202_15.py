# -*- coding:utf-8 -*-
__author__ = "huohuo"

if __name__ == "__main__":
    t = ('1', '2', '3', '4', '5', 'a', 'b', 'efg')

    # 用 - 将元素合并成一个新的字符串
    str_demo = '-'.join(t)
    print(str_demo)

    #将str_demo以-切割
    str_set = str_demo.split('-')
    print(str_set)

    #将t中元素合并成一个新字符串
    str_demo = ''.join(t)
    print(str_demo)

