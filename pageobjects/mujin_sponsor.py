import os.path
from my_framework.log import Logger
import yaml
from my_framework.file_case_import import file_process
from my_framework.element_location import location_element
from my_framework.base_page import BasePage
logger = Logger(logger="sponsor_page").getlog()
class sponsor_page(BasePage):

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

    # 平台方分发案件
    def case_dispense(self):
        name = 'element_sponsor=>case_manager/select_module1/search_case/name'
        search = 'element_sponsor=>case_manager/select_module1/search_case/search'
        select = 'element_sponsor=>case_manager/select_module1/search_case/select'
        button = 'element_sponsor=>case_manager/select_module1/case_dispense/button'
        organs = 'element_sponsor=>case_manager/select_module1/case_dispense/organs'
        organ_select = 'element_sponsor=>case_manager/select_module1/case_dispense/organ_select'
        submit = 'element_sponsor=>case_manager/select_module1/case_dispense/submit'
        lrst = file_process.get_data(u'姓名')
        for i in range(1,len(lrst)):
            self.clear(location_element(da,name))
            self.send_key(location_element(da,name),lrst[i])
            self.click(location_element(da,search))
            self.click(location_element(da,select))
            self.click(location_element(da,button))
            self.click(location_element(da,organs))
            self.click(location_element(da,organ_select))
            self.click(location_element(da,submit))



