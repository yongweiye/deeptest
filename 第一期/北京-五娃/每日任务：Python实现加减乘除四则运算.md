## 包含内容

* 代码内容
* 知识点

### 代码内容
题目：实现一个四则运算的类，要求实现任意两个数的加减乘除运算

```
# __author__ ='wuwa'
# -*- coding: utf-8 -*-

class Calc:
    # 初始化
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 加法
    def __add__(self):
        '''
        :return:self.a + self.b
        '''
        return self.a + self.b

    # 减法
    def __sub__(self):

        return self.a - self.b

    # 乘法
    def mul(self):
        return self.a * self.b

    # 除法
    def div(self):
        # print(type(self.a))
        # print(type(self.b))
        # print(type(self.a / self.b))
        #return self.a / self.b 2和3版本的除法有稍许变化
        if self.b !=0:
            return self.a // self.b
        else:
            return ('除数为0，无法计算！')


    # 加法
    def adds(self):
        return self.__add__()

    def subs(self, ):
        return self.__sub__()


if __name__ == "__main__":
    eg = Calc(2, 0)
    print(eg.adds())
    print(eg.subs())
    print(eg.mul())
    print(eg.div())

```
### 知识点

* 类的创建

  通过class关键字创建Python类，
  
```
class Calc:
    # 初始化
    def __init__(self, a, b):
        self.a = a
        self.b = b
```
如果需要指明继承的父类，则在类名后加上（继承的类名）默认为object。


* 私有方法

```
def __sub__(self):

        return self.a - self.b

def subs(self, ):
        return self.__sub__()
```
单下划线开头、双下划线开头、上下划线开头＋双下划线结尾代表的意义不同，自行Google。

__sub__ 是一个专有方法，不能从的类外面被调用（严格讲在在类外部也可以访问，略过），通过self.__sub__()访问。

* if /else语句
 
```
if self.b !=0:
    return self.a // self.b
else:
    return ('除数为0，无法计算！')
```
如上所示 if与else成对出现，当然有时候也可以只写if。

```
if self.b !=0:
    return self.a // self.b
if self.b = 0
    return ('除数为0，无法计算！')
```
又或者有多个if/else 可以通过elif实现。

```
if self.b !=0:
   return self.a // self.b
elif self.a !=0:
    return ('没哟这个条件')
else:
    return ('除数为0，无法计算！')
```
只有当if的条件不满足时，会执行下面的elif语句，如果elif语句的条件也不满足时，会执行else语句，可以有多个else语句。

if语句嵌套，当满足第一个if语句后才会执行第二个if语句（其实第二个if语句是第一个if语句的代码块，第一个if语句的条件满足了，代码块自然及执行了，反之亦然）。

```
if self.b !=0:
    if self.a!=0：
        return self.a // self.b
```

* python2与python3的语法不同点

  1. print函数，在python3中需要加（），如print（'hello'）
  2. 在进行整数相除时，得到的了float类型,
     因为，在X/Y类型，在Python2.6或者之前，这个操作对于整数运算会省去小数部分，而对于浮点数运算会保持小数部分；在Python3.0中变成真除法（无论任何类型都会保持小数部分，即使整除也会表示为浮点数形式）。