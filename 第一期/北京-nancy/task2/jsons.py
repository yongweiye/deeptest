# -*- coding:utf-8 -*-
__author__ = 'nancy'

import json

if __name__ == "__main__":
    # json to dict
    json_str = '{"name": "namev", "pass": "passv"}'
    print("old type is: ", type(json_str))

    json_dict = json.loads(json_str)
    print("json to dict: ", type(json_dict))

    print(json_dict)
    for k, v in json_dict.items():
       print(k,": " ,v)

    # dict to json
    json_dit = {"name": "namev", "pass": "passv"}
    print("old type is: ", type(json_str))

    json_str1 = json.dumps(json_dit)
    print("dict to json: ", type(json_dict))
    print(json_str1)


