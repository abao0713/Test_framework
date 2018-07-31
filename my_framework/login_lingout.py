from my_framework.log import Logger
import os.path
from configparser import ConfigParser
from my_framework.base_page import BasePage
import yaml
# create a logger instance
logger = Logger(logger="login_logout").getlog()
class login_logout(BasePage):
    file_path = os.path.dirname(os.path.abspath('.')) + '\config_file\element.yaml'
    fs = open(file_path, 'r', encoding="utf-8")
    data = yaml.load(fs.read())
    fs.close()
    def login_consigner(self):
        config = ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config_file/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config_file/config.ini'
        config.read(file_path)

        username = config.get("userinfo", "c_username")
        logger.info("You select username is :" % c_username)
        password = config.get("userinfo", "c_password")
        logger.info("The test password acquire success")
        self.clear(self.data["login"]["user_input"])
        self.click(self.data["login"]["user_input"]).send_keys(username)
        self.clear(self.data["login"]["password_input"])
        self.click(self.data["login"]["password_input"]).send_keys(password)
        self.click(self.data["login"]["submit"])
        refresh()
    def logout_consigner(self):
        pass


