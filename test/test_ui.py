import pytest
import allure
from SearchPage import SearchPage


@pytest.mark.ui
@allure.story("Aviasales UI")
@allure.title("Поиск по полному названию города")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_full_city_name(browser_edge):
    page = SearchPage(browser_edge)
    search_query = "Токио"
    with allure.step("Открытие страницы"):
        page.open()
    with allure.step(f"Ввод названия города '{search_query}'"):
        page.enter_search_query(search_query)
    with allure.step("Проверка релевантных подсказок и выбор города"):
        items = page.get_dropdown_items_text()
        assert len(items) > 0, "Выпадающий список пуст"
        page.select_dropdown_item_by_text(search_query)
    with allure.step("Проверка, что город корректно заполнился в поле"):
        assert search_query.lower() in page.get_input_value().lower()


@pytest.mark.ui
@allure.story("Aviasales UI")
@allure.title("Поиск по полному названию города на латинице")
@allure.severity(allure.severity_level.CRITICAL)
def test_full_city_name_lat(browser_ff):
    page = SearchPage(browser_ff)
    with allure.step("Открытие страницы"):
        page.open()
    with allure.step("Ввод названия города 'Irkutsk'"):
        page.enter_search_query("irkutsk")
    with allure.step("Выбор аэропорта 'Иркутск' из подсказок"):
        page.select_dropdown_item_by_text("Иркутск")
    with allure.step("Проверка, что поле заполнено корректно"):
        assert "Иркутск" in page.get_input_value()


@pytest.mark.ui
@allure.story("Aviasales UI")
@allure.title("Поиск по IATA коду аэропорта")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_iata_code(browser):
    page = SearchPage(browser)
    with allure.step("Открытие страницы"):
        page.open()
    with allure.step("Ввод IATA кода 'SVX'"):
        page.enter_search_query("SVX")
    with allure.step("Выбор аэропорта 'Екатеринбург' из подсказок"):
        page.select_dropdown_item_by_text("Екатеринбург")
    with allure.step("Проверка, что поле заполнено корректно"):
        assert "Екатеринбург" in page.get_input_value()


@pytest.mark.ui
@allure.story("Aviasales UI")
@allure.title("Поиск по названию страны")
@allure.severity(allure.severity_level.NORMAL)
def test_search_country_name(browser):
    page = SearchPage(browser)
    with allure.step("Открытие страницы"):
        page.open()
    with allure.step("Ввод названия страны 'Германия'"):
        page.enter_search_query("Германия")
    with allure.step("Выбор конкретного аэропорта из списка"):
        page.select_dropdown_item_by_text("Берлин")
    with allure.step("Проверка, что выбран нужный город/аэропорт"):
        assert "Берлин" in page.get_input_value()


@pytest.mark.ui
@allure.story("Aviasales UI")
@allure.title("Ввод части названия города")
@allure.severity(allure.severity_level.NORMAL)
def test_search_partial_country_name(browser):
    page = SearchPage(browser)
    search_query = "Стокгольм"
    with allure.step("Открытие страницы"):
        page.open()
    with allure.step(f"Ввод названия города '{search_query}'"):
        page.enter_search_query(search_query[:4])
    with allure.step("Проверка релевантных подсказок и выбор города"):
        items = page.get_dropdown_items_text()
        assert len(items) > 0, "Выпадающий список пуст"
        page.select_dropdown_item_by_text(search_query)
    with allure.step("Проверка, что город корректно заполнился в поле"):
        assert search_query.lower() in page.get_input_value().lower()


@pytest.mark.ui
@allure.story("Aviasales UI")
@allure.title("Ввод несуществующего названия")
@allure.severity(allure.severity_level.NORMAL)
def test_search_invalid_name(browser):
    page = SearchPage(browser)
    with allure.step("Открытие страницы"):
        page.open()
    with allure.step("Ввод несуществующего значения 'Tro-lo-lo'"):
        page.enter_search_query("Tro-lo-lo")
    with allure.step("Проверка отображения сообщения 'Ничего не найдено'"):
        items = page.get_dropdown_items_text()
        empty_msg = page.get_empty_result_message()
        # Проверяем, что либо список пуст, либо появилось сообщение об ошибке
        assert len(items) == 0 or empty_msg != "", "ошибка"
