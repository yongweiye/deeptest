#-*- coding:utf-8 -*-

class Calc():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return  self.a * self.b

    def div(self):
        try:
            result = self.a / self.b
        except ZeroDivisionError:
            print "You can't divide by zero!"
        else:
            return result

if __name__ == "__main__":
    calc = Calc(2,0)
    result = calc.div()
    print result