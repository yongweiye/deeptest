#! -*- coding:utf-8 -*-

__author__ = "Mr.汪"
#导入生成随机数的库
import random
# #随机生成10-1000之间的数
# # a_list = range(10,10000)
# b_list = random.sample(range(10,10000),100)
# print(b_list)
# b_length = len(b_list)
# #实现排序
# """
#
# """
# for i in range(0,b_length - 1):
#     for j in range(0,b_length - 1 - i):
#         if b_list[j] > b_list[j + 1]:
#             b_list[j],b_list[j + 1] = b_list[j + 1],b_list[j]
#
# print(b_list)


class Sort:
    """
    定义排序sort类
    """
    def __init__(self,start,end,count):
        """
        这里初始化三个参数分别是随机数开始结束的范围，以及随机数的个数
        :param start:
        :param end:
        :param count:
        """
        self.start = start
        self.end = end
        self.count = count

    def sort_data(self):
        """
        实现排序，这里利用冒泡排序，还是现学的
        :return:
        """
        list_random = random.sample(range(self.start,self.end),self.count)
        length_random = len(list_random)
        for i in range(0, length_random - 1):
            for j in range(0, length_random - 1 - i):
                if list_random[j] > list_random[j + 1]:
                    list_random[j], list_random[j + 1] = list_random[j + 1], list_random[j]

        result_random = list_random
        return print(result_random)


if __name__ == '__main__':
    """
    主函数入口,调用排序方法
    """
    # start = int(input("请输入区间开始范围:"))
    # end = int(input("请输入区间结束范围:"))
    # count = int(input("请输入随机个数:"))
    result = Sort(10,100,10)
    result.sort_data()
