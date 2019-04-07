from commom.commomData import CommonData
from conftest import http
import pytest
import random
import allure
@allure.feature('列表相关信息')
class Test_zhuce():
    def test_zhuce_success(self):
        nickname=str(random.randint(10000000,100000000))
        mobile='135'+nickname
        data={
            "nickName": "ffffffffff",
            "userName": mobile,
            "telNo": "",
            "email": "",
            "address": "",
            "roleIds": "",
            "regionId": 1,
            "regionLevel": 1
}
        resp = http.post1('/user/saveOrUpdateUser', data)
        # assert resp['code']==401

        print(mobile)

        id = self.login(mobile)
        i = self.huoqu()

        assert id == i[1]
        assert i[0] == mobile


        # assert resp['msg']=="操作成功"


    def login(self,user):
        login_data={
            'userName':user,
            'password':CommonData.password
        }
        login_resp = http.post1('/sys/login',login_data)
        assert login_resp['code']==200
        assert login_resp['msg']=='操作成功'
        return login_resp['object']['userId']
    def huoqu(self):
        data ={
                "pageCurrent": 1,
                "pageSize": 10,
                "nickName": "",
                "userName": "",
                "regionId": 1
                }
        huoqu = http.post1('/user/loadUserList',data)
        name = huoqu['object']['list'][0]['userName']
        id = huoqu['object']['list'][0]['id']
        return name,id