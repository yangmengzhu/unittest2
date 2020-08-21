import os
import time
import unittest

from selenium import webdriver


class baidu02(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url="https://www.baidu.com/"
        self.driver.maximize_window()
        self.verficationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verficationErrors )

    def test_baidusearch(self):
        driver=self.driver
        driver.get(self.base_url)
        time.sleep(3)
        driver.find_element_by_id("kw").send_keys("明日之子")
        driver.find_element_by_id("su").click()
        try:
            self.assertEqual("明日之子_百度搜索", driver.title, msg="hahah")
        except:
            self.saveScreenShot(driver,"error.png")
        time.sleep(3)

    def saveScreenShot(self,driver,file_name):
        if not os.path.exists("../errorImage"):
            os.makedirs("../errorImage")
        now=time.strftime("%Y%m%S-%H%M%S",time.localtime(time.time()))
        driver.get_screenshot_as_file("./errorImage"+now+"-"+file_name)
        time.sleep(3)

    @unittest.skip("skipping")#忽略此方法
    def test_hao1(self):
        driver=self.driver
        driver.get(self.base_url)
        time.sleep(3)
        driver.find_element_by_link_text("hao123").click()
        time.sleep(3)

    def test_hao(self):
        driver=self.driver
        driver.get(self.base_url)
        time.sleep(3)
        driver.find_element_by_link_text("新闻").click()
        time.sleep(3)

   # @unittest.skip("skipping")
    def test_baidusearch1(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        driver.find_element_by_id("kw").send_keys(u"毛不易")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        self.assertEqual("毛不易_百度搜索",driver.title,msg="网页未打开")
        time.sleep(3)

if __name__=="__main__":
    unittest.main()



