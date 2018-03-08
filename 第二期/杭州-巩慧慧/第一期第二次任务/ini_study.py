#! /usr/bin/env python2
# -*- coding:utf-8 -*-
import configparser

if __name__ == "__main__":
    #
    config = configparser.ConfigParser()

    config.add_section("开源优测")

    config.set("开源优测", "微信", "DeepTest")
    config.set("开源优测", "口号", "自我娱乐")
    config.set("开源优测", "号外", "其实有很多公众号")

    #
    config.add_section("我很好")
    # 写入文件
    with open('iniConfig.ini', 'w') as configfile:
        config.write(configfile)
     #
    config.read("iniConfig.ini")
    #
    sections = config.sections()
    print(sections)

    for sec in sections:
        options = config.options(sec)
        print(options)

    for sec in sections:
        for option in config.options(sec):
            print("[%s] %s = %s" % (sec, option, config.get(sec, option)))