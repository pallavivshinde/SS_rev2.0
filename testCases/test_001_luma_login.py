import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_001_luma_reg():
    def test_001_luma(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(2)
        driver.find_element(By.XPATH, "(//a[text()='Create an Account'])[1]" ).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,'input[id="firstname"]').send_keys('pallavi')
        time.sleep(2)
        driver.find_element(By.ID,'lastname').send_keys('shinde')
        time.sleep(2)
        driver.find_element(By.NAME,'email').send_keys('pallavisr24@gmail.com')
        time.sleep(2)
        driver.find_element(By.XPATH,'(//input[@name="password"])[1]').send_keys('pallavis@24')
        time.sleep(2)
        driver.find_element(By.XPATH,'//input[@name="password_confirmation"]').send_keys('pallavis@24')
        time.sleep(2)
        driver.find_element(By.XPATH,'(//span[text()="Create an Account"])[1]').click()
        time.sleep(10)
        if(driver.title == "My Account"):
            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\AutomationPrg\\Screenshots\\test_001_luma_login.pass.png")
            print("\n *********** REGISTRATION IS SUCCESSFULL ****************")
            assert True
        else:
            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\AutomationPrg\\Screenshots\\test_001_luma_login.fail.png")
            print("\n *********** REGISTRATION UNSUCCESSFULL ****************")
            assert False


