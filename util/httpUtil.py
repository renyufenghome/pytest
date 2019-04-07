import requests
import json
from commom.commomData import CommonData
# proxies={'http':'http://localhost:8888'}
# headers={}
# headers['Content-Type']='application/json;charset=utf-8'
# http=requests.session()
# s=http.post(url="http://192.168.1.203:8083/sys/login/",
#                 proxies=proxies,
#                 data='{"userName":"13233344305","password":"123456"}',
#                 headers=headers)
# assert  s.status_code==200
# s_dict=json.loads(s.text)   # json转python_dict
# token=s_dict['object']['token']     #获取token
# headers['token']=token      #将token加到headers_dict中
#
# data={'token':token}     #创建了一个data的dict，添加了token数据
# data_json=json.dumps(data)    #将python转化为json
# s=http.post(url="http://192.168.1.203:8083/sys/getUserInfo",
#                 proxies=proxies,
#                 data=data_json,
#                 headers=headers)
#
# print(s.text)



# s=http.post(url="192.168.1.203:8083/place/denableIllegal",
#             proxies=proxies,
#             data='{"id": 81,"enable": 0}',
#             headers=headers)
# print(s.text)
# print(s.headers)
# print(s.status_code)
# print(s.cookies)
# print(s.content)




class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.headers={'Content-Type':'application/json;charset=utf-8'}

    def post1(self,path,data):

        proxies=CommonData.proxies
        host=CommonData.host
        data_json=json.dumps(data)
        if CommonData.token is not None:
            self.headers['token']=CommonData.token
        resp_login=self.http.post(url=host+ path,
                                  proxies=proxies,
                                  data=data_json,
                                  headers=self.headers
                                  )
        assert resp_login.status_code==200
        resp_json=resp_login.text
        resp_dict=json.loads(resp_json)
        print(resp_dict)
        return resp_dict
