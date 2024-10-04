import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Test_008_FB_DropDown():
    def test_008_DropDown(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://en-gb.facebook.com/")
        time.sleep(3)
        driver.find_element(By.XPATH,'//a[text()="Create new account"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH,'//input[@name="firstname"]').send_keys("pallavi")
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@name="lastname"]').send_keys("rpatil")
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@name="reg_email__"]').send_keys("spallavi24@gmail.com")
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@id="password_step_input"]').send_keys("1234")
        time.sleep(3)

        day= Select(driver.find_element(By.XPATH,'//select[@id="day"]'))
        day.select_by_value("5")

        mon = Select(driver.find_element(By.XPATH,'//select[@id="month"]'))
        mon.select_by_index(2)

        year = Select(driver.find_element(By.XPATH,'//select[@id="year"]'))
        year.select_by_visible_text('2000')

        btn = driver.find_element(By.XPATH,"//label[text()='Female']")
        btn.click()
        print("btn is selected or not",btn.is_selected())
        time.sleep(3)


        driver.close()
        assert True