class Calc:
     def __init__(self,a,b):
         self.a=a
         self.b=b
     def __add__(self):
         return self.a+self.b
     def __sub__(self):
         return self.a-self.b
     def __mul__(self):
         return self.a*self.b
     def __divmod__(self):
         return self.a/self.b

c1 = Calc(2,2)

print(c1.__add__())
print(c1.__sub__())
print(c1.__mul__())
print(c1.__divmod__())

class MySort:
    
