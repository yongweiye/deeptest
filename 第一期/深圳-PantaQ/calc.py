class Calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        if self.b !=0:
            return self.a/self.b
        else:
            print("the 2th arg can not be 0. ")

if __name__ == "__main__":
    mycalc = Calc(2,4)
    print(mycalc.add())
    print(mycalc.sub())
    print(mycalc.mul())
    print(mycalc.div())