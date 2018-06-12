# coding =ut-8


import  os

# print os.getcwd()

# os.mkdir("test_mk1")
# os.rename("test_mk1","deptest_mk1")

print os.curdir
walk_result=os.walk(os.curdir)

for root,dirs,files in walk_result:
    print root

    for name in dirs:
        print "1111",name

    print "-----------"
    for name in files:
        print "2222",name
