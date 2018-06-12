# -*- coding:utf-8 -*-
__author__ = "liqi"

import sys

if __name__ == "__main__":
    seq_tuple = (1, 2, 3, 4, 5)

    # 创建迭代器
    seq_it = iter(seq_tuple)

    # 访问打印第一个元素
    print("第一个元素：%s"%next(seq_it))

    #访问打印第二个元素
    print("第二个元素：%d"%next(seq_it))

    #访问打印第三个元素
    print("第三个元素：%f"%next(seq_it))

    # 使用for循环来遍历迭代器对象
    print("\nfor循环遍历迭代器对象： ")
    for_it = iter(seq_tuple)
    for i in for_it:
        print(i,end = " ")

    # 使用while结合next遍历迭代器对象
    while_it = iter(list(seq_tuple))
    while True:
        try:
            print(next(while_it))
        except StopAsyncIteration:
            # exception StopAsyncIteration
            # Must be raised by __anext__() method of an asynchronous
            # iterator object to stop the iteration.
            sys.exit()
