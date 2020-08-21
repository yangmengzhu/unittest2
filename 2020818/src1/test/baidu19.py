import time
import unittest

from selenium import webdriver


class baidu01(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url="https://www.baidu.com/"
        self.driver.maximize_window()
        self.verficationErrors=[]
        self.accept_next_alert=True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verficationErrors)

    def test_hao(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("hao123").click()
        time.sleep(6)

    def test_baiduSearch(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys(u"明日之子")
        driver.find_element_by_id("su").click()
        time.sleep(6)

if __name__=="main__":
    unittest.main()