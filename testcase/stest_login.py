from config import Conf
import os
from utils.YamlUtil import YamlReader
import pytest
from config.Conf import ConfigYaml
from utils.RequestsUtil import Request
from common import Base
from utils.AssertUtil import AssertUtil

# 获取测试用例类容list
# 获取testlogin.yml文件路径
test_file =os.path.join(Conf.get_data_path(),"testlogin.yml")
# print(test_file)

# 使用工具类来读取多个文档内容
data_list = YamlReader(test_file).data_all()
print(data_list)

# 参数化执行测试用例
@pytest.mark.parametrize("login", data_list)
def test_yaml(login):
    # 初始化url，data
    # print("login结果值%s:"%login)
    url =ConfigYaml().get_conf_url()+login["url"]
    data = str(login["data"])
    print("参数类型为：%s" % data)
    app_id = login["app_id"]
    total_record = login["total_record"]
    result = login["result"]
    # print("期望结果是：%s"%result["except1"])

    # print(url)
    # print(data)
    # post请求
    request = Request()
    body_data = Base.read_body(data)
    # 请求头信息
    body_digest = Base.read_digest(data, app_id)

    headers = {'appId': app_id, 'digest': body_digest, 'records': total_record}
    print("请求头部信息为：%s" %headers)
    res = request.post(url, json=body_data, headers=headers)
    # 打印结果
    # print(res)

    # 结果验证
    code = res["code"]
    body = res["body"]


    body_l = AssertUtil().assert_body_header(body)

    AssertUtil().assert_code(code, result["except"])
    AssertUtil().assert_body(body["resultCode"], result["except1"])
    AssertUtil().assert_body(body["resultDesc"], result["except2"])
    # # AssertUtil().assert_body(body["failureList"], [])
    AssertUtil().assert_body(body_l[0], result["except3"])




if __name__ == '__main__':
    pytest.main(["-s","test_login.py"])