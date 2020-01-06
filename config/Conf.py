import os

from utils.YamlUtil import YamlReader

# 1.获取项目基本目录
# 获取当前项目的绝对路径
current = os.path.abspath(__file__)

# 获取父级目录
BASE_DIR = os.path.dirname(current)
BASE_DIR = os.path.dirname(os.path.dirname(current))

# 2.定义config目录的路径
_config_path = BASE_DIR + os.sep + "config"

# 3.定义conf.yml的路径
_config_file = _config_path + os.sep + "conf.yml"

# 定义logs文件路径
_log_path = BASE_DIR + os.sep + "logs"

# 定义db_conf.yml路径
_db_config_file = _config_path + os.sep +"db_conf.yml"

# 定义data目录路径
_data_path = BASE_DIR + os.sep +"data"

# 定义report目录路径
_report_path = BASE_DIR + os.sep +"report"






# 获取私有参数的方法

def get_config_path():
    return _config_path

def get_config_file():
    return _config_file

def get_log_path():
    """
    获取log文件路径
    :return:
    """
    return _log_path

def get_db_config_file():
    return _db_config_file


# 获取testlogin文件路径
def get_data_path():
    return _data_path

def get_report_path():
    """
    获取report绝对路径
    :return:
    """
    return _report_path



# 4.读取配置文件
# 创建类
class ConfigYaml:
    # 初始yaml读取配置文件
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()
        self.db_config = YamlReader(get_db_config_file()).data()

    # 获取文件内的内容
    def get_conf_url(self):
        """获取接口ip"""
        return self.config["BASE"]["test"]["url"]

    # 获取日志级别
    def get_conf_log(self):
        return self.config["BASE"]["log_level"]

    # 获取文件扩展名
    def get_conf_log_extension(self):
        return self.config["BASE"]["log_extension"]

    # 获取数据库配置相关信息
    def get_db_conf_info(self, db_alias):
        """
        根据db_alias获取 该名称下的数据库信息
        :param db_alias:
        :return:
        """
        return self.db_config[db_alias]

    def get_db_sql(self):
        return self.db_config["sql"]

    def get_excel_file(self):
        """
        获取测试用例excel名称
        :return:
        """
        return self.config["BASE"]["test"]["case_file"]

    def get_excel_sheet(self):
        """
        获取测试用例excel名称
        :return:
        """
        return self.config["BASE"]["test"]["case_sheet"]


    def get_email_info(self):
        """
        获取邮件配置相关信息
        :return:
        """
        return self.config["email"]


if __name__ == '__main__':
    conf_read = ConfigYaml()
    # print(conf_read.get_conf_url())
    # print(conf_read.get_conf_log())
    # print(conf_read.get_conf_log_extension())
    # print(conf_read.get_db_conf_info("db_1"))
    # print(conf_read.get_db_sql())
    print(conf_read.get_email_info())

    # print(conf_read.get_excel_file())
    # print(conf_read.get_excel_sheet())

    # 初始化数据库信息,Base.py