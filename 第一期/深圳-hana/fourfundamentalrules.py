
import re
class Calc():
    # 初始化
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def isnum(self,kk):
        # kk = "603.32"
        reg = "^\-?[0-9]+(.[0-9]+)?$"
        s = re.match(reg, kk)
        # print s,type(s)
        if str(s) == 'None':
            return (1)
        else:
            return (2)
    # 加法
    def add(self):
        if (self.isnum(self.before)==2 and self.isnum(self.after)==2):
            return (float(self.before) + float(self.after))
        else:
            return ("please make sure your input is number")
    # 减法
    def sub(self):
        if (self.isnum(self.before) == 2 and self.isnum(self.after) == 2):
            return ((float(self.before))-(float(self.after)))
        else:
            return ("please make sure your input is number")

    # 乘法
    def mul(self):
        if (self.isnum(self.before) == 2 and self.isnum(self.after) == 2):
            return (float(self.before) * float(self.after))
        else:
            return ("please make sure your input is number")

    # 除法
    def div(self):
        if (self.isnum(self.before)==2 and self.isnum(self.after)==2):
            if(float(self.after)==0):
                return "0不能做除数"
            else:
                return (float(self.before) / float(self.after))
        else:
            return ("please make sure your input is number")


if __name__ == '__main__':
    ca = Calc("-96","2.6")
    print(ca.add())
    print(ca.sub())
    print(ca.mul())
    print(ca.div())


