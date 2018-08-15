import xlrd
from my_framework.log import Logger
import time
import os

# create a logger instance
logger = Logger(logger="file_process").getlog()

class file_process():
    """封装操作excel的方法"""
    excel_path = os.path.dirname(os.path.abspath('.')) + '\config_file\case_import.xlsx'
    def __init__(self, file=excel_path, sheet_id=0):
        self.file = file
        self.sheet_id = sheet_id
        self.data = self.get_data()
        # 为了在创建一个实例时就获得excel的sheet对象，可以在构造器中调用get_data()
        # 因为类在实例化时就会自动调用构造器，这样在创建一个实例时就会自动获得sheet对象了

    # 获取某一页sheet对象
    def get_data(self):
        data = xlrd.open_workbook(self.file)
        sheet = data.sheet_by_index(self.sheet_id,cell_overwrite_ok=True)
        return sheet

    # 获取excel数据行数
    def get_rows(self):
        rows = self.data.nrows
        # t = self.get_data()  # 调用get_data()取得sheet对象(如果不在构造器获取sheet对象，就需要在方法内先获取sheet对象，再进行下一步操作，每个方法都要这样，所以还是写在构造器中方便)
        # rows = t.nrows
        return rows

    # 获取某个单元格数据
    def get_value(self, row, col):
        value = self.data.cell_value(row, col)
        return value

    # 向某个单元格写入数据
    def write_value(self,srt):

        self.get_data().write(0, 0, srt)
    #定位需要写入的位置
    def location(self,line,column,str):
        """
        :param line: 定位需要写入的行
        :param column:定位需要写入的列
        :param str:需要写入的字符
        :return:
        """
        data.write(line, column, srt)
#        logger.info("success writing %s",%str)
#封装需要写入的常量


# 封装excel的列名常量
def get_bill_code():
    """获取bill_code"""
    caseSeq = 0
    return caseSeq


def get_apitype():
    """获取apiType"""
    apiType = 1
    return apiType


def get_apiseq():
    """获取apiSeq"""
    apiSeq = 2
    return apiSeq


def get_apiName():
    """获取apiName"""
    apiName = 3
    return apiName


def get_priority():
    """获取priority"""
    priority = 4
    return priority


def get_url():
    """获取url"""
    url = 5
    return url


def get_method():
    """获取method"""
    method = 6
    return method


def get_header():
    """获取header"""
    header = 7
    return header


def get_purpose():
    purpose = 8
    return purpose


def get_params():
    """获取params"""
    params = 9
    return params


def get_expectvalue():
    """获取expectValue"""
    expect = 10
    return expect


def set_bill_code():
    da = time.strftime("%Y-%m-%d/%H:%M:%S", time.localtime())
    da_a =da.split('/')[0]
    da_b =da.split('/')[1]
    print(da_a)
    print(da_b)
    a = file_process()
    for i in range(1,6):
        a.get_data().write(i, 1, str = (da_a+"00"+i))
        logger.info("success writing s%" %str)









if __name__ == '__main__':
    #a=file_process()
    set_bill_code()
