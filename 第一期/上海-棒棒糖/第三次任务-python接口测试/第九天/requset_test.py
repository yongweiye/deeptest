import urllib.request
print("读取www.python.org首页的html源码")
response = urllib.request.urlopen("http://www.python.org")
print("打印下结果")
print(response.read())


