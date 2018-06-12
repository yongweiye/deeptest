# -*- coding:utf-8 -*-
__author__ = "huohuo"

if __name__ == "__main__":
    demo_str = "  我的前 后 和 中 间 都有空格  "
    print(demo_str)

    #去前面的空格
    lstr = demo_str.lstrip()
    print(lstr)

    #去后面的空格
    rstr = demo_str.rstrip()
    print(rstr)

    #去前后的空格
    demo = demo_str.strip()
    print(demo)