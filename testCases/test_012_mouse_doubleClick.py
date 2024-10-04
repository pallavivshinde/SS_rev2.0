import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

class Test_012_Right_Click():
    def test_012_Right_click(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        time.sleep(3)

        action = ActionChains(driver)

        dbl_click = driver.find_element(By.XPATH,'//button[text()="Double-Click Me To See Alert"]')
        time.sleep(3)

        action.double_click(dbl_click).perform()
        time.sleep(3)

        print("\n ********** HANDLING ALERT AFTER MOUSE ACTION DOUBLE CLICK ************")
        text1 = Alert(driver).text
        print(text1)

        Alert(driver).accept()
        assert True
        driver.close()




