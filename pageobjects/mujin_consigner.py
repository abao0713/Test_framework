import os.path
from my_framework.log import Logger
import yaml
from time import sleep
from my_framework.file_case_import import file_process
from my_framework.base_page import BasePage

logger = Logger(logger="consigner_page").getlog()
class consigner_page(BasePage):
    # 导入案件
    #proDir = os.path.split(os.path.realpath(__file__))[0]
    #configPath = os.path.join(proDir, "config.ini")
    file_path = os.path.dirname(os.path.abspath('__file__')) + '\config_file\element_consigner.yaml'
    excel = file_process()
    file_name = excel.create_excel_file()
    excel_path = os.path.dirname(os.path.abspath('__file__')) + '\config_file\case_import'
    ecl = os.path.join(excel_path, file_name)
    fs = open(file_path,'r',encoding="utf-8")
    da = yaml.load(fs.read())
    fs.close()
    data_module1 = da["case_manager"]["select_module1"]

    #选择模板
    def import_case(self, type="standard"):
        #data = da["case_manager"]["select_module1"]
        self.click(self.data_module1["import_case"]["button"])

        # 首先定义标准模板
        if type == "standard":
            self.click(self.data_module1["import_case"]["standard_template"])
            self.click(self.data_module1["import_case"]["upload_file"])
            self.send_key(self.data_module1["import_case"]["upload_file"],self.ecl)
            self.click(self.data_module1["import_case"]["submit"])
            sleep(5)
            logger.info("Set implicitly wait 5 seconds.")
        #定义自定义模板
        else:
            # 暂时不写
            self.click(self.data_module1["import_case"]["upload_file"])
            self.send_key(self.data_module1["import_case"]["upload_file"], "excel_path")

    # 输入模块和子模块，示例：案件管理/外访管理（需重写）
    def module_select(self, module):
        if "/" not in module:
            self.click(self.da["module"])
        else:
            module_father = module.split('/')[0]
            module_child = module.split('/')[1]
            self.click(self.da[module_father]["element"])
            self.click(self.da[module_father][module_child])
    #def case_search(self,):


if __name__ == '__main__':
    a = consigner_page(BasePage)
    a.import_case()