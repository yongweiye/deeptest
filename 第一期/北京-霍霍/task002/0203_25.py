# -*- coding:utf-8 -*-
__author__ = "huohuo"

if __name__ == "__main__":
   source_str = "it's my book, please show it, wa ka ka, yo yo yo!"

   #从左往右查yo
   print("从左往右查 yo")
   print(source_str.find("yo"))
   print(source_str.index("yo"))

   #从右往左查yo
   print("从右往左查 yo")
   print(source_str.rfind("yo"))
   print(source_str.rindex("yo"))

   #替换所有的 yo
   des_str = source_str.replace("yo", "ha")
   print(des_str)

   #替换两次 yo
   des_str = source_str.replace("yo", "ha", 2)
   print(des_str)