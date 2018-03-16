#! __author__ == 'wuwa'
# ! -*- coding:utf-8 -*-
import pymysql

from common.writeLog import mylogger

"""
创建数据库连接
"""


class pymysqlopreations:
    def __init__(self, host, port, user, password, db, charset='utf8', link_type=0):
        """
        link_type = 0 时，数据库返回结果为元组模式
        当link_type !=0时，数据库返回结果为字典模式
        :param host:
        :param port:
        :param user:
        :param password:
        :param db:
        :param charset:
        :param link_type:
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset

        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                        db=self.db, charset=self.charset)
            if link_type == 1:
                self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
            else:
                self.cur = self.conn.cursor()

        except Exception:
            mylogger.info(u'Mysql数据库连接失败！')

    def select_one(self, params):
        """
        查询一条数据
        :param params:
        :return:
        """
        try:
            self.cur.execute(params)
            result = self.cur.fetchone()
            result = {'code': '0000', 'message': u'执行单条查询操作成功', 'data': result}
        except:
            result = {'code': '9999', 'message': u'执行单条查询异常', 'data': []}
            mylogger.info(u'Mysql查询失败！')
        finally:
            return result
    def select_all(self):
        pass
    def opt(self):
        pass
    def close_con(self):
        pass


if __name__ == "__main__":
    conn = pymysqlopreations(host='127.0.0.1', port=3306, user='root', password='root', db='irootdb',
                             link_type=1)
    sql = " SELECT * FROM `interface_detail`"
    resutl = conn.select_one(sql)
    print(resutl)
