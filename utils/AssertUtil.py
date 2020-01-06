from utils.LogUtil import my_log
import json

# 1.定义封装类
class AssertUtil:
# 2.初始化数据，日志
    def __init__(self):
        self.log = my_log("AssertUtil")

    def assert_body_header(self, body):
        """获取需断言信息"""
        self.list = []
        for i in range(0, len(body['failureList'])):
            self.list.append(body['failureList'][i]['returnDesc'])
            return self.list


        # 3.code相等
    def assert_code(self, code, expected_code):
        try:
            assert int(code) == int(expected_code)
            return True
        except:
            self.log.error("code error,code is %s,expected_code is %s"%(code, expected_code))
            raise

# body相等
    def assert_body(self, body, expected_body):
        try:
            assert body == expected_body
            return True
        except:
            self.log.error("body errror,body is %s,expected_body is %s"%(body, expected_body))
            raise

# 5.body包含
    def assert_in_body(self, body, expected_body):
        """
        验证返回结果是否包含期望的结果
        :param body:
        :param expected_body:
        :return:
        """
        try:
            # body = json.dumps(body)
            assert expected_body in body
            return True
        except:
            self.log.error("不包含或者body是错误的,body is %s,expected_body is %s" % (body, expected_body))
            raise

