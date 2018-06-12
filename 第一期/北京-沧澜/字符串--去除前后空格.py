#_*_coding:utf-8_*_
_author_ ="u,张晋"

if __name__ == "__main__":
    demo_str = "       我的前后都哦有空格       "
    print(demo_str)
    #去除前面的空格
    lstr = demo_str.lstrip()
    print(lstr)
    #去除右边的空格
    rstr = demo_str.rstrip()
    print(rstr)
    #去除两边的空格
    strip = demo_str.strip()
    print(strip)


