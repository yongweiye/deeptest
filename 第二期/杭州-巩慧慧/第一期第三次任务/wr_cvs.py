#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-23 下午11:35
# @Author  : gonghuihui
# @File    : wr_cvs.py
import csv

if __name__ == "__main__":
    print("Python csv文件亵渎操作示例")
    with open('csv_data.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(['hello', 'Study Python3', 'Auto Testing'])
        csvfile.close()

    print("读取csv_data.csv内容")
    with open('csv_data.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print("row的类型： ", type(row))
            print(row)

            # 遍历每行中每个数据
            for data in row:
                print(data, "  ")

        f.close()
