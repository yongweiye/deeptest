# *-*coding:utf-8 *-*

__author__ = "liqi"

class Stack():
    def __init__(self, size = 30):
        #初始化堆栈大小
        self.size = size

        #初始化堆栈列表
        self.stack = []

        #初始化堆栈默认top值
        self.top = -1

    #设置堆栈大小
    def set_size(self, size):
        self.size = size

    # 判断堆栈是否为空
    def is_empty(self):
        res = False
        if self.top == -1:
            res = True

        return res

    # 判断堆栈是否满了
    def is_full(self):
        res = False
        if self.top + 1 == self.size:
            res = True

        return res 
    
    # 打印堆栈里所有内容
    def show(self):
        print(self.stack)

    # 入栈
    def push_obj(self, obj):
        if self.is_full():
            raise Exception ("堆栈满了~")
        else:
            self.stack.append(obj)
            self.top += 1

    #出栈
    def pop_obj(self):
        if self.is_empty():
            raise Exception ("堆栈是空的~")
        else:
            self.top -= 1
            return self.stack.pop()

if __name__ == "__main__":
    print("堆栈实现示例")

    #初始一个长度为5的堆栈示例
    stack = Stack(5)

    # 入栈 整数1-5
    for i in range(1, 7):
        stack.push_obj(i)
        print(stack)

    # 打印下堆栈的内容
    stack.show()

    # 出栈, data的值应该为5
    data = stack.pop_obj()
    print(data)

    # 打印下堆栈的内容，此时应该是[1,2,3,4]
    stack.show()
