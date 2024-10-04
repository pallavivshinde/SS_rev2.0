import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_013_Scroll_By():
    def test_013_ScrollBy(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://www.bbc.com/")
        time.sleep(3)
        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_013_beforeScroll.png")

        driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(3)

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_013_afterScroll.png")
        time.sleep(3)

        driver.close()
