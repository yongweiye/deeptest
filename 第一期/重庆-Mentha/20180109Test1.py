class Test:
    # 初始化参数
    def __init__(self, a, b):
        self.a=a
        self.b=b
    # 加法
    def __add__(self):
        return self.a+self.b
    # 减法
    def __sub__(self):
        return self.a-self.b
    # 乘法
    def mul(self):
        return self.a*self.b
    # 除法
    def div(self):
        return self.a/self.b
    
    def Test1(Test):
        sum=Test.add()
        print (sum)
        sub=Test.sub()
        print (sub)
        mul=Test.mul()
        print (mul)
        div=Test.div()
        print (div)
