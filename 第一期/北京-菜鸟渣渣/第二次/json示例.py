# coding=utf-8


import json

json_str = '{"name": "Deep", "url": "www.testingunion.com", "id": "DeepTest"}'

json_data=json.loads(json_str)
print type(json.loads(json_str))

for k,v in json_data.items():
    print k,v
print "-------------"
json_date = {"name": "Deep", "url": "www.testingunion.com", "id": "DeepTest"}

print type(json_data)
print  json.dumps(json_data)
print  type(json.dumps(json_data))

print "<><><><><><><><><><><><><><><><><><><"

json_demo = """
    {
        "weixin": [
            {
                "name": "开源优测",
                "uid": "DeepTest",
                "desc": "分享开源测试技术"
            },
            {
                "name": "开源优测_demo",
                "uid": "DeepTest_demo",
                "desc": "分享开源测试技术_demo"
            }
        ],
        "web": [
            {
                "url": "www.testingunion.com",
                "name": "开源优测社区",
                "desc": "分享各类开源测试技巧"
            },
            {
                "url": "www.testingunion.com_demo",
                "name": "开源优测社区_demo",
                "desc": "分享各类开源测试技巧_demo"
            }
        ]
    }
"""

json_dict=json.loads(json_demo)

for (k,v) in json_dict.items():
    print k ,"   " , v

    for data in v:

        for k,v in data.items():
            print k ,"-" ,v