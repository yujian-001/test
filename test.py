# print "hello world"

from selenium import webdriver

driver=webdriver.Chrome("/usr/bin/chromedriver")

driver.implicitly_wait(5)

driver.get("http://www.baidu.com")