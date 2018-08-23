import os.path
from my_framework.log import Logger
import yaml
from time import sleep
from my_framework.file_case_import import file_process
from my_framework.base_page import BasePage
logger = Logger(logger="sponsor_page").getlog()
class sponsor_page(BasePage):
    def case_dispense(self):

