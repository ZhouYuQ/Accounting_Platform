from config.Conf import ConfigYaml
import os
from common.ExcelData import Data
from utils.LogUtil import my_log
from common import ExcelConfig
from utils.RequestsUtil import Request
import json
from common import Base
import pytest
from utils.AssertUtil import AssertUtil
from common.Base import init_db
from config import Conf
import allure
from config import Conf

# 1.初始化信息
# 初始化测试用例文件
# case_file = os.path.join("../data", ConfigYaml().get_excel_file())
case_file =Conf.get_data_path()+"\\"+ ConfigYaml().get_excel_file()
print("文件地址是%s"%case_file)
# 测试用例sheet名称
sheet_name = ConfigYaml().get_excel_sheet()
# case
data_init = Data(case_file, sheet_name)
run_list = data_init.get_run_data()
print("是否运行为“也”的可执行的测试用例为：%s"%run_list)
#日志
log = my_log()
# 初始化dataconfig
data_key = ExcelConfig.DateConfig
print("获取到的地址信息：%s"%data_key)
sql = init_db("db_1")
sql.clear(ConfigYaml().get_db_sql())

# 2.测试用例方法，参数化运行
    # 一个用例的执行
class TestExcel:
    # 1.增加pytest
    # 2.修改方法参数
    # 3.重构函数内容
    def run_api(self, url, method, params=None, header=None, cookie=None):
        """发送请求api"""
        # 2) 接口请求
        request = Request()

        # headers 转义json
        # 验证params有没有内容

        if len(str(params).strip()) != 0:
            # 转换为str类型
            # params = json.loads(params)
            # header = json.loads(headers)
            body_data = Base.read_body(params)

            app_id = header["appId"]
            print(app_id)
            total_record = header["records"]
            print(total_record)
            body_digest = Base.read_digest(params, app_id)
            print(body_digest)

            headers = {'appId': app_id, 'digest': body_digest, 'records': total_record}
            print(headers)

        # method post/get
        if str(method).lower() == "get":
            res = request.get(url, json=body_data, headers=headers, cookies=cookie)
        elif str(method).lower() == "post":
            res = request.post(url, json=body_data, headers=headers, cookies=cookie)
        else:
            log.error("错误请求method:%s" % method)
        print("获取到的code：%s" %res["code"])
        return res


    def run_pre(self, pre_case):
       # 初始化数据
       url = ConfigYaml().get_conf_url() + pre_case[data_key.url]
       method = pre_case[data_key.method]
       params = pre_case[data_key.params]
       headers = pre_case[data_key.headers]
       cookies = pre_case[data_key.cookies]

       # 判断json是否存在，json转义
       # if headers:
       #     header = json.loads(headers)
       # else:
       #     header = headers

       header = Base.json_parse(headers)
       cookie = Base.json_parse(cookies)


       res = self.run_api(url, method, params, header, cookie)
       print("前置测试用例的执行结果是：%s"%res)
       return res

       # if cookies:
       #     cookie = json.loads(cookies)
       # else:
       #     cookie = cookies

