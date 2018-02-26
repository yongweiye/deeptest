# -* coding:utf-8 *-
__author__ = 'nancy'

import urllib.request

if __name__ == "__main__":
    url = "http://www.baidu.com"
    resp = urllib.request.urlopen(url)

    print(resp.status)
    print(resp.reason)
    print(resp.headers)
  #  print(resp.read().decode("utf-8"))