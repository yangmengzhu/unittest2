import sys,csv


import time
import unittest
import ddt
from selenium import webdriver
from ddt import ddt, data, file_data, unpack

@ddt
class baidu03(unittest.TestCase):
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

    def getCsv(file_name):
        rows=[]
        path=sys.path[0]

        with open(path+'/data/'+file_name,'rt',encoding='utf-8') as f:
            readers=csv.reader(f,delimiter=',',quotechar='|')
            next(readers,None)
            for row in readers:
                temprows=[]
                for i in row:
                    temprows.append(i)
                rows.append(temprows)
            return rows

    @unittest.skip("skipping")
    @data(["lisa",u"lisa_百度搜索"],["毛不易",u"毛不易_百度搜索"],["张一山",u"张一山_百度搜索"])
    @unpack
    def test_baidu(self, value,expected_value):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(5)
        self.assertEqual(expected_value,driver.title,msg="不一致")
        time.sleep(5)

    @unittest.skip("skipping")
    @data(*getCsv('test_baidu_data.txt') )
    @unpack
    def test_baidu1(self, value,expected_value):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(6)
        self.assertEqual(expected_value, driver.title, msg="不一致")
        time.sleep(6)

    @file_data('test_baidu_data.json')
    def test_baidu1(self, value):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(6)

    @unittest.skip("skipping")
    def test_hao(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("hao123").click()
        time.sleep(6)



if __name__=="main__":
    unittest.main()