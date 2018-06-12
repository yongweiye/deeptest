# -*- coding:utf-8 -*-
__author__ = "huohuo"

if __name__ == "__main__":
   print("元组切片操作示例！")

   data_demo = ("Deeptest", "appium", "testingunion.com", "hello", "pyrhon3")

   # 读取第二个元素appium,索引下标从0开始
   e = data_demo[1]
   print(e)

   # 读取倒数第二个hello
   e = data_demo[-2]
   print(e)

   # 切片，截取从第2个元素开始的所有元素
   e = data_demo[1:]
   print(e)

   # 切片，截取2-4个元素
   e = data_demo[1:4]
   print(e)