class Clac(object):

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        if type(self.a) != int or  type(self.b) != int:
            return("请务必输入数字")
        else:
            return(self.a + self.b)

    def sub(self):
        if type(self.a) != int or  type(self.b) != int:
            return("请务必输入数字")
        else:
            return(self.a * self.b)

    def mul(self):
        if type(self.a) != int or  type(self.b) != int:
            return("请务必输入数字")
        else:
            return(self.a - self.b)

    def div(self):
        if type(self.a) != int or  type(self.b) != int:
            return("请务必输入数字")
        else:
            return(self.a / self.b)

print(Clac(3,4).add())
print(Clac(3,4).sub())
print(Clac(3,4).mul())
print(Clac(3,4).div())
print(Clac("3",4).div())
