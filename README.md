# Final_projekt

## Автоматизация тестирования функционала поиска билетов на платформе Aviasales с помощью Python

Репозиторий содержит автоматизированные тесты для проверки веб-интерфейсов и API.
Проект построен на базе языка Python с использованием фреймворка Pytest и паттерна проектирования PageObjectModel (POM) для UI-тестов.
Отчетность по результатам тестирования генерируется с помощью Allure.

Финальный проект по ручному тестированию: [https://tens.yonote.ru/share/fbde4c74-c123-40c7-928f-3a5ff626c58a#h-api-test-kejsy]

### Шаги
1. Склонировать проект и перейти в папку проекта:
   '''git clone https://github.com/TensRussia/Final_projekt.git'''
   '''cd <название_папки>'''

2. Создать и активировать виртуальное окружение:
   Windows:
      '''python -m venv venv'''
      '''venv\Scripts\activate'''

   macOS / Linux:
      '''python3 -m venv venv'''
      '''source venv/bin/activate'''

3. Установить зависимости
   Для установки зависимостей проекта выполнить команду:
   '''pip install -r requirements.txt'''

4. Запустить тесты 'pytest'
   В проекте настроены маркеры для раздельного запуска различных видов тестирования.
   Убедитесь, что вы находитесь в корневой директории проекта перед запуском.

   Запуск только UI-тестов:
      '''pytest -m "ui"'''
   Запуск только API-тестов:
      '''pytest -m "api"'''
   Запуск всех тестов проекта:
      '''pytest'''

5. Сгенерировать отчет
   Для формирования наглядного отчета о прохождении тестов выполнить следующие шаги:

   Запустить тесты с флагом сохранения результатов:
      '''pytest --alluredir=allure-results'''

6. Открыть отчет
   Сгенерировать и открыть отчет в браузере:
      '''allure serve allure-results'''

### Библиотеки (!)
- pyp install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests

### Стек:
- pytest
- selenium
- requests
- allure
- config

### Структура:
- ./test - папка стестами;
- README.md - документация проекта;
- requirements.txt - список зависимостей.

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)