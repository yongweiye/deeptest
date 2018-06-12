# -*- coding:utf-8 -*-

import random

#比较a和b
def compare(a,b):
    if a < b:
        return True
    else:
        return False

#交换列表sourcelist[a]和sourcelist[a+1]项位置
def swap(sourcelist,a):
    if a<len(sourcelist):
        sourcelist[a],sourcelist[a+1]=sourcelist[a+1],sourcelist[a]
        return sourcelist
    else:
        print("over list edge")

#排序函数
def paiXuIncrease(sourcelist):
    for k in range(len(sourcelist)):
        for i in range(len(sourcelist)-1):
            j = i+1
            if not compare(sourcelist[i], sourcelist[j]):
                swap(sourcelist,i)
            else:
                continue
    return sourcelist


#生成low到hight的num个数元素的随机数列
def random_list(low,hight,num):
    ralist = []
    for i in range(num):
        j = 0
        while j == 0:
            a = random.randint(low, hight)
            if a not in ralist:
                ralist.append(a)
                j = 1

    return ralist

if __name__ == "__main__":
    list1 = random_list(10,1000,100)
    # list1=[2,144,9,17,3,56,7,34,66,33]
    list2 = paiXuIncrease(list1)
    print(list2)
    print(len(list2))






