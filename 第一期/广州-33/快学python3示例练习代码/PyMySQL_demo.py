# coding = utf-8
# 使用pymysql库实现增删改查

import pymysql

# import random

if __name__ == "__main__":
    print("PyMySQL基本示例")

    # 创建一个连接实例
    conn = pymysql.connect(
        host="ip",  # mysql服务ip地址，若服务在本机则用localhost
        port=port,  # mysql服务端口
        user="user",  # 访问mysql的用户名
        password="password",  # 访问mysql的密码
        db="db",  # 默认连接到的数据库
        charset="utf8"  # 连接字符集
    )

    try:
        # 创建用于交互的cursor对象
        cursor = conn.cursor()

        '''
        # 先插入10条测试数据
        # 构建插入数据的sql
        sql = "INSERT INTO 'user' ('email', 'password') VALUES (%s, %s)"
        
        # 生产10条测试数据
        sql_data = []
        for index in range(0, 10):
            email = "%.10f@163.com" % random.random()
            password = random.random()
            sql_data.append((email,password))
            
        # 执行sql，进行批量插入数据
        cursor.executemany(sql, sql_data)
        
        # 提交至数据库
        conn.commit()
        '''

        # 查询5条数据
        sql = "SELECT * FROM 'training_building' LIMIT 5"

        # 执行sql
        cursor.execute(sql)

        # 取查询到的所有数据
        all_data = cursor.fetchall()

        # 遍历打印出来
        print("取所有查询到的数据")
        for data in all_data:
            print(
                "building_id: %d building_code: %d building_name: %d province_code: %d province_name: %d city_code: %d city_name: %d county_code: %d county_name: %d address: %d create_code: %d create_name: %d create_time: %d last_update_code: %d last_update_name: %d last_update_time: %d"
                % (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
                   data[11], data[12], data[13], data[14], data[15], data[16]))

        # 取1条数据
        one_data = cursor.fetchone()
        print("\n取1条数据")
        print(
            "building_id: %d building_code: %d building_name: %d province_code: %d province_name: %d city_code: %d city_name: %d county_code: %d county_name: %d address: %d create_code: %d create_name: %d create_time: %d last_update_code: %d last_update_name: %d last_update_time: %d"
            % (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
               data[11],
               data[12], data[13], data[14], data[15], data[16]))

    finally:
        # 最后把数据库连接关闭
        conn.close()