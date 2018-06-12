# -*- coding:utf-8 -*-

__author__ = '罗权'

if __name__ == "__main__":
    #这是一种注释
    sum = 0
    #range左闭右开
    for i in range(1,100):
        sum = sum + i

    print('1-99的和为 %d ' %sum)

#读取键盘输入
'''
if __name__ == "__main__":

    content = input('请输入任意字符：')

    print('你输入了: %s ' %content)

    #以空格切割输入的字符串
    list_content = content.split(' ')
    print(list_content)
'''
#命令行参数
#python3 -h:查看python各参数帮助信息

import sys

if __name__ == '__main__':
    print('命令行参数个数: %d' %len(sys.argv))

    print('命令行参数列表: %s' %str(sys.argv))