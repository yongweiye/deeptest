# -*-coding:utf-8 -*-
__author__ = "huohuo"

if __name__ == "__main__":
    list_demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    print("内置函数处理list示例：")

    # 计算list_demo中元素个数
    print(len(list_demo))

    # 返回list_demo中最大值的元素
    print(max(list_demo))

    # 返回list_demo中最小值的元素
    print(min(list_demo))

    # 将元组转换成list
    tuple_demo = (1, 2, 3, 4, 5, 6)
    list1 = list(tuple_demo)

    # 打印转换后的列表
    print(list1)
