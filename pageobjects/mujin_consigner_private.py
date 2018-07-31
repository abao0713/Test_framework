import os.path

import yaml

from my_framework.base_page import BasePage


class private_consigner_page(BasePage):
    # 导入案件
    #proDir = os.path.split(os.path.realpath(__file__))[0]
    #configPath = os.path.join(proDir, "config.ini")
    file_path = os.path.dirname(os.path.abspath('.')) + '\config_file\element.yaml'
    excel_path = os.path.dirname(os.path.abspath('.')) + '\config_file\case_import.xlsx'
    fs = open(file_path,'r',encoding="utf-8")
    da = yaml.load(fs.read())
    fs.close()
    data_module1 = da["case_manager"]

    #首先定义标准模板
    def import_case(self, type="standard"):
        #data = da["case_manager"]["select_module1"]
        print(self.data_module1["import_case"]["button"])
        self.click(self.data_module1["import_case"]["button"])
        if type == "standard":
            self.click(self.data_module1["import_case"]["standard_template"])
            self.click(self.data_module1["import_case"]["upload_file"]).send_keys("excel_path")
            self.click(self.data_module1["import_case"]["submit"])
        else:
            # 暂时不写
            self.click(self.data_module1["import_case"]["upload_file"]).send_keys("excel_path")

    # 输入模块和子模块，示例：案件管理/外访管理
    def module_select(self, module):
        if "/" not in module:
            self.click(self.da["module"])
        else:
            module_father = module.split('/')[0]
            module_child = module.split('/')[1]
            self.click(self.da[module_father]["element"])
            self.click(self.da[module_father][module_child])
if __name__ == '__main__':
    a = private_consigner_page(BasePage)
    a.import_case()