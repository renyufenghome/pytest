from commom.commomData import CommonData
from conftest import http
class Test_Login():
    def test_login_success(self):
        data={
            'userName':CommonData.userName,
            'password':CommonData.password
        }
        resp = http.post1('/sys/login',data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'

        # assert resp['object']['userId']== 121

    def test_login_fail(self):
        data={
            'userName':'13233344306',
            'password':CommonData.password
        }
        resp=http.post1('/sys/login',data)
        assert resp['code'] == 301
        assert resp['msg'] == '用户不存在'

    def test_login_fail1(self):
        data={
            'userName':' ',
            'password':CommonData.password
        }
        resp = http.post1('/sys/login', data)
        assert resp['code'] == 3010
        assert resp['msg'] == '此账户禁止登录'


    def test_login_fail2(self):
        data={
            'userName':CommonData.userName ,
            'password': '12345'
        }
        resp = http.post1('/sys/login', data)
        assert resp['code'] == 410
        assert resp['msg'] == '用户名或密码错误'


    def test_login_fail3(self):
        data={
            'userName': ' ',
            'password': ' '
        }
        resp = http.post1('/sys/login', data)
        assert resp['code'] == 3010
        assert resp['msg'] == '此账户禁止登录'
