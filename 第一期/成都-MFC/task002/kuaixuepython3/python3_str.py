# -*- coding:utf-8 -*-

"""
字符串
https://note.youdao.com/web/#/file/WEB98c227493cf921f71d8b69ba93cef80d/note/WEB7f0ac39f04ec94e91ae095d9fadcc620/
在python3中，所有的字符串都是Unicode编码
join and split
"""


if __name__ == '__main__':
    t = ('1', '2', '3', '4', '5', 'a', 'b', "efg")   # tuple

    # 用 - 将t中元素合并成一个新的字符串
    str_demo = '-'.join(t)
    print(str_demo)

    # 将str_demo以-进行切割
    str_set = str_demo.split('-')
    print(str_set)

    # 将t中元素合并成一个新的字符串
    str_demo = ''.join(t)
    print(str_demo)

    source_str = u"it's my book, please show it, wa ka ka, yo yo yo!"

    # Replace
    print("Replace示例：")
    # 从左往右查找yo
    print(u"从左往右查找 yo")
    print(source_str.find("yo"))
    print(source_str.index("yo"))

    # 从右往左查找yo
    print(u"从右往左查找 yo")
    print(source_str.rfind("yo"))
    print(source_str.rindex("yo"))

    # 替换所有的 yo
    des_str = source_str.replace("yo", "ha")
    print(des_str)

    # 替换两次 yo
    des_str = source_str.replace("yo", "ha", 2)
    print(des_str)

    # 去字符串空格示例
    print("去字符串空格示例:")
    demo_str = "  我的前  后 和 中 间  都有空格  "
    print(demo_str)

    # 去除前面的空格
    lstr = demo_str.lstrip()
    print(lstr)

    # 去除后面的空格
    rstr = demo_str.rstrip()
    print(rstr)

    # 去除前后的空格
    str = demo_str.strip()
    print(str)

    # 判断字符串类型is
    str_1 = "1234567890"
    str_2 = "abcdefABCDEF"
    str_3 = "12345abcdeABCDE"
    str_4 = "abcdef"
    str_5 = "ABCDEF"
    str_6 = "    "
    str_7 = " sfsdf "
    str_8 = "四五六"

    # isalnum
    print(str_3.isalnum())

    # isalpha
    print(str_2.isalpha())

    # isdigit
    print(str_1.isdigit())

    # islower
    print(str_4.islower())
    print(str_2.islower())

    # isupper
    print(str_4.isupper())
    print(str_2.isupper())

    # isspace
    print(str_6.isspace())
    print(str_7.isspace())

    # compare isdigit or isnumeric
    print(str_8.isdigit())    # False
    print(str_8.isnumeric())   # True