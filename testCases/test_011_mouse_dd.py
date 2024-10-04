import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Test_011_DropDown():
    def test_011_Drop_down(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://vinothqaacademy.com/mouse-event/")
        time.sleep(3)

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_011_before_dd.pass.png")
        time.sleep(3)

        action = ActionChains(driver)

        drag = driver.find_element(By.XPATH,'//div[@id="draggableElement"]')
        drop = driver.find_element(By.XPATH,'//div[@id="droppableElement"]')

        action.drag_and_drop(drag,drop).perform()
        time.sleep(3)

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\Revision2\\Sreenshot\\test_011_after_dd.pass.png")

        driver.close()

