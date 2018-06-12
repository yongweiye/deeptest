# -*- coding:utf-8 -*-

__author__ ='huohuo'

if __name__ == '__main__':
    # 读取键盘任意输入
    data = input("请输入一串任意字符:")
    # 以空格切割输入的字符串
    list_data = data.split('  ')
    # 打印切割后的列表数据
    print(list_data)
