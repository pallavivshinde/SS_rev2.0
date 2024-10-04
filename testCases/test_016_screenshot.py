import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_016_Screenshot():
    def test_016_ss(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(25)

        driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("admin123")
        time.sleep(3)

        driver.find_element(By.XPATH,'//button[text()=" Login "]').click()
        time.sleep(3)

        try:
            driver.find_element(By.XPATH,'//i[@class="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]')

            print("\n ************* LOGIN IS DONE SUCCESSFULLY *********")
            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_016_ss_pass.png")
            time.sleep(3)
            driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]').click()
            time.sleep(3)
            driver.find_element(By.XPATH,'//a[text()="Logout"]').click()
            time.sleep(3)
            assert True
            driver.close()
        except:
            print("\n ************* LOGIN IS FAILED *********")
            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_016_ss_fail.png")
            time.sleep(3)

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





