# -*- coding: utf-8 -*-
__author__='张晋'

#定义一个基本类
class DemoClass:
     def __init__(self):
         print('初始化')
     def output(self,text):
         #输出text到console
         print(text)
     def output_none(self):
         print('输出不带参数的方法')
class ChildDemoclass(DemoClass):
     def __init__(self):
         print('我是子类')
     def output_none(self):
         print('我是子类不能传参的方法')

if __name__ == "__main__":

     demo_obj = DemoClass()
     demo_obj.output('我叫张晋')
     demo_obj.output_none()
     print('-------------------------------')
     #创建子类的对象
     child_demo_obj=ChildDemoclass()
     child_demo_obj.output('我叫张晋')
     child_demo_obj.output_none()

