# -*- coding:utf-8 -*-
__author__ = "huohuo"

if __name__ == "__main__":
    x = 1.68
    y = 10

    #x转换为整数
    print(int(x))
    #y转换为浮点数
    print(float(y))
    #x转换为复数，实部为x,虚部为0
    print(complex(x))
    #x,y转换为复数，实部为x,虚部为y
    print(complex(x, y))