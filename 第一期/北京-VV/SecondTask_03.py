# -*- coding:utf-8 -*-

__author__ = "VV"

if __name__ == '__main__':
    list_demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    print("demo of internal function for list: ")

    # count number of list
    print(len(list_demo))

    # max of list
    print(max(list_demo))

    # min of list
    print(min(list_demo))

    # turn tuple to list
    tuple_demo = (1, 2, 3, 4, 5, 6)
    list1 = list(tuple_demo)
    print(list1)


if __name__ == '__main__':
    print("demo of list functions:")
    list1 = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6]
    list2 = [7, 8, 9, 0, 10, 11]

    # append one element
    list1.append(100)
    print(list1)

    # count number of 1
    count = list1.count(1)
    print(count)

    # extend list2 ot list1
    list1.extend(list2)
    print(list1)

    # index first 2
    index = list1.index(2)
    print(index)

    # insert 200 to first section
    list1.insert(0, 200)
    print(list1)

    # pop the last element
    list1.pop()
    print(list1)

    # reverse
    list1.reverse()
    print(list1)

    # sort
    list1.sort()
    print(list1)

    # copy list
    list3 = list1.copy()
    print(list1)
    print(list3)

    # clear list
    list1.clear()
    print(list1)
    print(list3)


if __name__ == '__main__':
    print("demo of slice list:")

    data_demo = ["ukulele", "dance", "oilpainting", "hello", "python3"]

    # read the second element
    e = data_demo[1]
    print(e)

    # read the second element from end
    e = data_demo[-2]
    print(e)

    # from second to end
    e = data_demo[1:]
    print(e)

    # from 2-4
    e = data_demo[1:4]
    print(e)


if __name__ == '__main__':
    print("demo of update list")
    data_demo = ["uku", "dance", "oil", "hello", "python3"]
    print(data_demo)

    # update hello to hello world
    data_demo[3] = "hello world"
    print(data_demo)



if __name__ == '__main__':
    # demo of dict
    dict = {"uku": "ukulele", "oil": "oilpainting"}

    # length of dict
    print(len(dict))

    # turn dict to string
    str_d = str(dict)
    print(str_d)
    print(dict)

    # type
    print(type(dict))  # dict type
    print(type(str_d))  # string type



if __name__ == '__main__':
    print("demo of dict functions")

    dict_demo = {"uku": "ukulele", "oil": "oilpainting"}
    tup1 = (1, 2, 3, 4)

    # copy dict
    dict_cp = dict_demo.copy()
    print(dict_demo)
    print(dict_cp)

    # fromkeys create a new dict
    dict_new = dict_demo.fromkeys(tup1, "value")
    print(dict_new)

    # get specific value of key
    value1 = dict_demo.get("uku", "default value")
    value2 = dict_demo.get("oil", "default value")
    print(value1)
    print(value2)

    # in, if key exist
    key = "uku"
    resule1 = key in dict_demo
    result2 = key in dict_new
    print(resule1)
    print(result2)

    # items, return all key and value looks like tuple ???
    items = dict_demo.items()
    print(items)
    # print(type(items))

    # keys, return all key with list type ???
    keys = dict_demo.keys()
    print(keys)

    # setdefault, return value if key exists
    # else insert the key and default value to the dict
    set_result1 = dict_demo.setdefault("uku", "setkey")
    set_result2 = dict_demo.setdefault("I'm a key", "i'm a value")
    print(set_result1)
    print(set_result2)
    print(dict_demo)

    # update dict
    dict_demo.update(dict_new) #??? plus or update?
    print(dict_demo)

    #values, return all values from dict with 'dict_values' in the front of dict
    values = dict_demo.values()
    print(values)


if __name__ == '__main__':
    print("demo of traverse, modify and delete for dict")
    dict_demo = {"uku": "ukulele", "d": "dance"}

    # travers func 1
    for (key, value) in dict_demo.items():
        print(f"{key} : {value}")

    # travers func 2
    for key in dict_demo.keys():
        print(f"{key} : {dict_demo[key]}")

    # modify
    dict_demo["d"] = "draw"
    print(dict_demo)

    # delete specific element
    del dict_demo["d"]
    print(dict_demo)

    # clear dict
    dict_demo.clear()
    print(dict_demo)
