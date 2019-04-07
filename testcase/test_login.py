# import  pytest
# @pytest.fixture()
# def my_fixture():
#     print("我的初始化操作:")
# def test_first():
#     print("我的第一个pytest测试用例")
#     # assert  1==2
# @pytest.mark.usefixtures("my_fixture")
# def test_second():
#     print("我的第二个测试用例")
#     # assert 2==2
# @pytest.mark.usefixtures("my_fixture")
# def test_three():
#     print("我的第3个测试用例")
#     # assert 'a' in 'ab'
import pytest
import  requests
from commom.commomData import CommonData
from conftest import http
# class Test_Login():
# def test_login():
#     # path='/sys/getUserInfo'
#     # data={'token':CommonData.token}
#     # resp=http.post(path,data)
#     print("                ")

#     # b=[1,2,3]
#     # assert  3 in b
#
