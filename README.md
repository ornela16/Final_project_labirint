# Final_project_labirint
Дипломная работа. Автоматизированные тесты проекта "Книжный интернет-магазин Лабиринт".

## Шаблон для автоматизации тестирования на python

### Шаги
1. Склонировать проект 'git clone https://github.com/имя_пользователя/
   pytest_ui_api_template.git'
2. Установить зависимости
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- selenium
- requests

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
-  test_config.ini - настройки для тестов


### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)

### Библиотеки (!)
- pyp install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest


[Лабиринт](https://www.labirint.ru)

Тестирование функционала интернет-магазина Лабиринт https://www.labirint.ru/

В папке pages находятся файлы, содержащие классы и методы для работы с сайтом.

Файлы автотестов:

    test_ui_labirint.py

1. test_go_in_new_user - тестирование авторизации нового пользователя по номеру телефона.

2. test_cart_counter - тестирование поиска книг на начальной странице сайта по ключевому слову, добавление найденных книг в корзину,
   проверка количества книг в корзине.

3. test_empty_search - тестирование поиска книг с пустым полем поиска.

4. test_hold_over - тестирование добавления книг в Отложенные, проверка количества отложенных книг. 

   