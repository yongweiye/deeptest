# -*- coding:utf-8 -*-
import sys

__author__ = 'beck'

# #多元赋值
# x,y=1,2
# print(x)
# print(y)
# #交换2个变量
# x,y=y,x
# print(x)
# print(y)

#基本语法熟悉
if __name__ == '__main__':
    # sum=0
    # for i in range(101):
    #     sum=sum+i
    # print("1-99的和为%d"%sum+",此时i的值为%d"%i)

    # data=input("请输入你需要输入的内容：")
    # print("你输入的内容为：%s"%data)
    # mylist = []
    # print('请输入需要输入的字符串，以.为结束：')
    # while True:
    #     datalist = input('')
    #     print('\n')
    #     if datalist == '.':
    #      break
    #     else:
    #         mylist.append(datalist)
            #print(mylist)
    # newlist = mylist.split('8')  #split只能对字符串进行分割，且可以按照指定参数进行分割，返回结果为列表
    # print(newlist)

#控制字符串分割
    # datalist = input('请输入需要的字符串：')
    # mylist = datalist.split('.')
    # print(mylist)
    print("命令行参数个数: %d"% len(sys.argv))
    print("命令行参数列表：%s" % str(sys.argv))

