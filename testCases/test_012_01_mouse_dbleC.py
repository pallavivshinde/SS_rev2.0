import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains


class Test_012_01_MouseDC():
    def test_012_01_double_click(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://artoftesting.com/samplesiteforselenium")
        time.sleep(3)

        mouseDc= driver.find_element(By.XPATH,'//button[text()="Double-click to generate alert box"]')

        action = ActionChains(driver)

        action.double_click(mouseDc).perform()

        text1 = Alert(driver).text
        print(text1)

        Alert(driver).accept()

        driver.close()
        assert True
