import xlrd


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
        sheet = data.sheet_by_index(self.sheet_id)
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
    def write_value(self):
        data.write(0, 0, 'this should overwrite1')


# 封装excel的列名常量
def get_bill_code():
    """获取caseSeq"""
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


if __name__ == '__main__':
    test = HandleExcel()
    print(test.get_data())
    print(test.get_rows())
    print(test.get_value(0, 0))