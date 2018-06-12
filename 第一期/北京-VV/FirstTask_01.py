class operation(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 加法
    def add(self):
        return self.a + self.b

    # 减法
    def sub(self):
        return self.a - self.b

    # 乘法
    def mul(self):
        return self.a * self.b

    # 除法
    def div(self):
        return self.a / self.b

if __name__ == '__main__':
    # 验证
    x = int(input("a = "))
    y = int(input("b = "))
    c = operation(x, y)
    print("a + b =", c.add())
    print("a - b =", c.sub())
    print("a * b =", c.mul())
    print("a / b =", c.div())
