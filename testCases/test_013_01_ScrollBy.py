import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_013_01_ScrollBy():
    def test_103_01_scrollBy(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://ed.ted.com/?utm_term=ted%20ed&utm_campaign=TED-Ed+site&utm_source=adwords&utm_medium=ppc&hsa_acc=7777130675&hsa_cam=18739292599&hsa_grp=151439764548&hsa_ad=631444589734&hsa_src=g&hsa_tgt=kwd-296155107571&hsa_kw=ted%20ed&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQjwxsm3BhDrARIsAMtVz6O8hI-lJIwThcqbdly9xoiHpTVh8uSHhjZ8lcKcijGFYvD6JCIEplMaAk-pEALw_wcB")
        time.sleep(3)

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_013_01_beforeScroll.png")

        driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(3)

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_013_afterScroll.png")

        driver.close()