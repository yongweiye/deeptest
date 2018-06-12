#_*_coding:utf-8_*_
if __name__ == "__main__":
    print("元组切片操作实例")
    print("-------------------------------")
    data_demo = (u"北京",u"河北",u"天津",u"山东",u"河南")
    #读取第二个元素河北
    e = data_demo[1]
    print(e)
    #读取倒数第二个元素天津
    e = data_demo[-2]
    print(e)
    #切片，截取第2-4元素
    e = data_demo[1:4]
    print(e)