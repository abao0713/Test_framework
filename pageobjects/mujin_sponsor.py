import os.path
from my_framework.log import Logger
import yaml
from my_framework.file_case_import import file_process
from my_framework.file_case_import import file_process
from my_framework.element_location import location_element
from my_framework.base_page import BasePage
logger = Logger(logger="sponsor_page").getlog()
class sponsor_page(BasePage):
    # 平台方分发案件
    # proDir = os.path.split(os.path.realpath(__file__))[0]
    # configPath = os.path.join(proDir, "config.ini")
    file_path = os.path.dirname(os.path.abspath('.')) + '\config_file\element_sponsor.yaml'
    excel = file_process()
    file_name = excel.create_excel_file()
    excel_path = os.path.dirname(os.path.abspath('.')) + '\config_file\case_import'
    ecl = os.path.join(excel_path, file_name)
    fs = open(file_path, 'r', encoding="utf-8")
    da = yaml.load(fs.read())
    fs.close()

    def case_dispense(self):
        location = 'element_sponsor=>case_manager/select_module1/search_case/bill_code'
        lrst = file_process.get_data(u'姓名')
        for name in lrst:

            self.clear(location_element(da,location))
            self.send_key(location_element(da,location))


