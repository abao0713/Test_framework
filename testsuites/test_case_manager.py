from pageobjects.login_logout import login_logout
from my_framework.select_browser import BrowserEngine
import unittest
from pageobjects.mujin_consigner import consigner_page


class Case_manager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        a = login_logout(cls.driver)
        a.login_consigner()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        a = login_logout(cls.driver)
        a.logout_consigner()

    def test_import_case(self):
        #self.module
        homepage = consigner_page(self.driver)
        homepage.module_select("case_manager/select_module1")
        homepage.import_case()


if __name__ == '__main__':
    unittest.main()