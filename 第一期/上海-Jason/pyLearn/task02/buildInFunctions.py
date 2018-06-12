# -*- coding: UTF-8 -*-
# @author   :   Jason
# @date     :   20180111 23:43
class buildInFunctions:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    print(abs(-5))#返回5
'''
python内建函数：
python3.6.4版共有68个内建函数：
abs(x)
    Return the absolute value of a number. The argument may be an integer or a floating point number.
    If the argument is a complex number, its magnitude is returned.
    返回一个数值的绝对值。参数可以是一个数字或者一个浮点数。
    如果参数是一个复数，则返回其大小。
all(iterable)
    Return True if any element of the iterable is true.
    If the iterable is empty, return False.
    Equivalent to:
    如果参数（迭代器）的所有元素都为True，或者参数为空时，则返回True。
    等价于：
    def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
any(iterable)
    Return True if any element of the iterable is true.
    If the iterable is empty, return False.
    Equivalent to:
    如果参数（迭代器）的所有元素都为True，则返回True。
    如果参数为空，则返回False。
    等价于：
    def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
ascii(object)
    As repr(), return a string containing a printable representation of an object,
    but escape the non-ASCII characters in the string returned by repr() using \x, \u or \U escapes.
    This generates a string similar to that returned by repr() in Python 2.
    同repr()，返回包含参数对象的一个可输出代表的字符串。
    当遇到非ASCII码时，就会输出\x，\u或\U等字符来表示。
    与Python 2版本里的repr()是等效的函数。
bin()
bool()
bytearray()
bytes()
callable()
chr()
classmethod()
compile()
complex()
delattr()
dict()
dir()
divmod()
enumerate()
eval()
exec()
filter()
float()
format()
frozenset()
getattr()
globals()
hasattr()
hash()
help()
hex()
id()
id()
input()
int()
isinstance()
issubclass()
iter()
len()
list()
locals()
map()
max()
memoryview()
min()
next()
object()
oct()
open()
ord()
pow()
print()
property()
range()
repr()
reversed()
round()
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()
tuple()
type()
vars()
zip()
__import__()
'''
