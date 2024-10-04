'''program for Screenshot automatically showing  '''
import pyscreenshot
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_006_ImplicitWait():
    def test_006_implicit_wait(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://www.google.co.in/")
        time.sleep(3)
        driver.find_element(By.XPATH,'//textarea[@title="Search"]').send_keys("INTERNET SPEED TEST")
        time.sleep(3)

        driver.find_element(By.XPATH,'(//input[@value="Google Search"])[2]').click()
        time.sleep(3)

        driver.find_element(By.XPATH,'//div[text()="RUN SPEED TEST"]').click()
        time.sleep(45)

        print("\n ********** DOWNLOAD SPEED**********")
        text1 = driver.find_element(By.XPATH,'//div[@class="oyUhj"]').text
        print("\n my downloaded speed is:",text1,"mbps")
        time.sleep(3)

        print("\n ******** UPLOAD SPEED *************")
        text2 = driver.find_element(By.XPATH,'//div[@class="iD3Ij"]').text
        print("\n my uploaded speed is:",text2,"mbps")
        time.sleep(3)

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_006_02_pass.png")
        # image = pyautogui.screenshot()
        image=pyscreenshot.grab()

        image.show()
        image.save("test_006_02_pass.png")
        driver.close()
