
import random

#x = random.randint(10,1000)
#print(x)

a=[]
for i in range(0,100):
   a.append(random.randint(10,1000))
#print(a)

#将随机生成的100个整数升序排列
def sort():
    for i in range(0,100):
        for j in range(0,99):
            if a[j]>a[j+1]:
                b=a[j]
                a[j]=a[j+1]
                a[j+1]=b
                
if __name__ == '__main__':
	sort()
	print (a)
