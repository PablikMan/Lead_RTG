import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from data import Data

driver = webdriver.Chrome("./src/chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

succeed = 0
failed = 0


def run(desired_url):
    try:
        driver.get(desired_url)
        time.sleep(3)
        driver.find_element(By.XPATH, Data.xpaths_main_page["Last_Name"]).send_keys(Data.string["Last_Name"])
        time.sleep(1)
        driver.find_element(By.XPATH, Data.xpaths_main_page["First_Name"]).send_keys(Data.string["First_Name"])
        time.sleep(1)
        driver.find_element(By.XPATH, Data.xpaths_main_page["Email"]).send_keys(Data.string["Email"])
        time.sleep(1)
        driver.find_element(By.XPATH, Data.xpaths_main_page["Phone"]).send_keys(Data.string["Phone"])
        time.sleep(1)
        driver.find_element(By.XPATH, Data.xpaths_main_page["Choose_Maslul"]).click()
        time.sleep(1)
        driver.find_element(By.XPATH, Data.xpaths_main_page["RT_Maslul"]).click()
        time.sleep(1)
        driver.find_element(By.XPATH, Data.xpaths_main_page["Terms_Of_Services"]).click()
        time.sleep(1)
        driver.find_element(By.XPATH, Data.xpaths_main_page["Send_Button"]).click()
        time.sleep(15)
    except Exception:
        print("No form has been found... :(", driver.title)
        return False

    if driver.title == Data.string["Thank You Title Page"]:
        print("Send Successfully!")
        return True

    print("Did not send... :(", driver.title)
    return False


def lead_page_fullstack(desired_url):
    driver.get(desired_url)
    time.sleep(3)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Full_Name"]).send_keys(Data.string["First_Name"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Phone"]).send_keys(Data.string["Phone"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Email"]).send_keys(Data.string["Email"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Send_Button_FS_FSBT"]).click()
    time.sleep(15)
    if driver.current_url == Data.string["Thank You URL Page Landing Site"]:
        print("Send Successfully!")
        return True
    print("Error\nExpected:", Data.string["Thank You URL Page Landing Site"], "\nGiven:", driver.current_url)
    return False


def lead_page_qa(desired_url):
    driver.get(desired_url)
    time.sleep(3)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Full_Name"]).send_keys(Data.string["First_Name"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Phone"]).send_keys(Data.string["Phone"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Email"]).send_keys(Data.string["Email"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Send_Button_QA"]).click()
    time.sleep(15)
    if driver.current_url == Data.string["Thank You URL Page Landing Site QA"]:
        print("Send Successfully!")
        return True
    print("Error\nExpected:", Data.string["Thank You URL Page Landing Site QA"], "\nGiven:", driver.current_url)
    return False


def lead_page_real_time_embedded_linux(desired_url):
    driver.get(desired_url)
    time.sleep(3)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Full_Name"]).send_keys(Data.string["First_Name"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Phone"]).send_keys(Data.string["Phone"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Email"]).send_keys(Data.string["Email"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Background"]).click()
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["No_Background"]).click()
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Terms_Of_Services_RT_ML_RTBT"]).click()
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Send_Button_RT_RTBT"]).click()
    time.sleep(15)
    try:
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        if driver.current_url == Data.string["Thank You URL Page Landing Site"]:
            print("Send Successfully!")
            driver.close()
            driver.switch_to.window(tabs[0])
            return True
        print("Error\nExpected:", Data.string["Thank You URL Page Landing Site"], "\nGiven:", driver.current_url)
        driver.close()
        driver.switch_to.window(tabs[0])
        return False
    except IndexError:
        print("Error\nCouldn't switch tabs")


def lead_page_machine_learning(desired_url):
    driver.get(desired_url)
    time.sleep(3)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Full_Name"]).send_keys(Data.string["First_Name"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Phone"]).send_keys(Data.string["Phone"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Email"]).send_keys(Data.string["Email"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Background"]).click()
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["No_Background"]).click()
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Terms_Of_Services_RT_ML_RTBT"]).click()
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Send_Button_ML"]).click()
    time.sleep(15)
    try:
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        if driver.current_url == Data.string["Thank You URL Page Landing Site"]:
            print("Send Successfully!")
            driver.close()
            driver.switch_to.window(tabs[0])
            return True
        print("Error\nExpected:", Data.string["Thank You URL Page Landing Site"], "\nGiven:", driver.current_url)
        driver.close()
        driver.switch_to.window(tabs[0])
        return False
    except IndexError:
        print("Error\nCouldn't switch tabs")


