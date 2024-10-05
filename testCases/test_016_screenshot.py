import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_016_Screenshot():
    def test_016_ss(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()

        driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9jdXN0b21lci9hY2NvdW50L2xvZ291dFN1Y2Nlc3Mv/")
        time.sleep(25)

        driver.find_element(By.XPATH,'//input[@id="email"]').send_keys("pallavirg@gmail.com")
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@id="pass"]').send_keys("Pallavi123")
        time.sleep(3)

        driver.find_element(By.XPATH,'(//button[@id="send2"])[1]').click()
        time.sleep(3)

        if(driver.title=="My Account"):
            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_016_ss_pass.png")
            print("\n-----------YOU ARE AT THE LOGIN PAGE-------------\n")
            driver.find_element(By.XPATH,'(//button[@class="action switch"])[1]').click()
            driver.find_element(By.XPATH,"(//a[normalize-space()='Sign Out'])[1]").click()
            time.sleep(3)
            driver.close()
            assert True
        else:
            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_016_ss_fail.png")
            print("\n-----------SORRY,SOMETHING WENT WRONG-------------\n")
            driver.close()
            assert False


    def test_016_addition(self):
        a=10
        b=5
        add= a+b
        if (add==15):
            print("\n--------- ADDITION IS SUCCESSFUL ------------\n")
            print("addition",add)
            assert True

        else:
            print("\n -----------ADDITION IS FAILED ---------------\n")
            assert False





