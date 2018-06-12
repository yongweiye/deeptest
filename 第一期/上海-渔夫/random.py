import random
class MySort:
    def __init__(self, start, end, count):
        if not(isinstance(start, (int, float))):
            raise TypeError('bad operand type!')
        elif not (isinstance(end, (int, float))):
            raise TypeError('bad operand type!')
        elif not(isinstance(count, (int))):
            raise TypeError('bad operand type!')
        else:
            self.start = start
            self.end = end
            self.count = count
            self.a = []

        if self.count <= 0:
            print('不生成随机数!')
        else:
            for i in range(self.count):
                self.a.append(random.uniform(self.start, self.end))
            print(self.a)

    def __mysort__(self):
        for i in range(len(self.a)):
            for j in range(len(self.a)-i-1):
                if self.a[j] > self.a[j+1]:
                    self.a[j], self.a[j+1] = self.a[j+1], self.a[j]
        return self.a

    if  __name__  =  "__main__":
        print('初始化：')
        mylist = MySort(1, 10, 3)
        print('排序后：\n{0}'.format(mylist.__mysort__()))