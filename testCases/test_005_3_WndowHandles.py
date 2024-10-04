# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# class Test_005_MultipleWindow():
#     def test_005_Multiple_window(self):
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(10)
#         driver.maximize_window()
#         driver.get("https://demo.automationtesting.in/Windows.html")
#         time.sleep(3)
#
#         driver.find_element(By.XPATH,'(//button[@class="btn btn-info"])[1]').click()
#         time.sleep(3)
#
#         all_window = driver.window_handles
#         driver.switch_to.window(all_window[1])
#
#         print("\n******* HANDLING CHILD WINDOW 1 **********")
#
#         title1 = driver.title
#         print("\nprinting title of child window1:",title1)
#
#         driver.switch_to.window(all_window[0])
#         print("\n ****** BACK TO PARENT WINDOW***********")
#         title0 = driver.title
#         print("parent window title:",title0)
#
#         driver.find_element(By.XPATH,'(//button[@class="btn btn-info"])[1]').click()
#         time.sleep(3)
#         driver.switch_to.window(all_window[1])
#         print("\n ******** HANDLING CHILD WINDOW 2************")
#         title2 = driver.title
#         print("\nprinting title of child window1:",title2)
#
#         driver.switch_to.window(all_window[0])
#         print("\n ****** BACK TO PARENT WINDOW***********")
#         title0 = driver.title
#         print("parent window title:", title0)
#
#
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_005_Multiplewindow():

    def test_005_mul_windowhandles(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://demo.automationtesting.in/Windows.html")

        driver.find_element(By.XPATH,'(//a[@class="analystic"])[3]').click()
        time.sleep(1)

        parenttitle=driver.title
        print('\n******PARENT WINDOW TITLE*****')
        print(parenttitle)

        parenttext=driver.find_element(By.XPATH,'//p[contains(text(),"Click the button to open multiple windows")] ').text
        print('*******PARENT WINDOW TEXT********')
        print(parenttext)

        driver.find_element(By.XPATH,'//button[text()="click "]').click()

        all_window=driver.window_handles

        driver.switch_to.window(all_window[0])
        time.sleep(2)

        title0=driver.title
        print('\n*******TITLE OF ZEROTH WINDOW')
        print(title0)

        text0=driver.find_element(By.XPATH,'//h1[text()="Automation Demo Site "] ').text
        print('\n*******TEXT OF ZEROTH WINDOW******')
        print(text0)

        print('*****PERFORMING ACTION WITH FIRST WINDOW******')
        driver.switch_to.window(all_window[1])
        time.sleep(2)

        title1=driver.title
        print('********TITLE OF FIRST WINDOW*******')
        print(title1)

        text1=driver.find_element(By.XPATH,'//input[@id="email"]').text
        print('************TEXT OF FIRST WINDOW**********')
        print(text1)

        driver.switch_to.window(all_window[2])
        time.sleep(1)

        title2=driver.title
        print('******TITLE OF SECOND WINDOW********')
        print(title2)

        text2=driver.find_element(By.XPATH,'//div[@class="mx-auto text-center p-4"]').text
        print('**********TEXT OF SECOND WINDOW*******')
        print(text2)

        driver.switch_to.window(all_window[1])
        time.sleep(1)
        driver.close()

        driver.switch_to.window(all_window[0])
        time.sleep(1)
        driver.close()
