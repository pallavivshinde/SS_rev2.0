import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class Test_004_AlertHandling():
    # def test_004_01_simpleAlert(self):
    #     driver = webdriver.Chrome()
    #     driver.implicitly_wait(10)
    #     driver.maximize_window()
    #     driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
    #     time.sleep(3)
    #
    #     driver.find_element(By.XPATH,'//input[@id="alertexamples"]').click()
    #     time.sleep(3)
    #
    #     text1 = Alert(driver).text
    #     print("\n ******** SIMPLE ALERT TEXT ************")
    #     print(text1)
    #
    #     Alert(driver).accept()
    #     driver.close()
    #     assert True

    def test_004_02_ConfirmAlert(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@id="confirmexample"]').click()
        time.sleep(3)

        Alert(driver).accept()

        print("\n ******** CONFIRM ALERT TEXT***************")
        text2 = driver.find_element(By.XPATH,'//p[@id="confirmexplanation"]').text
        print("\n",text2)

        driver.close()

    def test_004_03_PromptAlert(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@id="promptexample"]').click()
        time.sleep(3)

        Alert(driver).send_keys("hello pallavi")
        text3 = Alert(driver).text
        print("\n ******** PROMPT TEXT***********")
        print("\n ", text3)

        Alert(driver).accept()

        text3_1 = driver.find_element(By.XPATH,'//p[@id="promptexplanation"]').text
        print("\n ********** PRINTING ACTION ON PROMPT ALERT********")
        print("\n",text3_1)

        driver.close()



