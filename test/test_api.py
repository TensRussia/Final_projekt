import allure
import pytest
import requests

base_url_api = "https://suggest.aviasales.com/v2/" + \
    "places.json?locale=ru_RU&max=100&&max=100&term="
base_url_api_end = "&types[]=city&types[]=airport&types[]=country"

MY_HEADERS = {"Content-Type": "application/json"}


@pytest.mark.api
@allure.story("Aviasales API")
@allure.title("Позитивный запрос: город/аэропорт отправления")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("city_input",
                         ["Ижевск",
                          "Vladivostok",
                          "SVX",
                          "ЛОФ"])
def test_city_input(city_input: str):
    with allure.step("Формирование GET запроса"):
        city_list = requests.get(
            f"{base_url_api} + '{city_input}' + {base_url_api_end}",
            headers=MY_HEADERS)
    with allure.step("Проверка статус-кода (ожидается 200)"):
        assert city_list.status_code == 200


@pytest.mark.api
@allure.story("Aviasales API")
@allure.title("Негативный запрос: город/аэропорт отправления")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("city_input_neg",
                         ["ИжевскИжевскИжевскИжевскИжевскИжевск",
                          "56789",
                          "**-//+/*",
                          ""])
def test_city_input_negativ(city_input_neg: str):
    with allure.step("Формирование GET запроса"):
        city_list = requests.get(
            f"{base_url_api} + '{city_input_neg}' + {base_url_api_end}",
            headers=MY_HEADERS)
    with allure.step("Проверка статус-кода (ожидается 200)"):
        assert city_list.status_code == 200


@pytest.mark.api
@allure.story("Aviasales API")
@allure.title("Негативный запрос: неверный метод запроса")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("city_input_no_get", "Ижевск")
def test_city_no_get(city_input_no_get: str):
    with allure.step("Формирование PUT запроса"):
        city_list = requests.put(
            f"{base_url_api} + '{city_input_no_get}' + {base_url_api_end}",
            headers=MY_HEADERS)
    with allure.step("Проверка статус-кода (ожидается 200)"):
        assert city_list.status_code == 200
