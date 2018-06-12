# -*- coding:utf-8 -*-
# __author__ = u'linan'

#字符串的连接和切割
if __name__ == "__main__":
    t = ('1','2','3','4','5','a','b','efg')
    
    #用 - 将t中的元素合并成一个新的字符串
    str_demo = '-'.join(t)
    print(str_demo)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

    #将str_demo以-进行切割
    str_set = str_demo.split('-')
    print(str_set)

    #将t中的元素合并成一个新的字符串
    str_demo = ''.join(t)
    print(str_demo)

#字符串的查找和替换
if __name__ == "__main__":
    source_str = u"it's my book, please show it, wa ka ka, yo yo yo!"

    #从左往右找yo
    print(u"从左往右寻找yo")
    print(source_str.find("yo"))
    print(source_str.index("yo"))

    #从右往左寻找yo
    print(u"从右往左寻找yo")
    print(source_str.rfind("yo"))
    print(source_str.rindex("yo"))

    #替换所有的yo
    des_str = source_str.replace("yo","ha")
    print(des_str)

    #替换两次yo
    des_str = source_str.replace("yo","ha",1)
    print(des_str)


#去字符串的前后空格

if __name__ == "__main__":
    demo_str = "  我的  前后 中 间都有 空格 "
    print(demo_str)

    #去掉前面的空格
    lstr = demo_str.lstrip()
    print(lstr)

    #去掉后面的空格
    rstr = demo_str.rstrip()
    print(rstr)

    #去掉前后的空格
    str = demo_str.strip()
    print(str)

# 判断字符串类型
if __name__ == "__mian__":
    str_1 = "1234567890"
    str_2 = "dfsdfdSDASSD"
    str_3 = "1234565sdfsfWSS"
    str_4 = "abcdef"
    str_5 = "SBCDEF"
    str_6 = "   "
    str_7 = " sfasdf "

    #isalnum 判断字符串是否由字母或数字组成
    print(str_3.isalnum())

    #isalpha 判断字符串是否都是字母
    print(str_2.isalpha())
    print(str_3.isalpha())

    #isdigit 判断字符串是否都是数字
    #isnumeric 判断字符串是否都是数字
    print(str_1.isdigit())
    print(str_1.isnumeric())

    #islower 判断字符串是否都是小写
    print(str_4.islower())
    print(str_4.islower())

    #isspqce 判断字符串是否都是空格
    print(str_6.isspace())
    print(str_7.isspace())

    #isupper 判断字符串是否都是大写
    print(str_5.isupper())