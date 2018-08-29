import os.path
from my_framework.log import Logger
import yaml
from my_framework.file_case_import import file_process
from my_framework.element_location import location_element
from my_framework.base_page import BasePage
logger = Logger(logger="assignee_page").getlog()
class assignee_page(BasePage):
    def __init__(self):


        # proDir = os.path.split(os.path.realpath(__file__))[0]
        # configPath = os.path.join(proDir, "config.ini")
        file_path = os.path.dirname(os.path.abspath('.')) + '\config_file\element_assignee.yaml'
        excel = file_process()
        file_name = excel.create_excel_file()
        excel_path = os.path.dirname(os.path.abspath('.')) + '\config_file\case_import'
        ecl = os.path.join(excel_path, file_name)
        fs = open(file_path, 'r', encoding="utf-8")
        self.da = yaml.load(fs.read())
        fs.close()
    # 催收方分发案件(需要采用select的方法)
    def case_dispense(self,num='1'):
        """

        :param num: 1=人工分案；2=人工调案；3=按搜索分案
        :return:
        """
        lrst = file_process.get_data(u'姓名')
        #分案元素信息

        for i in range(1,len(lrst)):
            location = 'element_assignee=>case_manager/select_module1/search_case/name'
            select = 'element_assignee=>case_manager/select_module1/search_case/select'
            # 分案元素信息
            button1 = 'element_assignee=>case_manager/select_module1/case_dispense/button1'
            button2 = 'element_assignee=>case_manager/select_module1/case_dispense/button2'
            button3 = 'element_assignee=>case_manager/select_module1/case_dispense/button3'

            self.case_search(lrst[i],location)

            if num == '1':
                self.click(location_element(self.da,select))
                self.click(location_element(self.da,button1))
            elif num == '2':
                self.click(location_element(self.da, select))
                self.click(location_element(self.da, button2))

            else:
                self.click(location_element(self.da, button3))

    def case_search(self,str,location):
        """

        :param search: 需要查询的字符
        :param location: 字符所在的定位信息
        :return:
        """
        spread = 'element_assignee=>case_manager/select_module1/search_case/spread'
        search = 'element_assignee=>case_manager/select_module1/search_case/search'
        reset = 'element_assignee=>case_manager/select_module1/search_case/reset'
        self.click(location_element(self.da,spread))
        self.click(location_element(self.da,reset))
        self.clear(location_element(self.da, location))
        self.send_key(location_element(self.da, location), str)
        self.click(location_element(self.da, search))
        self.click(location_element(self.da, reset))