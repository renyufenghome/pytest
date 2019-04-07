from commom.commomData import CommonData
from conftest import http
import pytest
import allure
@allure.feature('用户相关信息')
class Test_changePwd():
    @pytest.mark.debug
    @pytest.mark.usefixtures("recoveryPwd")
    @allure.story("修改密码。。。。。。。。。。。。。")
    def test_changePwd_success(self):
        newPwd='123456'
        data = {'token':CommonData.token,
            'userId': 121,
            'userName': CommonData.userName,
            'oldPwd':CommonData.password,
            'password':newPwd
        }
        resp = http.post1('/sys/changePwd', data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        print("现在的新密码是666666")
@pytest.fixture()
def recoveryPwd():
    newPwd='123456'
    yield
    data={
        'token': CommonData.token,
        'userId': 121,
        'userName': CommonData.userName,
        'oldPwd': '123456',
        'password': CommonData.password

    }
    resp=http.post1('/sys/changePwd',data)

    assert resp['code'] == 200
    assert resp['msg'] == '操作成功'
    print("现在的新密码是123456")





       # assert resp['object'] == 'null'
    # def test_changeppPwd_again(self):
    #     data ={'token':CommonData.token,
    #         'userId': 121,
    #         'userName': CommonData.userName,
    #         'oldPwd':'666666',
    #         'password':'999999'
    #     }
    #     resp = http.post1('/sys/changePwd', data)
    #     assert resp['code'] == 200
    #     assert resp['msg'] == '操作成功'
    #     print("现在的新密码是999999")