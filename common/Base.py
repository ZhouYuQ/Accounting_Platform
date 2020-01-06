from utils.Base64Util import Read
from config.Conf import ConfigYaml
from utils.MysqlUtil import Mysql
import json
import re
from utils.AssertUtil import AssertUtil
from utils.LogUtil import my_log
import subprocess
from config.Conf import ConfigYaml
from utils.EmailUtil import SendEmail

read = Read()
log = my_log()


p_data ='\${(.*)}\$'


def read_body(payload):
    """
    获取加密请求体
    :param payload:
    :return:
    """
    body_data = read.base64_code(payload)
    return body_data


def read_digest(payload, app_id):
    """
    获取请求头摘要
    :param payload:
    :param app_id:
    :return:
    """
    body_digest = read.sha256_code(payload, app_id)
    return body_digest


# 1.定义init_db
def init_db(db_alias):
    # 获取数据库配置信息
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host = db_info["db_host"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    db_name = db_info["db_name"]
    charset = db_info["db_charset"]
    port = int(db_info["db_port"])

# 初始化mysql对象
    conn = Mysql(host, user, password, db_name, charset, port)
    print(conn)
    return conn



def json_parse(data):
    """格式化字符转换json格式"""
    # 判断json是否存在，json转义
    # if headers:
    #     header = json.loads(headers)
    # else:
    #     header = headers
    return json.loads(data) if data else data

def res_find(data, pattern_data=p_data):
    """查询"""
    # pattern = re.compile('\${(.*)}\$')
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    return re_res


def res_sub(data,replace,pattern_data=p_data):
    """
    替换
    :param data: 原来的参数
    :param replace: 替换的内容
    :param pattern_dat：查询的内容
    :return:
    """
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    if re_res:
       return re.sub(pattern_data,replace,data)
    return re_res

def params_find(headers,cookies):
    """
    验证请求中是否有${}$;需要结果关联
    :param headers:
    :param cookies:
    :return:
    """
    if "${" in headers:
        headers = res_find(headers)

    if "${" in cookies:
        cookies = res_find(cookies)
    return headers,cookies

def assert_db(db_name,result,db_verify):
    assert_util = AssertUtil()
    sql = init_db("db_name")
    # 2.查询sql，excel定义好的
    db_res = sql.fetcone(db_verify)
    log.debug("数据库查询结果：{}".format(str(db_res)))
    # 数据库结果与接口返回的结果验证
    # 获取数据库结果的key
    verify_list = list(dict(db_res).keys())
    # 根据key获取数据库结果，接口结果
    for line in verify_list:
        # res_line = res["body"][line]
        res_line = result[line]
        res_db_line = dict(db_res)[line]
        # 验证
        assert_util.assert_body(res_line, res_db_line)


def allure_report(report_path,report_html):
    """
    生成allure报告
    :param report_path:
    :param report_html:
    :return:
    """
    # 1.定义执行命令allure generate
    allure_cmd = "allure generate %s -o %s --clean"%(report_path, report_html)
    # 2.subprocess.call进行执行
    log.info("报告地址")
    try:
        subprocess.call(allure_cmd, shell=True)
    except:
        log.error("执行用例失败，请检查一下相关配置")
        raise


def send_mail(report_html_path="", content="", title="测试"):
    """
    发送邮件
    :param report_html_path:
    :param content:
    :param title:
    :return:
    """
    email_info = ConfigYaml().get_email_info()
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    recv = email_info["receiver"]
    email = SendEmail(
        smtp_addr=smtp_addr,
        username=username,
        password=password,
        recv=recv,
        title=title,
        content=content,
        file=report_html_path)
    email.send_mail()




if __name__ == '__main__':
    # payload = "{'checkinList':[{'tranDate':'2019-08-26','srcNo':'000912', 'eventCode':'JJGM001','prdCode':'JJGM','ccy':'156','amt':888.88,'aux1':'L009','aux2':'000083','aux4':'N100696C00008','extSet':{'companyCode':'N100696C00008','custno':'000000367699','purchaseFare':'35.79','purchaseDate':'20190130','orderNumber':'3390000002020','fundProductCode':'000083','companyName':'汇添富基金管理股份有限公司','fundProductName':'添富消费行业混合','redeemDate':'','redeemFare':'','fconfirmbalance':'6000','fundTypeName':'混合型','fconfirmshares':'','fundTypeCode':'mix','businessType':'02'}}]}"
    # app_id = "N100696-L009"
    # print(read_body(payload))
    # print(read_digest(payload, app_id))

    # init_db("db_1")
    print(res_find('{"Authorization": "JWT ${token}$"}'))
    print(res_sub('{"Authorization": "JWT ${token}$"}', "123"))



