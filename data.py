from selenium.webdriver.common.by import By


class Data:
    urls = {
        "Veterans_Page": "https://rt-ed.co.il/articles/soldiers-trust-courses/",
        "Articles": "https://rt-ed.co.il/articles/archive/",
        "About": "https://rt-ed.co.il/internal/about/",
        "Contact_Us": "https://rt-ed.co.il/internal/contact-us/",
        "Maslulim_Automation_Course": "https://rt-ed.co.il/program/automation/",
        "Maslulim_QA_Course": "https://rt-ed.co.il/program/qa-automation/",
        "Maslulim_FullStack_Bootcamp_Course": "https://rt-ed.co.il/program/full-stack-bootcamp/",
        "Maslulim_FullStack_Course": "https://rt-ed.co.il/program/full-stack/",
        "Maslulim_Cyber_Course": "https://rt-ed.co.il/program/cyber-course/",
        "Maslulim_DevOps_Course": "https://rt-ed.co.il/program/devops/",
        "Maslulim_Data_Science_Course": "https://rt-ed.co.il/program/data-science/",
        "Maslulim_Data_Analyst_Course": "https://rt-ed.co.il/program/%d7%a7%d7%95%d7%a8%d7%a1-%d7%93%d7%90%d7%98%d7%94-%d7%90%d7%a0%d7%9c%d7%99%d7%a1%d7%98/",
        "Maslulim_Machine_Learning_Course": "https://rt-ed.co.il/program/machine-learning/",
        "Maslulim_Image_Processing_Course": "https://rt-ed.co.il/program/image-processing/",
        "Maslulim_IT_Course": "https://rt-ed.co.il/program/courses-%d7%a7%d7%95%d7%a8%d7%a1-%d7%a0%d7%99%d7%94%d7%95%d7%9c-%d7%a9%d7%a8%d7%aa%d7%99-%d7%9c%d7%99%d7%a0%d7%95%d7%a7%d7%a1/",
        "Maslulim_Real_Time_Bootcamp_Course": "https://rt-ed.co.il/program/rt-bootcamp/",
        "Maslulim_Embedded_Systems_Course": "https://rt-ed.co.il/program/rt-embedded/",
        "Maslulim_Real_Time_Embedded_Linux_Course": "https://rt-ed.co.il/program/real-time-embeded/",
        "Maslulim_Embedded_Linux_Course": "https://rt-ed.co.il/program/real-time-embedded-experienced/",
        "Selenium_Course": "https://rt-ed.co.il/courses/selenium-web/",
        "Java_Course": "https://rt-ed.co.il/courses/java-course/",
        "Python_Course": "https://rt-ed.co.il/courses/python-course/",
        "Networking_Course": "https://rt-ed.co.il/courses/networking-%d7%a7%d7%95%d7%a8%d7%a1/",
        "Docker_Course": "https://rt-ed.co.il/courses/docker/",
        "ML_Fundamentals": "https://rt-ed.co.il/courses/%d7%a7%d7%95%d7%a8%d7%a1-machine-learning-fundamentals/",
        "Cuda_Course": "https://rt-ed.co.il/courses/%d7%a7%d7%95%d7%a8%d7%a1-cuda/",
        "RT_Concepts": "https://rt-ed.co.il/courses/rt-concepts-%d7%a7%d7%95%d7%a8%d7%a1/",
        "Linux_Fundamentals": "https://rt-ed.co.il/courses/linux-basic-2/"}

    urls_landing_page = {"FullStack": "https://rt-ed.tech/full-stack-developer-22/",
                         "QA_and_Automation": "https://rt-ed.tech/%D7%A7%D7%95%D7%A8%D7%A1-%D7%91%D7%93%D7%99%D7%A7%D7%95%D7%AA-%D7%AA%D7%95%D7%9B%D7%A0%D7%94-qa/",
                         "Real_Time_Embedded_Linux": "https://rt-ed.tech/lp-real-time-embedded-linux/",
                         "Machine_Learning": "https://rt-ed.tech/machine-learning/",
                         "FullStack_Bootcamp": "https://rt-ed.tech/full-stack-bootcamp-22/",
                         "DevOps": "https://rt-ed.tech/devops-specialist_lp/",
                         "Real_Time_Embedded_Linux_Bootcamp": "https://rt-ed.tech/real-time-embedded-linux-bootcamp/",
                         "Cyber_Security": "https://rt-ed.tech/new-cyber/"}

    string = {"Last_Name": "tester",
              "First_Name": "tester",
              "Email": "official.rtg.tester@gmail.com",
              "Phone": "0547717136",
              "Thank You Title Page": "תודה » מכללת הייטק | לימודי תכנות וקורסים מקצועיים להייטק - מכללת RTG",
              "Thank You URL Page Landing Site": "https://rt-ed.tech/thanks/",
              "Thank You URL Page Landing Site QA": "https://rt-ed.tech/thanks-qa/",
              "Thank You URL Page Landing Site FSBT": "https://rt-ed.tech/thanks-fsbootcamp/",
              "Thank You URL Page Landing Site DV": "https://rt-ed.tech/thanks-devops/",
              "Thank You Title Page Landing Site QA": "עמוד תודה -QA - rt-ed.tech",
              "Thank You Title Page Landing Site RT_EL": "Real Time Embedded Linux - rt-ed.tech",
              "Thank You Title Page Landing Site ML": "Machine Learning_LP - rt-ed.tech",
              "Thank You Title Page Landing Site FSBT": "עמוד תודה - FSBootCamp - rt-ed.tech",
              "Thank You Title Page Landing Site DV": "עמוד תודה - devops - rt-ed.tech",
              "Thank You Title Page Landing Site RT_EL_BT": "Real Time Embedded Linux Bootcamp - rt-ed.tech",
              "Thank You Title Page Landing Site Cyber": "New Cyber - rt-ed.tech"}

    locators_main_page = {
        "Last_Name": (By.XPATH, "//*[@id='floating-lead-form2'] //descendant::input[@placeholder='שם משפחה']"),
        "First_Name": (By.XPATH, "//*[@id='floating-lead-form2'] //descendant::input[@placeholder='שם פרטי']"),
        "Email": (By.XPATH, "//*[@id='floating-lead-form2'] //descendant::input[@placeholder='אימייל']"),
        "Phone": (By.XPATH, "//*[@id='floating-lead-form2'] //descendant::input[@placeholder='טלפון']"),
        "Choose_Maslul": (By.XPATH, "//*[@id='floating-lead-form2'] //descendant::select[@id='target-track']"),
        "RT_Maslul": (By.XPATH, "//*[@id='floating-lead-form2'] //descendant::option[@value='RT']"),
        "Terms_Of_Services": (By.XPATH, "//*[@id='floating-lead-form2'] //descendant::input[@type='checkbox']"),
        "Send_Button": (By.XPATH, "//*[@id='floating-lead-form2'] //descendant::button[@name='submit']")}

    xpaths_main_page = {"Last_Name": "//*[@id='floating-lead-form2'] //descendant::input[@placeholder='שם משפחה']",
                        "First_Name": "//*[@id='floating-lead-form2'] //descendant::input[@placeholder='שם פרטי']",
                        "Email": "//*[@id='floating-lead-form2'] //descendant::input[@placeholder='אימייל']",
                        "Phone": "//*[@id='floating-lead-form2'] //descendant::input[@placeholder='טלפון']",
                        "Choose_Maslul": "//*[@id='floating-lead-form2'] //descendant::select[@id='target-track']",
                        "RT_Maslul": "//*[@id='floating-lead-form2'] //descendant::option[@value='RT']",
                        "Terms_Of_Services": "//*[@id='floating-lead-form2'] //descendant::input[@type='checkbox']",
                        "Send_Button": "//*[@id='floating-lead-form2'] //descendant::button[@name='submit']"}

    xpaths_landing_page = {"Full_Name": "//*[@id='form-field-name']",
                           "Phone": "//*[@id='form-field-number']",
                           "Email": "//*[@id='form-field-myEmail']",
                           "Background": "//select[@id='form-field-select']",
                           "No_Background": "//select[@id='form-field-select'] //option[contains(text(), 'אין לי ידע בכלל')]",
                           "Terms_Of_Services_FS_QA_FSBT_DO": "//*[@id='form-field-terms']",
                           "Terms_Of_Services_RT_ML_RTBT": "//*[@id='form-field-terms-0']",
                           "Terms_Of_Services_Cyber": "//*[@data-id='a2374ca'] //*[@id='form-field-terms-0']",
                           "Send_Button_FS_FSBT": "//*[@id='dx']",
                           "Send_Button_QA": "//*[@id='dx']",
                           "Send_Button_RT_RTBT": "//*[@id='rt1'] //*[@id='dx']",
                           "Send_Button_ML": "//*[@id='ml1'] //*[@id='dx']",
                           "Send_Button_DV": "//*[@id='devops1'] //*[@id='dx']",
                           "Send_Button_Cyber": "//*[@id='cy1'] //*[@id='dx']"}
