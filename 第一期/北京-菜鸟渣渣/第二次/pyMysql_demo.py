# coding=utf-8


from collections import Iterable
from collections import Iterator
from collections import Generator

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

    ge = odd()
    print(isinstance(ge, Iterator))
    print(isinstance(ge, Iterable))
    print(isinstance(ge, Generator))
    print(type(ge))

for i in odd():
    print i