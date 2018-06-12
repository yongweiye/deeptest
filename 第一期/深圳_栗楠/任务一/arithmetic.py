#定义函数
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

#输入
print("请选择运算：")
print("A.加")
print("B.减")
print("C.乘")
print("D.除")

choice = input("请选择(A/B/C/D):")

letter1 = int(input("请输入第一个选项："))
letter2 = int(input("请输入第二个选项："))

if choice == 'A':
    print(letter1, "+", letter2,"=", add(letter1,letter2))
    
elif choice == 'B':
    print(letter1, "-", letter2,"=",subtract(letter1,letter2))

elif choice == 'C':
    print(letter1, "*", letter2,"=",multiply(letter1,letter2))

elif choice == 'D':
    print(letter1, "/",letter2,"=",divide(letter1,letter2))

else:
    print("没有此选项")
