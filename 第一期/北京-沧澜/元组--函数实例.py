#_*_coding:utf-8_*_
_author_ = "张晋"
if __name__ == "__main__":
    tuple_demo = (1,2,3,4,5,6,7,8,9)
#返回元组的元素个数
print(len(tuple_demo))
#返回元组中元素最大值
print(max(tuple_demo))
#返回元组中最小值
print(min(tuple_demo))
#将list转换为元组
list_demo = [1,2,3,4]
tuple1 = tuple(list_demo)
#打印转换后的元组
print(tuple1)