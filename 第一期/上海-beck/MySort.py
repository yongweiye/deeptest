import random

class MySort():
    def __init__(self,start,end,count):
        self.start = start
        self.end = end
        self.count = count
        self.numberlist = []

    def mysort(self):
        self.numberlist = [random.randint(self.start, self.end) for _ in range(self.count)]
        # print("+++++++++++++++++++++++++++++++++++++++++++")
        # print(self.numberlist)
        # print("+++++++++++++++++++++++++++++++++++++++++++")
        n =len(self.numberlist)
        for i in range(0,n-1):
            current_stats = False #添加标志位，一趟比较若没有办法则数组已经有序
            for j in range(0,n-i-1):
                if self.numberlist[j] >= self.numberlist[j+1]:
                    self.numberlist[j],self.numberlist[j+1] = self.numberlist[j+1],self.numberlist[j]
                    current_stats = True
                #print(self.numberlist)
            if not current_stats :
                    break
        return self.numberlist

# 使用示例
if __name__ == "__main__":
     sorted_data = MySort(10,1000, 100)
     newlist = sorted_data.mysort()
# 打印排序后的结果
     print(newlist)

