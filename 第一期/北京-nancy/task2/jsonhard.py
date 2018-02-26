# -*- coding:utf-8 -*-
__author__ = 'nancy'

import json

if __name__ == "__main__":
    json_demo = """
        {
        "one" : [
            {
                "one11" : "one11value",
                "one12" : "one12value",
                "one13" : "one13value"
            },
            {
                "one21" : "one21value",
                "one22" : "one22value",
                "one23" : "one23value"
            }
        ],
        "two" : [
            {
                "two11" : "two11value",
                "two12" : "two12value",
                "two13" : "two13value"
            },
            {
                "two21" : "two21value",
                "two22" : "two22value",
                "two23" : "two23value"
            }
        ]
        }
        """
    print(type(json_demo))
    json_dict = json.loads(json_demo)

    for k, v in json_dict.items():
        print(k, "---", v)
        for date in v:
             for dk, dv  in date.items():
                 print("------", dk, ":", dv)
