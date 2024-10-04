import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_005_MultipleWindow():
    def test_005_Multiple_window(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://demo.automationtesting.in/Windows.html")
        time.sleep(3)

        driver.find_element(By.XPATH,'(//button[@class="btn btn-info"])[1]').click()
        time.sleep(3)
        all_windoes = driver.window_handles


        driver.switch_to.window(all_windoes[1])
        title0 = driver.title
        print("\n****** TITLE OF CHILD WINDOW ********")
        print(title0)

        print("\n ***** TEXT IN CHILD WINDOW **********")
        text0 = driver.find_element(By.XPATH,'//h1[@class="d-1 fw-bold"]').text
        print(text0)

        driver.switch_to.window(all_windoes[0])

        title1 = driver.title
        print("\n****** TITLE OF PARENT WINDOW ********")
        print(title1)

        print("\n ***** TEXT IN PARENT WINDOW **********")
        text1 = driver.find_element(By.XPATH, "//p[contains(text(),'If you set the target attribute to')]").text
        print(text1)
        assert True
        driver.close()








