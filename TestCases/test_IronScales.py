# ------------------------------------------------------------------------------------------------
# -- coding                                   | utf-8
# -- Author                                   | Sergei Chernyahovsky
# -- Site                                     | http://sergeicher.pro/
# -- Favorite Quote                           | “Always code as if the guy who ends up
#                                               maintaining your code will be a violent
#                                                    psychopath who knows where you live”
# -- Language                                 | Python
# -- WebDriver                                | Selenium
# -- Description                              | QA automation Junior position test - Python
# ------------------------------------------------------------------------------------------------
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from TestCases import conftest


@pytest.mark.usefixtures("InitWebDriver")
class Test_IronScales:

    def test_Case1(self):
        conftest.action.move_to_element(conftest.driver.find_element(By.XPATH, "//span[text()='Solution']")).perform()
        conftest.action.move_to_element(conftest.driver.find_element(By.XPATH, "//ul/li/a[text()='By Plan']")).perform()
        links = conftest.driver.find_elements(By.XPATH, "//*[@id='navbar_global']/div/ul[1]/li[1]/ul/li[2]/ul/li")
        expected = ["Starter™", "Email Protect™", "Complete Protect™"]
        actual = []
        for i in links:
            actual.append(i.text)
        assert actual == expected, "The links don't match"

    def test_Case2(self):
        conftest.action.move_to_element(conftest.driver.find_element(By.XPATH, "//span[text()='Company']")).perform()
        conftest.driver.find_element(By.XPATH, "//a[text()='Careers']").click()
        job_openings = conftest.driver.find_element(By.XPATH, "//a[text()='Job Openings']")
        conftest.action.move_to_element(job_openings).perform()
        job_openings.click()
        conftest.driver.find_element(By.XPATH, "//h3/a[text()='QA Automation Engineer']").click()

        year_experience = conftest.driver.find_element(By.XPATH,
                                                       "//*[@id='opportunityDetailView']/div[2]/div/div/div/div["
                                                       "2]/div[1]/div[3]/p/ul[2]/li[2]").text

        string = ""
        for i in year_experience:
            if i.isdigit():
                string += i

        assert int(string) > 1, "The number is less or equal to 1"

    def test_Case3(self):

        conftest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        conftest.driver.execute_script("window.scrollTo(0, 400);")

        expected = "LinkedIn In1_layer,YouTube2_layer,Twitter3_layer,Facebook F4_layer,Instagram5_layer"

        social_links = conftest.driver.find_elements(By.XPATH, "//a[@class='no-decoration']/i/*[name()='svg']/*[name("
                                                               ")='g']")

        string = ""
        for i in social_links:
            string += i.get_attribute("id") + ","

        assert string[:-1] == expected, "The elements don't match: "

