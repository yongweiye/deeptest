# -*- coding:utf-8 -*-

__author__ = 'VV'

if __name__ == '__main__':
    print("demo of set")

    set_source = set([1, 1, 2, 3, 4, 5, 6, 7])
    set_demo = set([1, 1, 2, 3, 4, 5, 6, 7])

    print("origin data: ", end="")
    print(set_demo)

    # add
    print("after add: ", end="")
    set_demo.add(9)
    set_demo.add(1)

    print(set_demo)

    # remove
    print("after remove: ", end="")
    set_demo.remove(9)

    print(set_demo)

    # update to add more than one element
    list_demo = ["a", "b", "c"]
    set_demo.update(list_demo)

    print("after update: ", end="")
    print(set_demo)


if __name__ == '__main__':

    var1 = int(input("Plean enter a int: "))

    if var1 >= 0 and var1 < 10:

        print("your number is greater than 0 and less than 10")

    elif var1 >= 10:

        print("your number is greater than or equle to 10")

    else:

        print("negative number")



if __name__ == '__main__':
    # traverse tuple by using for
    tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9,0)

    print("traverse and print tuple: ")
    for t in tuple_1:
        print(t)


if __name__ == '__main__':
    # traverse list by using for
    list_1 = ["uku", "dance", "hello"]

    print("traverse and print list: ")
    for text in list_1:
        print(text)


if __name__ == '__main__':
    # traverse dict by for
    dict_1 = {"uku": "ukulele", "d": "draw"}

    print("one way to traverse the dict and print it: ")
    for (key, value) in dict_1.items():
        print(f"{key} : {value}")

    print("\n--------------------------")

    print("the other way to traverse the dict and print it: ")
    for key in dict_1:
        print(f"{key} : {dict_1[key]}")


if __name__ == '__main__':
    print("instance of range for")

    # use the default parameter to create a list and traverse it
    for i in range(5):
        print(i, end=",")

    # enter
    print('')

    # list in a specific range and traverse it
    for i in range(0, 10):
        print(i, end=',')

    # enter
    print('')

    # step way create a list and traverse it
    for i in range(0, 10, 2):
        print(i, end=',')


if __name__ == '__main__':
    print("multiplication table: ")
    for i in range(1, 10):
        for j in range(i, 10):
            print(f"{i} * {j} =", i * j, end="  ")

        print("")


if __name__ == '__main__':
    print("count sum of even numbers in range of 0 to 100")

    n = 100
    index = 0
    sum = 0
    while index <= n:
        sum = sum + index
        index = index + 2

    print(f"sum of even numbers in range of 0 to 100 is {sum}")


if __name__ == '__main__':
    print("multiplication table: ")
    n = 1

    while n <= 9:
        for m in range(n, 10):
            print(f"{n} * {m} = ", n * m, end="  ")

        print("")
        n = n + 1


def sum(a, b):

    c = a + b
    return c

if __name__ == '__main__':
    print("definition of function, count sum")
    # call function
    c = sum(1, 2)

    print(c)


def multi():
    data = []
    for i in range(1, 10):
        line = []
        for j in range(i, 10):
            p = i * j
            line.append(f"{i} * {j} = {p} ")

        data.append(line)

    return data

if __name__ == '__main__':
    print("multiplication table: ")
    data = multi()

    for d in data:
        print(d)


# sum

def sum_tuple(seq):
    sum = 0
    for s in seq:
        sum = sum + s
    return sum

if __name__ == '__main__':
    print("call tuple parameter, instance of sum: ")
    tuple_1 = (1, 9, 10, 2, 2, 39, 0, 11, 20)
    print(tuple_1)

    sum = sum_tuple(tuple_1)
    print(f"sum is {sum}")


def str_join(str1, str2, str3):

    return str1 + str2 + str3

if __name__ == '__main__':
    print("connect trings: ")

    str1 = "hello, "
    str2 = "My name is: "
    str3 = "VV"

    str_j = str_join(str1, str2, str3)
    print(str_j)
