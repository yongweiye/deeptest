#-*- coding:utf-8 -*-
import random

class Sort():
    def __init__(self,start,end,count):
        self.start = start
        self.end = end
        self.count = count

    def sorted(self):
        a = []
        for i in range(self.count):
            num = random.randint(self.start, self.end)
            a.append(num)
        print a
        list_count = len(a)
        for x in range(0,list_count):
            for y in range(x+1,list_count):
                if a[x] > a[y]:
                    a[x],a[y] = a[y],a[x]
        print a

if __name__ == "__main__":
    sort1 = Sort(1,10,5)
    sort1.sorted()