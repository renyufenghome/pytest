# import  pytest
# @pytest.fixture()
# def my_fixture():
#     print("有钱吗。。。")
#     yield
#     print("滚下去。。。")
# class Test_case():
#     @pytest.mark.debug
#     def test_first(this):
#         print("第一个人：我有钱")
#         # assert  1==2
#
#     @pytest.mark.debug
#     @pytest.mark.usefixtures("my_fixture")
#     def test_second(this):
#         print("第二个人：我没钱")
#         # assert 2==2
#     @pytest.mark.usefixtures("my_fixture")
#     def test_three(this):
#         print("第三个人：我没钱")
#         # assert 'a' in 'ab'
#
#     def test_four(this):
#         print("第四个人")