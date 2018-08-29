from my_framework.log import Logger
import os.path
from configparser import ConfigParser
from my_framework.base_page import BasePage
#from my_framework.select_browser import BrowserEngine
from time import sleep
import yaml
from selenium.webdriver.common.action_chains import ActionChains

# create a logger instance
logger = Logger(logger="login_logout").getlog()
class login_logout(BasePage):
    yaml_consigner = os.path.dirname(os.path.abspath('.')) + '\config_file\element_consigner.yaml'
    yaml_assignee = os.path.dirname(os.path.abspath('.')) + '\config_file\element_assignee.yaml'
    yaml_sponsor = os.path.dirname(os.path.abspath('.')) + '\config_file\element_sponsor.yaml'
    #读取委案方元素定位文件
    fs_consigner = open(yaml_consigner, 'r', encoding="utf-8")
    data = yaml.load(fs_consigner.read())
    fs_consigner.close()
    # 读取催收方元素定位文件
    fs_assignee = open(yaml_assignee, 'r', encoding="utf-8")
    data_assignee = yaml.load(fs_assignee.read())
    fs_assignee.close()
    # 读取平台方元素定位文件
    fs_sponsor = open(yaml_sponsor, 'r', encoding="utf-8")
    data_sponsor = yaml.load(fs_sponsor.read())
    fs_sponsor.close()

    def login_consigner(self):
        #browser = BrowserEngine(self)
        #self.driver = browser.open_browser(self)
        config = ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config_file/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config_file/config.ini'
        config.read(file_path)

        username = config.get("userinfo", "c_username")
        logger.info("You select username is %s:" %username)
        password = config.get("userinfo", "c_password")
        logger.info("The test password acquire success")
        self.clear(self.data["login"]["user_input"])
        self.send_key(self.data["login"]["user_input"],username)
        self.clear(self.data["login"]["password_input"])
        self.send_key(self.data["login"]["password_input"],password)
        self.click(self.data["login"]["submit"])
        sleep(2)
        logger.info("Set time wait 2 seconds.")

    def logout_consigner(self):
        element = self.find_element(self.data["logout"]["location"])
        ActionChains(self.driver).move_to_element(element).perform()
        element2 = self.find_element(self.data["logout"]["out"])
        ActionChains(self.driver).click(element2).perform()

    def login_assignee(self):
        #browser = BrowserEngine(self)
        #self.driver = browser.open_browser(self)
        config = ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config_file/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config_file/config.ini'
        config.read(file_path)

        username = config.get("userinfo", "a_username")
        logger.info("You select username is %s:" %username)
        password = config.get("userinfo", "a_password")
        logger.info("The test password acquire success")
        self.clear(self.data_assignee["login"]["user_input"])
        self.send_key(self.data_assignee["login"]["user_input"],username)
        self.clear(self.data_assignee["login"]["password_input"])
        self.send_key(self.data_assignee["login"]["password_input"],password)
        self.click(self.data_assignee["login"]["submit"])
        sleep(2)
        logger.info("Set time wait 2 seconds.")

    def logout_assignee(self):
        element = self.find_element(self.data_assignee["logout"]["location"])
        ActionChains(self.driver).move_to_element(element).perform()
        element2 = self.find_element(self.data_assignee["logout"]["out"])
        ActionChains(self.driver).click(element2).perform()

    def login_sponsor(self):
        # browser = BrowserEngine(self)
        # self.driver = browser.open_browser(self)
        config = ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config_file/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config_file/config.ini'
        config.read(file_path)

        username = config.get("userinfo", "s_username")
        logger.info("You select username is %s:" % username)
        password = config.get("userinfo", "s_password")
        logger.info("The test password acquire success")
        self.clear(self.data_sponsor["login"]["user_input"])
        self.send_key(self.data_sponsor["login"]["user_input"], username)
        self.clear(self.data_sponsor["login"]["password_input"])
        self.send_key(self.data_sponsor["login"]["password_input"], password)
        self.click(self.data_sponsor["login"]["submit"])
        sleep(2)
        logger.info("Set time wait 2 seconds.")

    def logout_sponsor(self):
        element = self.find_element(self.data_sponsor["logout"]["location"])
        ActionChains(self.driver).move_to_element(element).perform()
        element2 = self.find_element(self.data_sponsor["logout"]["out"])
        ActionChains(self.driver).click(element2).perform()