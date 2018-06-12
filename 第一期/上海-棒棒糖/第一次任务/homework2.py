# 随机生成100个10至1000之间的数，对生成的100个数进行排序，禁止使用Python自带的排序函数，要自己实现排序函数
import random
class MySort:
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # count为生成的随机数个数
    def __init__(self, start, end, count):
        list = []
        i = 0
        for i in range(count):
            nub = random.randint(start, end)
            list.append(nub)
            i += 1
            self.count = count
            self.list = list


    # 冒泡实现排序
    def __mysort__(self):
        for i in range(0, self.count):
            for j in range(i + 1, self.count):
                if self.list[i] > self.list[j]:
                    self.list[i], self.list[j] = self.list[j], self.list[i]
        return (self.list)

# 使用示例
# if __name__ == "__main__":
sorted_data = MySort(10, 1000, 100)
sorted_data=sorted_data.__mysort__()
### 打印排序后的结果
print('排序后的结果是:%s'%sorted_data)
