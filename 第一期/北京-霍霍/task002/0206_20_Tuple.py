# -*- coding:utf-8 -*-
__author__ = "huohuo"

if __name__ == "__main__":
    tuple_demo = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

    # tuple_demo中元素个数
    print(len(tuple_demo))

    # tuple_demo中最大值
    print(max(tuple_demo))

    # tuple_demo中最小值
    print(min(tuple_demo))

    # list转换成元组
    list_demo = [1, 2, 3, 4, 5, 6]
    tuple1 = tuple(list_demo)

    # 打印转换后的元组
    print(tuple1)
    