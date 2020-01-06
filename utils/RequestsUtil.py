import requests
from common import Base
from  utils.LogUtil import my_log

# 重构
# 1.创建类
class Request:
# 2.定义公共方法
    def __init__(self):
        self.log = my_log("Ruquests")
    # 1）增加方法的参数，根据参数来验证方法get/post, 方法请求
    def requests_api(self,url,method=None, json=None, headers=None,cookies=None):
        if method == "get":
            # 执行get请求
            self.log.debug("发送get请求")
            r = requests.get(url, headers=headers,cookies=cookies)
        elif method =="post":
            # 执行post请求
            self.log.debug("发送post请求")
            r = requests.post(url, json=json, headers=headers,cookies=cookies)
        # else:
        #     raise ("未定义此请求方法")

    # 2）重复的内容，复制进来
            # 3.获取结果相应内容
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        # 4.内容存到字典
        res = dict()
        res["code"] = code
        res["body"] = body
        # 5.字典返回
        return res


# 3.重构get/post方法
    # get
    # 1.定义方法
    def get(self, url, **kwargs):
    # 2.定义参数
        # url,headers,method,json
    # 3.调用公共方法
       return self.requests_api(url, method="get", **kwargs)

    # post
    # 1.定义方法
    def post(self, url, **kwargs):
    # 2.定义参数
        # url,headers,method,json
    # 3.调用公共方法
       return self.requests_api(url, method="post", **kwargs)



if __name__ == '__main__':
    r = Request()
    r.post("http",json=123,headers="aaa")










# # 1.创建封装POST方法
# def requests_post(url, json=None, headers=None):
# # 2.发送requestes POST请求
#     r = requests.post(url, json=json, headers=headers)
# # 3.获取结果相应内容
#     code = r.status_code
#     try:
#         body = r.json()
#     except Exception as e:
#         body = r.text
# # 4.内容存到字典
#     res = dict()
#     res["code"] = code
#     res["body"] = body
# # 5.字典返回
#     return res
#
#
# # 1.创建封装get方法
# def requests_get(url, headers=None):
# # 2.发送requestes get请求
#     r = requests.get(url, headers=headers)
# # 3.获取结果相应内容
#     code = r.status_code
#     try:
#         body = r.json()
#     except Exception as e:
#         body = r.text
# # 4.内容存到字典
#     res = dict()
#     res["code"] = code
#     res["body"] = body
# # 5.字典返回
#     return res