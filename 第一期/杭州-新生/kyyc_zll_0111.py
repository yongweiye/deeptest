# -*- coding: utf-8 -*-

__author__ = "zhonglinglong"

if __name__ == "__main__":
    list_demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    print(u"内置函数处理list示例： ")

    # 计算list_demo中元素个数
    print(len(list_demo))

    # 返回list_demo中最大值的元素
    print(max(list_demo))

    # 返回list_demo中最小值的元素
    print(min(list_demo))

    # 将list转换成元组
    list_demo = (1, 2, 3, 4, 5, 6)
    list1 = list(list_demo)

    # 打印转换后的列表
    print(list1)

    print(u"list方法代码示例： ")
    list1 = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6]
    list2 = [7, 8, 9, 0, 10, 11]

    # append，追加一个元素
    list1.append(100)
    print(list1)

    # count, 统计1出现的次数
    count = list1.count(1)
    print(count)

    # extend, 将list2追加到list1中
    list1.extend(list2)
    print(list1)

    # index, 返回第一个2的索引
    index = list1.index(2)
    print(index)

    # insert, 在列表第一个位置插入200
    list1.insert(0, 200)
    print(list1)

    # pop, 删除最后一个元素
    list1.pop()
    print(list1)

    # reverse, 把列表反向一下
    list1.reverse()
    print(list1)

    # sort,对列表进行排序
    list1.sort()
    print(list1)

    # copy，列表拷贝
    list3 = list1.copy()
    print(list1)
    print(list3)

    # clear 清空列表
    list1.clear()
    print(list1)
    print(list3)

    print(u"列表切片操作示例!")

    data_demo = [u"DeepTest", u"appium", u"testingunion.com", u"hello", u"python3"]

    # 读取第二个元素appium, 注意索引下标从0开始
    e = data_demo[1]
    print(e)

    # 读取倒数第二个hello
    e = data_demo[-2]
    print(e)

    # 切片，截取从第2个元素开始后的所有元素
    e = data_demo[1:]
    print(e)

    # 切片，截取第2-4个元素
    e = data_demo[1:4]
    print(e)

    print(u"列表更新操作示例!")
    data_demo = [u"DeepTest", u"appium", u"testingunion.com", u"hello", u"python3"]
    print(data_demo)

    # 把hello改为hello word
    data_demo[3] = u"hello word"
    print(data_demo)

    # 字典基本示例
    dict = {u"DeepTest": u"开源优测", u"book": u"快学Python3"}

    # 计算字典的长度
    print(len(dict))

    # 以字符方式输出字典,即将字典转换成字符串
    str_d = str(dict)
    print(str_d)
    print(dict)

    # 判断类型
    print(type(dict))  # 字典类型
    print(type(str_d))  # 字符串str类型

    print(u"字典方法应用示例")

    dict_demo = {u"DeepTest": u"开源优测", u"ebook": u"快学Python3"}
    tup1 = [1, 2, 3, 4]

    # copy复制字典
    dict_cp = dict_demo.copy()
    print(dict_demo)
    print(dict_cp)

    # fromkeys创建字典
    dict_new = dict.fromkeys(tup1, u"value")
    print(dict_new)

    # get获取指定key的value
    value1 = dict_demo.get(u"DeepTest", u"我是默认值")
    value2 = dict_demo.get(u"Python3", u"我是默认值")
    print(value1)
    print(value2)

    # in, 判断key是否存在
    key = u"DeepTest"
    result1 = key in dict_demo
    result2 = key in dict_new
    print(result1)
    print(result2)

    # items, 以元组形式返回字典所有的(key, value)
    items = dict_demo.items()
    print(items)

    # keys 以列表形式返回字典所有的key
    keys = dict_demo.keys()
    print(keys)

    # setdefault, 如果key存在，则返回其对应的value，
    # 否则将该key和默认值插入到字典中，并返回默认值
    set_result1 = dict_demo.setdefault(u"DeepTest", u"设置值")
    set_result2 = dict_demo.setdefault(u"我是key", u"我是value")
    print(set_result1)
    print(set_result2)
    print(dict_demo)

    # update, 更新字典
    dict_demo.update(dict_new)
    print(dict_demo)

    # values,返回字典中所有的value
    values = dict_demo.values()
    print(values)

    print(u"字典遍历、修改、删除示例")
    dict_demo = {u"DeepTest": u"开源优测", u"ebook": u"快学Python3"}

    # 遍历 方法1
    for (key, value) in dict_demo.items():
        print("%s : %s" % (key, value))

        # 遍历 方法2
    for key in dict_demo.keys():
        print("%s : %s" % (key, dict_demo[key]))

        # 修改
    dict_demo[u"ebook"] = u"修改后的值"
    print(dict_demo)

    # 删除指定元素
    del dict_demo[u"ebook"]
    print(dict_demo)

    # 清空字典
    dict_demo.clear()
    print(dict_demo)