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
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

driver = None
action = None


@pytest.fixture(scope="function")
def InitWebDriver(request):
    global driver
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver = globals()["driver"]
    driver.implicitly_wait(20)
    driver.get("https://ironscales.com/")
    globals()["action"] = ActionChains(driver)
    request.cls.driver = driver
    sleep(2)

    yield
    globals()["driver"].quit()
