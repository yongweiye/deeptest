# -*- coding:utf-8 -*- 
__author__ = "huohuo"

if __name__ == "__main__":
    print("字典遍历、修改、删除示例")
    dict_demo = {"DeepTest":"开源优测", "ebook":"快学python3"}

    # 遍历 方法1
    for (key, value) in dict_demo.items():
        print("%s : %s" % (key, value))

    # 遍历 方法2
    for key in dict_demo.keys():
        print("%s : %s" % (key, dict_demo[key]))

    # 修改
    dict_demo["ebook"] = "修改后的值"
    print(dict_demo)

    # 删除指定元素
    del dict_demo["ebook"]
    print(dict_demo)

    # 清空字典
    dict_demo.clear()
    print(dict_demo)