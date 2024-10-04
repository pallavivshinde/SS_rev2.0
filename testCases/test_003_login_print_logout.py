import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_002_login_detailPrint():
    def test_002_loginDetail(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(3)
        driver.find_element(By.XPATH, '(//a[contains(text(),"Sign In ")])[1]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//input[@id="email"]').send_keys("pallavisr24@gmail.com")
        time.sleep(3)
        driver.find_element(By.XPATH, '(//input[@id="pass"])[1]').send_keys("pallavis@24")
        time.sleep(3)
        driver.find_element(By.XPATH, '(//span[text()="Sign In"])[1]').click()
        time.sleep(3)
        if (driver.title == "Home Page"):
            print("********* LOGIN IS DONE SUCCESSFULLY ***********")
            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_003.pass.png")

            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click()
            time.sleep(3)

            driver.find_element(By.XPATH,'(//a[text()="My Account"])[1]').click()
            time.sleep(3)

            print("\n ************ LOGIN NAME *********")
            TEXT1 = driver.find_element(By.XPATH,'(//p[contains(text(),"pallavi shinde")])[1]').text
            print("\n",TEXT1)

            print("\n ********* BILLING ADDRESS ************")
            text2 = driver.find_element(By.XPATH,"(//address[contains(text(),'pallavi shinde')])[1]").text
            print("\n",text2)

            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click()
            time.sleep(3)

            driver.find_element(By.XPATH, "(//a[normalize-space()='Sign Out'])[1]").click()
            assert True
            driver.close()
        else:
            print("********* SORRY, LOGIN IS FAILED ***********")
            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_003.fail.png")
            time.sleep(3)
            assert False




