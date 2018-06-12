class Calc(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return  self.a + self.b

    def sub(self):
        return  self.a - self.b

    def mul(self):
        return  self.a * self.b

    def div(self):
        try:
            return  self.a/self.b
        except ZeroDivisionError as reason:
            print(str(reason))

test = Calc(3,4)
print(test.add())
print(test.sub())
print(test.mul())
print(test.div())