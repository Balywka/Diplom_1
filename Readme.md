🌌 Stellar Burgers — Diplom_1  
Задание 1: Юнит-тесты для класса `Burger` https://stellarburgers.education-services.ru/

> ✅ 100% покрытие кода  
> ✅ Полная независимость тестов  
> ✅ Параметризация и моки  
> ✅ Соответствие бизнес-логике

Описание
Реализованы юнит-тесты для класса `Burger` из пакета `praktikum`, сборкf космического бургера в приложении *Stellar Burgers*

Класс `Burger` отвечает за:
- Установку булок (`set_buns`)
- Добавление/удаление/перемещение ингредиентов (`add_ingredient`, `remove_ingredient`, `move_ingredient`)
- Расчёт стоимости (`get_price`)
- Формирование чека (`get_receipt`)

Тесты покрывают все методы, включая обработку ошибок и соответствия формату UI.

Реализованные сценарии

| Тест | Покрытие | Особенности |
| `test_init_empty` | `__init__` | Проверка пустого состояния |
| `test_set_buns` | `set_buns` | Корректная установка булки |
| `test_add_ingredient` | `add_ingredient` | Добавление в список |
| `test_remove_ingredient` | `remove_ingredient` | Удаление по индексу |
| `test_move_ingredient` | `move_ingredient` | Перемещение (drag-and-drop логика) |
| `test_get_price` | `get_price` | *Параметризация*: 5 сценариев цен (`@pytest.mark.parametrize`) |
| `test_get_price_no_bun_raises` | `get_price` | `AttributeError` при отсутствии булки |
| `test_get_receipt` | `get_receipt` | Проверка формата чека с ингредиентами: `(==== bun ====)`, `= type name =`, `Price: N` |
| `test_get_receipt_no_ingredients` | `get_receipt` | Чек только из булок (без начинки) |
| `test_get_price_with_mocks` | `get_price` | *Демонстрация моков* (`unittest.mock.Mock`)


Запуск тестов

Установите зависимости:
   pip install -r requirements.txt