def lead_page_fullstack_bt(desired_url):
    driver.get(desired_url)
    time.sleep(3)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Full_Name"]).send_keys(Data.string["First_Name"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Phone"]).send_keys(Data.string["Phone"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Email"]).send_keys(Data.string["Email"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Send_Button_FS_FSBT"]).click()
    time.sleep(15)
    if driver.current_url == Data.string["Thank You URL Page Landing Site FSBT"]:
        print("Send Successfully!")
        return True
    print("Error\nExpected:", Data.string["Thank You URL Page Landing Site FSBT"], "\nGiven:", driver.current_url)
    return False


def lead_page_devops(desired_url):
    driver.get(desired_url)
    time.sleep(3)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Full_Name"]).send_keys(Data.string["First_Name"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Phone"]).send_keys(Data.string["Phone"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Email"]).send_keys(Data.string["Email"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Send_Button_DV"]).click()
    time.sleep(15)
    if driver.current_url == Data.string["Thank You URL Page Landing Site DV"]:
        print("Send Successfully!")
        return True
    print("Error\nExpected:", Data.string["Thank You URL Page Landing Site DV"], "\nGiven:", driver.current_url)
    return False


def lead_page_real_time_embedded_linux_bt(desired_url):
    driver.get(desired_url)
    time.sleep(3)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Full_Name"]).send_keys(Data.string["First_Name"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Phone"]).send_keys(Data.string["Phone"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Email"]).send_keys(Data.string["Email"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Background"]).click()
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["No_Background"]).click()
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Terms_Of_Services_RT_ML_RTBT"]).click()
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Send_Button_RT_RTBT"]).click()
    time.sleep(15)
    try:
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        if driver.current_url == Data.string["Thank You URL Page Landing Site"]:
            print("Send Successfully!")
            driver.close()
            driver.switch_to.window(tabs[0])
            return True
        print("Error\nExpected:", Data.string["Thank You URL Page Landing Site"], "\nGiven:", driver.current_url)
        driver.close()
        driver.switch_to.window(tabs[0])
        return False
    except IndexError:
        print("Error\nCouldn't switch tabs")


def lead_page_cyber_security(desired_url):
    driver.get(desired_url)
    time.sleep(3)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Full_Name"]).send_keys(Data.string["First_Name"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Phone"]).send_keys(Data.string["Phone"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Email"]).send_keys(Data.string["Email"])
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Background"]).click()
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["No_Background"]).click()
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Terms_Of_Services_Cyber"]).click()
    time.sleep(1)
    driver.find_element(By.XPATH, Data.xpaths_landing_page["Send_Button_Cyber"]).click()
    time.sleep(15)
    try:
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        if driver.current_url == Data.string["Thank You URL Page Landing Site"]:
            print("Send Successfully!")
            driver.close()
            driver.switch_to.window(tabs[0])
            return True
        print("Error\nExpected:", Data.string["Thank You URL Page Landing Site"], "\nGiven:", driver.current_url)
        driver.close()
        driver.switch_to.window(tabs[0])
        return False
    except IndexError:
        print("Error\nCouldn't switch tabs")


def write_file(s):
    file = open("./rotations.txt", "w")
    file.write(s)
    file.close()


if __name__ == '__main__':
    # for url in Data.urls.values():
    #     if run(url):
    #         succeed += 1
    #     else:
    #         failed += 1

    #
    # print("Succeed = ", succeed)
    # print("Failed = ", failed)
    # driver.quit()

    time.sleep(3)

    if lead_page_fullstack(Data.urls_landing_page["FullStack"]):
        succeed += 1
    else:
        failed += 1

    time.sleep(3)

    if lead_page_qa(Data.urls_landing_page["QA_and_Automation"]):
        succeed += 1
    else:
        failed += 1

    time.sleep(3)

    if lead_page_real_time_embedded_linux(Data.urls_landing_page["Real_Time_Embedded_Linux"]):
        succeed += 1
    else:
        failed += 1

    time.sleep(3)

    if lead_page_machine_learning(Data.urls_landing_page["Machine_Learning"]):
        succeed += 1
    else:
        failed += 1

    time.sleep(3)

    if lead_page_fullstack_bt(Data.urls_landing_page["FullStack_Bootcamp"]):
        succeed += 1
    else:
        failed += 1

    time.sleep(3)

    if lead_page_devops(Data.urls_landing_page["DevOps"]):
        succeed += 1
    else:
        failed += 1

    time.sleep(3)

    if lead_page_real_time_embedded_linux_bt(Data.urls_landing_page["Real_Time_Embedded_Linux_Bootcamp"]):
        succeed += 1
    else:
        failed += 1

    time.sleep(3)

    if lead_page_cyber_security(Data.urls_landing_page["Cyber_Security"]):
        succeed += 1
    else:
        failed += 1

    time.sleep(3)

    print("Succeed = ", succeed)
    print("Failed = ", failed)
    driver.quit()

    write_file(str(succeed))
