import requests
print("开源优测 - requests基本示例")

# 发送HTTP GET请求，获取github API列表
r = requests.get("https://api.github.com")

# 请求返回码
status_code = r.status_code

# 完整的返回头
headers = r.headers

# 请求返回头 content-type的值
content_type = r.headers["content-type"]

# 返回内容编码类型
code = r.encoding

# 返回内容文本
text = r.text

# 若返回结果为json格式，我们可以获取其json格式内容
json_data = r.json()

# 打印上述所有获取到的值
print("状态码： ", status_code)
print("返回头： ", headers)
print("content-type： ", content_type)
print("编码：", code)
print("文本内容： ", text)
print("json串内容: ", json_data)


# 导入模块
import requests
print("开源优测 - requests自定义请求头基本示例")
url = "http://www.baidu.com"
# 定义自定义请求头数据
headers = { "user-agent": "www.testingunion.com","custom-head": "DeepTest"}    # 发送带自定义头的请求
r = requests.get(url, headers=headers)

import requests
print("requests post示例")
# 目标url
url = "http://httpbin.org/post"
# 请求头headers
headers = {"custom-header": "mypost"}
# 要post的数据
data = {"data_1": "deeptest", "data_2": "testingunion.com"}
# 发送post请求
r = requests.post(url, data=data, headers=headers)
# 输出结果
print(r.text)

import requests
print("requests post json数据示例")
# 目标服务url
url = "http://jsonplaceholder.typicode.com/posts"
# 自定义头
headers = {
    "custom-post": "my-post",
    "custom-header": "my-json-header"}
# 要post的数据
json_data = {
    "title": "deeptest",
    "body": "开源优测",
    "userId": "1"}
# post json格式的数据
r = requests.post(url, json=json_data, headers=headers)
# 打印下返回结果
print(r.text)


