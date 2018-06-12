# -*- coding:utf-8 -*-
__author__ = "阿_gu"

print("您好，这是我的第一个python程序")

a = 10
b = 20

if a - b > 0:
    print("a大于b")

elif a - b == 0:
    print("a等于b")

else:
    print("a大于b")

if __name__ == "__main__":
    sum = 0
    for index in range(1, 100):
        sum = sum + index
    print("1-99的和为： %d" % sum )


if __name__ == "__main__":

    data = input("请输入任意字符：")  # 读取键盘的输入
    print("你输入了：%s" % data ) #打印输入的字符




