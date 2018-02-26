# -* coding:utf-8 *-
__author__ = 'nancy'

import urllib.request

# http请求类
class http():
    def __init__(self,url):
        self.url = url

    # get
    def get(self):
         try:
            response = urllib.request.urlopen(self.url)
            response = response.read()
            return response
         except Exception as e:
            print(e)

    # post
    def post(self, data=''):
        try:
            response = urllib.request.urlopen(self.url, data)
            response = response.read()
            return response
        except Exception as e:
            print(e)