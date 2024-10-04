import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Test_010_RightClick():
    def test_010_Right_click(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://vinothqaacademy.com/mouse-event/")
        time.sleep(3)
        right_click= driver.find_element(By.XPATH,'//button[text()="Right Click Me"]')
        action= ActionChains(driver)
        action.context_click(right_click).perform()
        time.sleep(5)
        driver.find_element(By.XPATH,'//a[text()="Alert Popup"]').click()
        time.sleep(3)
        if ( driver.title=='Demo Site - Alert and Popup - Vinoth Q.A Academy'):
            print("\n ****** RIGHT CLICK ACTION IS DONE *********")
            driver.close()
            assert True
        else:
            print("\n ****** RIGHT CLICK ACTION IS FAILED *********")
            assert False

