import allure
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def browser():
    """Фикстура для инициализации веб-драйвера Chrome."""
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome()
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def browser_ff():
    """Фикстура для инициализации веб-драйвера FireFox."""
    with allure.step("Открыть и настроить браузер"):
        browser_ff = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()))
        browser_ff.implicitly_wait(4)
        browser_ff.maximize_window()
        yield browser_ff
    with allure.step("Закрыть браузер"):
        browser_ff.quit()


@pytest.fixture
def browser_edge():
    """Фикстура для инициализации веб-драйвера Edge."""
    with allure.step("Открыть и настроить браузер"):
        url = "https://msedgedriver.microsoft.com/LATEST_RELEASE"
        browser_edge = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager(
                url="https://msedgedriver.microsoft.com",
                latest_release_url=url).install())
        )
        browser_edge.implicitly_wait(3)
        browser_edge.maximize_window()
        yield browser_edge
    with allure.step("Закрыть браузер"):
        browser_edge.quit()
