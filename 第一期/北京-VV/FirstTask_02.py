from random import randint
from sys import exit

a = [randint(10, 1000) for i in range(100)]

# 打印
def print_():
    cnt = 0
    for j in a:
        cnt += 1
        print(cnt, j)
    return 0

# 排序
def order(a):
    for k in range(len(a)):
        for l in range(len(a)):
            if a[k] > a[l]:
                a[k], a[l] = a[l], a[k]
    return a

# 测试
print("100个随机数字:")
print_()
order(a)
print("\n排序后：")
print_()
