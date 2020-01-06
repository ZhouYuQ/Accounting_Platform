from common import Base
from utils.RequestsUtil import Request
from config.Conf import ConfigYaml
import pytest
from utils.AssertUtil import AssertUtil
from common.Base import init_db


request = Request()
conf_yaml = ConfigYaml()

# 登记
def test_login():
    """添加一条当天数据"""
    url = conf_yaml.get_conf_url()+"/api/serial/checkin"
    payload = "{'checkinList':[{'tranDate':'2019-12-24','srcNo':'0001026', 'eventCode':'JJGM001','prdCode':'JJGM','ccy':'156','amt':888.88,'aux1':'L009','aux2':'000083','aux4':'N100696C00008','extSet':{'companyCode':'N100696C00008','custno':'000000367699','purchaseFare':'35.79','purchaseDate':'20190130','orderNumber':'3390000002020','fundProductCode':'000083','companyName':'汇添富基金管理股份有限公司','fundProductName':'添富消费行业混合','redeemDate':'','redeemFare':'','fconfirmbalance':'6000','fundTypeName':'混合型','fconfirmshares':'','fundTypeCode':'mix','businessType':'02'}}]}"
    # print(payload)
    # 请求体
    body_data = Base.read_body(payload)

    # 请求头信息
    app_id = "N100696-L009"
    body_digest = Base.read_digest(payload, app_id)
    total_record = '2'

    headers = {'appId': app_id, 'digest': body_digest, 'records': total_record}
    r = request.post(url, json=body_data, headers=headers)
    print(r)
    code = r["code"]
    body = r["body"]

    body_l = AssertUtil().assert_body_header(body)


    AssertUtil().assert_code(code, 200)
    AssertUtil().assert_body(body["resultCode"], '1000')
    AssertUtil().assert_body(body["resultDesc"], "操作成功")
    AssertUtil().assert_body(body["failureList"], [])
    # AssertUtil().assert_body(body_l[0], "数据库唯一约束冲突，数据重复")


    # 初始化数据库对象
    conn = init_db("db_1")
    # 查询结果
    res_db = conn.fetcone("select * from gls_s_std_serial_l009 where src_no='0001025'")
    print("数据库查询结果：%s"%res_db)
    # 验证
    src_no = "0001025"
    assert src_no == res_db["src_no"]





if __name__ == '__main__':
    pytest.main(["-s", "test_mail.py"])




