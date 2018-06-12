# -*-coding:utf-8 -*-
__author__ = "huohuo"

if __name__ == "__main__":
    print("字典方法应用示例")

    dict_demo = {"DeepTest":"开源优测", "ebook":"快学python3"}
    tup1 = [1, 2, 3, 4]

    # copy 复制字典
    dict_cp = dict_demo.copy()
    print(dict_demo)
    print(dict_cp)
    print("复制结束")

    # fromkeys创建字典
    dict_new = dict.fromkeys(tup1, "value")
    print(dict_new)
    print("创建字典结束")

    # get 获取指定key的value
    value1 = dict_demo.get("DeepTest", "我是默认值")
    value2 = dict_demo.get("Python3", "我是默认值")
    print(value1)
    print(value2)
    print("获取指定key的value")

    # in,判断key是否存在
    key = "DeepTest"
    result1 = key in dict_demo
    result2 = key in dict_new
    print(result1)
    print(result2)

    # items, 以元组形式返回字典所有的（key, value）
    items = dict_demo.items()
    print(items)

    # keys以列表形式返回字典所有的key
    keys = dict_demo.keys()
    print(keys)

    # setdefault, 如果key存在，则返回其对应的value,否则将key和默认值插入字典,并返回默认值
    set_result1 = dict_demo.setdefault("DeepTest", "设置值")
    set_result2 = dict_demo.setdefault("我是key", "我是value")
    print(set_result1)
    print(set_result2)
    print(dict_demo)

    # updata,更新字典
    dict_demo.update(dict_new)
    print(dict_demo)
    print("更新字典结束")

    # values,返回字典中所有的value
    values = dict_demo.values()
    print(values)