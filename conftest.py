import pytest
import requests
import json
from util.httpUtil import HttpUtil
from commom.commomData import CommonData
#session    module   class   function
http = HttpUtil()
@pytest.fixture(scope='session',autouse=True)

def session_fixture1():
    path="/sys/login"
    data={"userName":CommonData.userName,"password":CommonData.password}
    resp_login=http.post1(path,data)
    CommonData.token=resp_login['object']['token']
    # assert resp_login.status_code==200
    print('登录成功')
    # yield
    # path = "/sys/logout"
    # data = None
    # resp_tuichu = http.post1(path, data)
    # # CommonData.token = resp_login['object']['token']
    # assert resp_tuichu['code'] == 200
    # print("退出成功")

    # proxies = {'http': 'http://localhost:8888'}
    # headers = {'Content-Type':'application/json;charset=utf-8'}
    # resp_login = http.post(url="http://192.168.1.203:8083/sys/login/",
    #               proxies=proxies,
    #               data='{"userName":"13233344305","password":"123456"}',
    #               headers=headers)
    # resp_dict = json.loads(resp_login.text)  # json转python_dict
    # token = resp_dict['object']['token']  # 获取token
    # assert resp_login.status_code==200
    # print("登录成功")
    # yield
    # headers[token]=token
    #
    # resp= http.post(url="http://192.168.1.203:8083/sys/logout/",
    #               proxies=proxies,
    #               data=None,
    #               headers=headers)
    # assert resp.status_code==200
    # print("退出")
