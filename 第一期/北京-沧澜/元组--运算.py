# -*- coding:utf-8 -*-

__author__ = u'zhangjin'

if __name__ == "__main__":
    print(u"元组运算示例")
    tup1 = (u"DeepTest", u"开源优测")
    tup2 = (1, 2, 3, 4)

    # 计算元组长度
    print(len(tup1))

    #  元组连接
    tup3 = tup1 + tup2
    print(tup3)

    # 元组复制
    tup4 = tup1 * 2
    print(tup4)

    # 判断元素是否在元组中, 是则返回True, 否则返回
    result = 5 in tup2
    print(result)

    # 遍历元组
    for t in tup2:
        print(t)