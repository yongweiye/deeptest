#! -*- coding:utf-8 -*-

__author__ = "Mr.汪"

class Calc:
    """
    定义calc类
    """
    def __init__(self, a, b):
        """
        初始化实例的值,方便其他方法调用
        """
        self.a = a
        self.b = b

    def add(self):
        """
        加法
        """
        return self.a + self.b

    def sub(self):
        """
        减法
        """
        return self.a - self.b

    def mul(self):
        """
        乘法
        """
        return self.a * self.b

    def div(self):
        """
        除法，考虑到除数不能为0的情况做判断
        """
        if b != 0:
            """
            使用内置round方法保留两位小数
            """
            return round(self.a / self.b, 2)
        else:
            print("除数不能为0！！！")

def result(calc):
    """
    实现加减乘除，并打印
    """
    sum = calc.add()

    sub = calc.sub()

    mul = calc.mul()

    div = calc.div()

    print(sum, sub, mul, div)



if __name__ == '__main__':
    """
    主函数里调用类方法
    """
    a = int(input("请输入第1个数据："))
    b = int(input("请输入第2个数据："))


    calc = Calc(a, b)
    result(calc)


