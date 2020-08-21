import os
import time

from selenium import webdriver

driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath("D:/360安全浏览器下载/selenium2html/upload.html")
driver.get(file_path)
driver.maximize_window()
time.sleep(5)
# driver.find_element_by_id("show_modal").click()
# div1=driver.find_element_by_class_name("madal-body")
# div1.find_element_by_link_text("click me").click()
# time.sleep(5)
# div2=driver.find_element_by_class_name("madal-footer")
# buttons=div2.find_elements_by_tag_name("button")
# buttons[0].click()

driver.find_element_by_name("file").send_keys("D:/360安全浏览器下载/selenium2html/upload.html")
time.sleep(5)

driver.quit()