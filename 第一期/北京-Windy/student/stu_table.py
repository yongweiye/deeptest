#-*- coding:utf-8 -*-

import sqlite3
# 打开本地数据库用于存储用户数据
cx = sqlite3.connect('student.db')

# 在该数据库中创建学生信息表
# cx.execute('''CREATE TABLE StudentTable(ID INTEGER PRIMARY KEY AUTOINCREMENT,StuId INTEGER NOT NULL,
# NAME TEXT NOT NULL,
# CLASS INT NOT NULL)''')

print('Table created successfully')

# 在该数据库下创建课程信息表

# cx.execute('''CREATE TABLE CourseTable(ID INTEGER PRIMARY KEY AUTOINCREMENT,
#  CourseId INT NOT NULL ,
#  Name TEXT NOT NULL,
#  Teacher TEXT NOT NULL ,
#  Classroom TEXT NOT NULL ,
#  StartTime CHAR(11) NOT NULL ,
#  EndTime CHAR(11) NOT NULL )''')

print('Table created successfully')

# 在该数据库中创建学生选课情况表

# cx.execute('''CREATE TABLE ChoseTable(
# ID INTEGER PRIMARY KEY AUTOINCREMENT,
#  CourseId INT NOT NULL ,
#  StuId INT NOT NULL )''')

print('Table created successfully')


def insert_stu():
    cu = cx.cursor()
    stu_id = input('输入学生学号：')
    cu.execute("SELECT StuId FROM StudentTable WHERE StuId = '%s':" % stu_id)
    row = cu.execute()
    if row:
        print('该学号已经存在，请重新输入')
    else:
        stu_name = input('请输入学生姓名：')
        stu_class = input('请输入学生班级：')