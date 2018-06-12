#_*_coding：utf-8_*_
if __name__ == "__main__":
    source_str = u"this is my favourite book play  boy ,please show it ,hei hei hei,ye ye ye  "
   #从左往右查找hei
    print(u"从左往右查找 hei")
    print(source_str.find("hei"))
    print(source_str.index("hei"))
    #从右往左查找ye
    print(u"从右往左查找 ye ")
    print(source_str.rfind("ye"))
    print(source_str.rindex("ye"))
    #替换所有的hei
    des_str = source_str.replace("hei","la")
    print(des_str)
    #替换两次hei
    des_str = source_str.replace("hei","la",2)                                                                                                                                                             
    print(des_str)
    