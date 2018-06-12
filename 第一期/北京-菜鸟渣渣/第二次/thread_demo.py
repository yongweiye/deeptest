# coding=utf-8


import time
import threading

'''
1.Python通过两个标准库thread和threading提供对线程的支持。thread提供了低级别的、原始的线程以及一个简单的锁.Threading模块封装了一些常用的方法，初学者直接学这个模块就行了。

2.Python中使用线程有两种方式：函数或者用类来包装线程对象

3.threading.Thread里面几个参数介绍：

class Thread(_Verbose)

    __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None)

    *group *：group参数必须为空，参数group是预留的，用于将来扩展；
    　
    　　参数args和kwargs分别表示调用target时的参数列表和关键字参数。

    *target *: 参数target是一个可调用对象（也称为活动[activity]），在线程启动后执行

    *name *: 参数name是线程的名字。默认值为“Thread - N“，N是一个数字。

    *args *：传递给线程函数target的参数, 他必须是个tuple类型.

    *kwargs *：kwargs表示关键字参数。字典类型
    {}.

'''


# 函数方式
def chi(threadName, name):
    print("%s 吃着%s开始：" % (time.ctime(), threadName))
    print("%s 吃着火锅：涮羊肉" % time.ctime())
    time.sleep(1)
    time.sleep(1)
    print("%s 吃着火锅：涮牛肉" % time.ctime())
    time.sleep(1)
    print("%s 吃着火锅：贡丸" % time.ctime())
    time.sleep(1)
    print("%s 吃着%s结束--" % (time.ctime(), threadName))
    print("%s 运行结束！" % name)


def ting(threadName):
    print("%s 哼着%s1！" % (time.ctime(),threadName))
    time.sleep(2)
    print("%s 哼着小曲2！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲3！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲4！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲5！" % time.ctime())
    time.sleep(2)


threads = []
'''

t1 = threading.Thread(target=chi, name=None,
                      args=("火锅1", "火锅2"), kwargs=None)
'''

t1 = threading.Thread(target=chi, kwargs={"threadName": "火锅", "name": "吃火锅"})
threads.append(t1)
t2 = threading.Thread(target=ting, args=("小猫",))

threads.append(t2)
for i in threads:
    i.start()