# 1）初始化信息，url，data
    # 1.增加pytest
    @pytest.mark.parametrize("case", run_list)
    def test_run(self, case):
        # run_list第一个用例，用例key获取values(映射）
        url =ConfigYaml().get_conf_url() + case[data_key.url]
        print("url地址为:%s"%url)
        case_id = case[data_key.case_id]
        case_model = case[data_key.case_model]
        case_name = case[data_key.case_name]
        pre_exec = case[data_key.pre_exec]
        method = case[data_key.method]
        params_type = case[data_key.params_type]
        params = case[data_key.params]
        expect_result = case[data_key.expect_result]
        print("期望结果期望的数据类型是：%s"%type(expect_result))
        headers = case[data_key.headers]
        cookies = case[data_key.cookies]
        code = case[data_key.code]
        print("期望的code是%s" %code)
        db_verify = case[data_key.db_verify]
        # print("期望的sql是%s" %db_verify)


        # 验证前置条件
        if pre_exec:

        # 找到执行的用例
            # 前置测试用例
            pre_case = data_init.get_case_pre(pre_exec)
            print("前置测试用例的条件是：%s"%pre_case)
            pre_res = self.run_pre(pre_case)
            headers, cookies = self.get_correlation(headers, cookies, pre_res)

        header = Base.json_parse(headers)
        cookie = Base.json_parse(cookies)
        res = self.run_api(url, method, params, header, cookie)
        print("全部测试用例的执行结果是：%s" % res)
        print("实际结果数据类型是：%s" % type(str(res["body"])))

        #sheet名称feature一级标签
        allure.dynamic.feature(sheet_name)
        #模块story二级标签
        allure.dynamic.story(case_model)
        #用例id + 接口名称title
        allure.dynamic.title(case_id+case_name)
        #请求url 请求类型 期望结果 实际结果 描述Description
        # desc = "请求URL:{},请求类型：{},期望结果：{},实际结果：{}".format(url, method, expect_result, res)
        desc = "<font color='red'>请求URL:</font>{}<Br/>" \
               "<font color='red'>请求类型：</font>{}<Br/>" \
               "<font color='red'>期望结果：</font>{}<Br/>" \
               "<font color='red'>实际结果：</font>{}".format(url, method, expect_result, res)
        allure.dynamic.description(desc)

        # 结果替换
        # 结果验证
        assert_util = AssertUtil()
        # 状态码
        assert_util.assert_code(int(res["code"]), int(code))
        # 验证返回结果内容
        assert_util.assert_in_body(str(res["body"]), str(expect_result))
        # 数据库结果验证
        # if db_verify:
        #     Base.assert_db("db_1",res["body"],db_verify)


        # 数据库结果验证
         # 1.初始化数据库
        if db_verify:
             # 2.查询sql，excel定义好的
            # sql = init_db("db_1")
            db_res = sql.fetcone(db_verify)
            log.debug("数据库查询结果：{}".format(str(db_res)))
            # 数据库结果与接口返回的结果验证
            # 获取数据库结果的key
            verify_list = list(dict(db_res).keys())
            # 根据key获取数据库结果，接口结果
            for line in verify_list:
                # res_line = res["body"][line]
                res_db_line = dict(db_res)[line]
            #验证
                assert_util.assert_body("0001025", res_db_line)


    # # 判断json是否存在，json转义
        # if headers:
        #     header = json.loads(headers)
        # else:
        #     header = headers
        #
        # if cookies:
        #     cookie = json.loads(cookies)
        # else:
        #     cookie = cookies






        # # 2) 接口请求
        # request = Request()
        # # headers 转义json
        # # 验证params有没有内容
        #
        # if len(str(params).strip()) != 0:
        #     # 转换为str类型
        #     # params = json.loads(params)
        #     body_data = Base.read_body(params)
        #
        #     app_id = header["appId"]
        #     print(app_id)
        #     total_record = header["records"]
        #     print(total_record)
        #     body_digest = Base.read_digest(params, app_id)
        #     print(body_digest)
        #
        #     headers = {'appId': app_id, 'digest': body_digest, 'records': total_record}
        #     print(headers)
        #
        # # method post/get
        # if str(method).lower() == "get":
        #     res = request.get(url, json=body_data, headers=headers, cookies=cookie)
        # elif str(method).lower() == "post":
        #     res = request.post(url, json=body_data, headers=headers, cookies=cookie)
        # else:
        #     log.error("错误请求method:%s" %method)
        # return res

    def get_correlation(self, headers, cookies, pre_res):

        """
        关联
        :param headers:
        :param cookies:
        :param pre_res:
        :return:
        """
        # 验证是否有关联
        headers_para, cookies_para = Base.params_find(headers, cookies)
        print("获取到的headers_para值是：%s" % headers_para)
        # 有关联，执行前置用例，获取结果
        if len(headers_para):
            headers_data = pre_res['body'][headers_para[0]]
            print("token是：%s" % headers_data)
            headers = Base.res_sub(headers, headers_data)

        if len(cookies_para):
            cookies_data = pre_res["body"][cookies_para[0]]
            # 结果替换
            cookies = Base.res_sub(cookies, cookies_data)
        return headers, cookies




# TestExcel().test_run()

if __name__ == '__main__':
    # 执行(把执行用例生成的allure报告存储在./report/result中）
    # pytest.main(["-s", "test_excel_case_动态关联.py", "--alluredir", "./report/result"])

    # 生成报告（再将其装换成heml报告）
    # Base.allure_report("./report/result", "./report/html")

    report_path = Conf.get_report_path()+os.sep+"result"
    report_html_path = Conf.get_report_path() + os.sep + "html"
    pytest.main(["-s", "test_excel_case_动态关联.py", "--alluredir", report_path])
    # Base.allure_report("./report/result", "./report/html")
    Base.allure_report(report_path, report_html_path)
    Base.send_mail(title="接口测试报告结果", content=report_html_path)




    # pytest.main(["-s", "test_excel_case_动态关联.py"])
    # str1 = '{"Authorization": "JWT ${token}$"}'
    # if "${" in str1:
    #     print(str1)
    # import re
    # pattern = re.compile('\${(.*)}\$')
    # print(pattern)
    # re_res = pattern.findall(str1)
    # print(re_res)
    # print(re_res[0])
    # token = "123"
    # res = re.sub(pattern, token, str1)
    # print(res)