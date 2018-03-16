# ！__author__ =='wuwa'
# ! -*- utf-8 -*-
import json
import re

import pytest
import requests

from libarry.httprequests import requests_interface

respons = requests_interface()


@pytest.fixture(scope='module')
def login():
    '''
    获取参数所需的token/session
    '''
    url = "请求的url"
    data = {"original": "2", "UserId": "xxxx"}
    headers = {'content-type': "application/json"}
    r = requests.post(url, data, headers)
    value = re.findall(r'<Cookie token=(.*?) for', str(r.cookies))[0]
    token = 'token=' + value
    return token


class TestClass:
    def test_get_current_user_info(self, login):
        url = "请求的url"
        querystring = {"platform": "platform"}
        headers = {'Cookie': login}
        result = respons.http_request(interface_url=url, interface_param=querystring, headerdata=headers,
                                 request_type='get')
      #  print(result['data'])
        m = json.loads(result['data'])
      #  print("======================")
      #  print(type(m))
        assert m['status'] ==0


if __name__ == "__main__":
    pytest.main()
