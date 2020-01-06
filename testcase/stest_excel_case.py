from config.Conf import ConfigYaml
import os
from common.ExcelData import Data
from utils.LogUtil import my_log
from common import ExcelConfig
from utils.RequestsUtil import Request
import json
from common import Base
from utils.AssertUtil import AssertUtil
import pytest
from config import Conf

# 1.初始化信息
# 初始化测试用例文件
case_file = os.path.join(Conf.get_data_path(), ConfigYaml().get_excel_file())
# 测试用例sheet名称
sheet_name = ConfigYaml().get_excel_sheet()
# 获取运行测试用例列表
run_list = Data(case_file, sheet_name).get_run_data()
print("是否运行为“也”的可执行的测试用例为：%s"%run_list)

#日志
log = my_log()

# 2.测试用例方法，参数化运行
    # 一个用例的执行
class TestExcel:
    # 1.增加pytest
    # 2.修改方法参数
    # 3.重构函数内容

# 1）初始化信息，url，data
    # 1.增加pytest
    def test_run(self):
        data_key = ExcelConfig.DateConfig
        print(data_key)
        # run_list第一个用例，用例key获取values(映射）
        url =ConfigYaml().get_conf_url() + run_list[0][data_key.url]
        # print("url地址为:%s"%url)
        case_id = run_list[0][data_key.case_id]
        case_model = run_list[0][data_key.case_model]
        case_name = run_list[0][data_key.case_name]
        pre_exec = run_list[0][data_key.pre_exec]
        method = run_list[0][data_key.method]
        params_type = run_list[0][data_key.params_type]
        params = run_list[0][data_key.params]
        expect_result = run_list[0][data_key.expect_result]
        headers = run_list[0][data_key.headers]
        cookies = run_list[0][data_key.cookies]
        code = run_list[0][data_key.code]
        db_verify = run_list[0][data_key.db_verify]

# 2) 接口请求
        request = Request()
        #headers 转义json
        # 验证params有没有内容

        if len(str(headers).strip()) != 0:
            # 转换为str类型
            # params = json.dumps(params)
            headers = json.loads(headers)
            body_data = Base.read_body(params)

            app_id = headers["appId"]
            print(app_id)
            total_record = headers["records"]
            print(total_record)
            body_digest = Base.read_digest(params, app_id)
            print(body_digest)

            headers = {'appId': app_id, 'digest': body_digest, 'records': total_record}
            print(headers)

        # method post/get
        if str(method).lower() == "get":
            res = request.get(url, json=body_data, headers=headers)
        elif str(method).lower() == "post":
            res = request.post(url, json=body_data, headers=headers)
        else:
            log.error("错误请求method:%s" %method)
        print("全部测试用例的执行结果是：%s" % res)


        # 结果验证
        assert_util = AssertUtil()
        assert_util.assert_code(int(res["code"]),200)


TestExcel().test_run()