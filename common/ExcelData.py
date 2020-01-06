from utils.ExeclUtil import ExcelReader
from common.ExcelConfig import DateConfig

# 使用excel工具类，获取结果list

class Data:
    def __init__(self, testcase_flie, sheet_name):
        self.reader = ExcelReader(testcase_flie, sheet_name)
        print("获取到全部用例为：%s"%self.reader.data_excel())

        # 列是否运行y
    def get_run_data(self):
        """
        获取是否执行测试用例的方法
        :return:
        """
        run_list = list()
        for line in self.reader.data_excel():
            if str(line[DateConfig().is_run]).lower() == "y":
                # print(line)
        # 保存要执行的结果，放到新的列表
                run_list.append(line)
        return run_list

    # 获取全部的测试用例
    def get_case_list(self):
        # run_list = list()
        # for line in self.reader.data_excel():
        #     run_list.append(line)
        # 列表推倒
        run_list = [line for line in self.reader.data_excel()]
        return run_list

    # 根据前置条件：从全部的测试用例当中取到前置对应的测试用例
    def get_case_pre(self,pre):
        #获取全部的测试用例
        # list判断哪些用例是需要执行的
        run_list = self.get_case_list()
        for line in run_list:
            if pre in dict(line).values():
                return line
        return None




