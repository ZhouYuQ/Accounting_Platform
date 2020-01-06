from utils.LogUtil import my_log
import pymysql


# 1.创建封装类
class Mysql:
# 2.初始化数据，连接数据库，光标对象
    def __init__(self, host, user, password, database, charset="utf8", port=3306):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port
        )

        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.log = my_log()
# 3.创建查询、执行方法
    def fetcone(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 清除表数据
    def clear(self, sql):
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("Mysql 执行失败")
            self.log.error(ex)
            return False
        return True

    # 插入表数据
    def insert(self, table_name, table_data):
        try:
            if self.conn and self.cursor:
                for key in table_data:
                    table_data[key] = "'" + str(table_data[key]) + "'"
                key = ','.join(table_data.keys())
                value = ','.join(table_data.values())
                sql = ("INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")")
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("Mysql 执行失败")
            self.log.error(ex)
            return False
        return True



    def exec(self, sql):
        """
        执行更新操作
        :return:
        """
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("Mysql 执行失败")
            self.log.error(ex)
            return False
        return True

# 4.关闭对象
    def __del__(self):
        # 关闭光标
        if self.cursor is not None:
            self.cursor.close()
        # 关闭数据库连接
        if self.conn is not None:
            self.conn.close()



if __name__ == '__main__':
    mysql = Mysql("10.152.16.114",
                  "camb_kaifa_w",
                  "YzNmZWMxZTFjNzVmYmJk",
                  "camb")
    res = mysql.fetchall("select * from gls_s_std_serial_l00805 where tran_date='2019-12-17' and src_")
    print(res)
    # res = mysql.clear("delete from gls_s_std_serial_l00805 where tran_date='2019-12-17'")

    # datas = {
    #     # 发布会数据
    #     'gls_s_std_serial_l00805': [
    #         {'busi_line': 'L00805', 'busi_brc': 'N100703', 'tran_Date': '2019-12-20', 'src_no': '12000021',
    #          'serial_no': '191218120717', 'event_code': 'HLW0001', 'prd_code': 'YB', 'ccy': '人民币', 'amt': 888},
    #   ]
    # }
    #
    # for table, data in datas.items():  # items() 方法以列表返回可遍历的(键, 值) 元组数组
    #     for d in data:
    #        res = mysql.insert(table, d)
    #        print(res)

# 这些配置信息可以放在配置文件中进行读取；创建db_conf.yml文件





# # 1.导入pymysql包
# import pymysql
# # 2.连接数据库
# conn = pymysql.connect(
#     host="10.152.16.114",
#     user="camb_kaifa_w",
#     password="YzNmZWMxZTFjNzVmYmJk",
#     database="camb",
#     charset="utf8",
#     port=3306
# )
# # 3.获取执行sql的光标对象
# cursor = conn.cursor()
# # 4.执行sql
# sql = "select * from gls_s_std_serial_l00805 where tran_date='2019-12-17' "
# cursor.execute(sql)
# res = cursor.fetchone()
# print(res)
# # 5.关闭对象
# cursor.close()
# conn.close()