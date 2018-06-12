# -*- coding:utf-8 -*-
__author__ = "huohuo"

if __name__ == "__main__":
    str_1 = "1234567890"
    str_2 = "abcdefABCDEF"
    str_3 = "12345abcddeABCDE"
    str_4 = "abcdef"
    str_5 = "ABCDEF"
    str_6 = "     "
    str_7 = "  sfsdf  "

    # isalnum是否都是字母或数字
    print(str_3.isalnum())

    # isalpha是否都是字母
    print(str_2.isalpha())

    # isdigit是否都是数字
    print(str_1.isdigit())

    # islower是否都是小写
    print(str_4.islower())
    print(str_2.islower())

    # isupper是否都大写
    print(str_4.isupper())
    print(str_2.isupper())

    # isspace是否有空格
    print(str_6.isspace())
    print(str_7.isspace())