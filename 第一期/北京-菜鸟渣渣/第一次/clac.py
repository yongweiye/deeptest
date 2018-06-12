＃编码= utf-8的

＃编码= utf-8的
class  Calc：
    def  __init__（self，a，b）：
        自我 .a = a
        自我 .b = b
    ＃添加
    def  add（self）：
        返回 自我 .a + self .b
    ＃分
    def  sub（self）：
        返回 自我 .a - 自我 .b
    ＃多少
    def  mul（self）：
        返回 自我 .a * self .b
    ＃ DIV
    def  div（self）：
        如果 b ！= 0：

             自我回报 .a /（self .b）
        提出 “除数未0，非法”
如果 __name__ == “ __main__ ”：
    a = int（input（“请输入第一个数字：”））
    b = int（input（“请输入第二个数字：”））
    calc = Calc（a，b）
    打印 calc.add（），calc.sub（），calc.mul（），calc.div（）