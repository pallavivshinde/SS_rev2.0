import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Test_007_ExplicitWait():
    def test_007_explicitWait(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()

        driver.get("https://www.google.co.in/")
        time.sleep(3)
        driver.find_element(By.XPATH, '//textarea[@title="Search"]').send_keys("INTERNET SPEED TEST")
        time.sleep(3)

        driver.find_element(By.XPATH, '(//input[@value="Google Search"])[2]').click()
        time.sleep(3)

        driver.find_element(By.XPATH, '//div[text()="RUN SPEED TEST"]').click()
        time.sleep(5)

        try:
            wait = WebDriverWait(driver,25,poll_frequency=0.5)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'(//div[@class="lv7K9c"])[3]')))

            print("\n ********** DOWNLOAD SPEED**********")
            text1 = driver.find_element(By.XPATH, '//div[@class="oyUhj"]').text
            print("\n my downloaded speed is:", text1, "mbps")
            time.sleep(3)

            print("\n ******** UPLOAD SPEED *************")
            text2 = driver.find_element(By.XPATH, '//div[@class="iD3Ij"]').text
            print("\n my uploaded speed is:", text2, "mbps")
            time.sleep(3)

            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_007.pass.png")
            driver.close()
            assert True

        except:
            print("\n**********SOORY, SOME ERROR OCCURED***********") ;
            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_007.fail.png")
            assert False


