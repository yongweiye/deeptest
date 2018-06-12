#coding=utf-8

'''
#python子类调用父类初始化函数有两种方式，以下代码在python2和python3都能运行：
class A(object):
    def __init__(self, x):
        self.x = x

# 方法一
class B(A):
    def __init__(self, x, y):
        A.__init__(self, x)
        self.y = y

# 方法二
class C(A):
    def __init__(self, x, y):
        super(C, self).__init__(x)
        self.y = y

b = B('foo', 'bar')
c = C('foo', 'bar')
print(b.x, b.y)
print(c.x, c.y)
'''

'''
# python2：

# 第二方法，在python2中父类A要继承objectt类，否则会出错：

class A(object):
    def __init__(self, x):
        self.x = x

# 方法一
class B(A):
    def __init__(self, x, y):
        A.__init__(self,x)
        self.y = y

# 方法二
class C(A):
    def __init__(self, x, y):
        super(C, self).__init__(x)
        self.y = y

b = B('foo', 'bar')
c = C('foo', 'bar')
print(b.x, b.y)
print(c.x, c.y)
'''


class DemoClass(object):
    def __init__(self):
        print("初始化")

    def output(self, text):
        # 输出text到console
        print(text)

    def output_none(self):
        # 不带参数的方法
        print("我不能传入参数")


# 继承DemoClass
class ChildDemoClass(DemoClass):
    def __init__(self):
        super(ChildDemoClass, self).__init__()
        print("我是子类")

        # 重写output_none

    def output_none(self):
        print("我是子类不能传参的方法")


if __name__ == "__main__":
    '''
    # 创建一个类对象
    demo_obj = DemoClass()

    # 调用output
    demo_obj.output("我是参数")

    # 调用output_none
    demo_obj.output_none()
'''
    print("-----------------------------------")
    # 创建子类的对象
    child_demo_obj = ChildDemoClass()

    # 调用output, 调用的是父类的方法
    child_demo_obj.output("我是参数")

    # 调用output_none, 调用的是自己的方法，即重写后的方法
    child_demo_obj.output_none()

'''
Python3对Unicode字符的原生支持

Python2中使用 ASCII 码作为默认编码方式导致string有两种类型str和unicode，Python3只支持unicode的string。python2和python3字节和字符对应关系为：

Python3采用的是绝对路径的方式进行import。


Python2中存在老式类和新式类的区别，Python3统一采用新式类。新式类声明要求继承object，必须用新式类应用多重继承。

Python3使用更加严格的缩进。Python2的缩进机制中，1个tab和8个space是等价的，所以在缩进中可以同时允许tab和space在代码中共存。这种等价机制会导致部分IDE使用存在问题。Python3中1个tab只能找另外一个tab替代，因此tab和space共存会导致报错：TabError: inconsistent use of tabs and spaces in indentation.

'''