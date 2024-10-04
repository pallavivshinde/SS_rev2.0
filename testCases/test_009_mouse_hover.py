import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Test_009_Mouse_Hover():
    def test_009_MouseHover(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://stqatools.com/demo/MouseHover.php")
        time.sleep(3)
        mouse_hover = driver.find_element(By.XPATH,'//button[text()="Mouse Hover DropDown"]')
        action = ActionChains(driver)
        action.move_to_element(mouse_hover).perform()
        time.sleep(3)
        driver.find_element(By.XPATH,'//a[text()="Link 2"]').click()

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_009_MoueHover.pass.png")

        print("\n ********* PRINTING A TEXT AFTER MOUSE HOVER ***********")
        text1 = driver.find_element(By.XPATH,"(//div[normalize-space()='You click on Dropdown hover Option'])[2]").text
        print("\n ",text1)
        time.sleep(3)

        driver.close()
        assert True