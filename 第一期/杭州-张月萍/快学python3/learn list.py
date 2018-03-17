# -*- coding: utf-8 -*-
# __author__ = 'Carina'


if __name__ == "__main__":

    print("1、列表的切片")

    list1 = [1, 2, 3, "appium", "selenium"]
    print(list1[2])
    print(list1[2:3])
    print(list1[:2])
    print(list1[-2])
    print(list1[-3:-1])   #不含右侧值
    print(list1[-2:])

    print("*" * 50, "\n")

    # 内置函数
    print("2、内置函数演示")

    list_demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print("list_demo的元素为：", list_demo)
    print("list_demo的元素个数为:", len(list_demo))     # 计算元素个数
    print("list_demo的元素中最大值为：", max(list_demo))    # 计算元素最大值
    print("list_demo的元素中最小值为：", min(list_demo))    # 计算元素最小值
    tuple_demo = (1, 2, 3, 4, 5)
    list_demo1 = list(tuple_demo)
    print("list_demo1的元素为{}，转换列表为{}".format(tuple_demo, list_demo1))   # tuple转换为list
    print("*" * 50, "\n")

    # 方法
    print("3、列表方法演示")
    list31 = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
    list32 = [7, 8, 9, 0, 10, 11]
    print("list31的原始元素为：", list31)
    print("list32的原始元素为：", list32, "\n")
    # 追加一个元素
    list31.append(100)
    print("list31追加一个元素：", list31)
    # 统计某个字符出现的次数
    count = list31.count(2)
    print("list31中2出现的次数为：", count)
    # list32追加到list31中
    list31.extend(list32)
    print("list32追加到list31中：", list31)
    # 返回第一个3的索引
    index = list31.index(3)
    print("list31中第一个3的位置", index)
    # 在指定位置插入
    list31.insert(3, 200)
    print("在list31中的第四个位置插入200：", list31)
    # 删除具体值
    list31.remove(5)
    print("删除list31中的元素5：", list31)
    # 删除最后一个元素
    list31.pop()
    print("删除list31的最后一个元素：", list31)
    # reverse，列表反向
    list31.reverse()
    print("list31反向后为：", list31)
    # 列表排序
    list31.sort()
    print("list31排序后：", list31)    # 列表中有string类型时不能进行排序
    # 列表拷贝
    list33 = list31.copy()
    print("list31拷贝后：", list33)
    # 清空列表
    list34 = list31.clear()
    print("list31清空后：", list34)

    print("*" * 50, "\n")

    # 更新
    print("4、列表更新演示")
    data_demo = ["Chrome", "FireFox", "360", "Safari"]
    print("data_demo为：", data_demo)
    # 360更新为360浏览器
    data_demo[2] = "360浏览器"
    print("更新后的data_demo：", data_demo)