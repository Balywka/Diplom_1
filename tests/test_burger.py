import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Burger


def test_init_empty(): #для сборки нового бургера
    burger = Burger()
    assert burger.bun is None
    assert burger.ingredients == []


def test_set_buns(): #метод set_buns() корректно устанавливает ссылку на объект Bun
    burger = Burger()
    bun = Bun("black bun", 100)
    burger.set_buns(bun)
    assert burger.bun is bun


def test_add_ingredient(): #Проверить добавление одного ингредиента в список
    burger = Burger()
    ing = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
    burger.add_ingredient(ing)
    assert len(burger.ingredients) == 1 #длина списка увеличилась
    assert burger.ingredients[0] is ing #объект сохранён по ссылке


def test_remove_ingredient(): # корректное удаление ингредиента по индексу
    burger = Burger()
    sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
    filling = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)
    burger.remove_ingredient(0)
    assert burger.ingredients == [filling]



def test_move_ingredient(): #логику перемещения слоя
    burger = Burger()
    sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
    filling = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)
    burger.move_ingredient(0, 1)
    assert burger.ingredients == [filling, sauce]



@pytest.mark.parametrize("bun_price,ing_prices,expected", [ #расчёт стоимости 5 сценариев в 1 тесте
    (100, [], 200),
    (100, [50], 250),
    (200, [10, 20], 430),
    (0, [1], 1),
    (500, [0, 0], 1000),
])
def test_get_price(bun_price, ing_prices, expected):
    burger = Burger()
    bun = Bun("test", bun_price)
    burger.set_buns(bun)
    for p in ing_prices:
        burger.add_ingredient(Ingredient("x", "x", p))
    assert burger.get_price() == expected


def test_get_price_no_bun_raises(): #вызов get_price() без предварительного set_buns()
    burger = Burger()
    with pytest.raises(AttributeError) as exc_info:
        burger.get_price()
    assert "'NoneType' object has no attribute 'get_price'" in str(exc_info.value)


def test_get_receipt(): #формат финального чека
    burger = Burger()
    bun = Bun("black bun", 100)
    sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
    filling = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
    burger.set_buns(bun)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)

    receipt = burger.get_receipt()
    lines = receipt.strip().split('\n')
    assert lines[0] == "(==== black bun ====)"
    assert lines[1] == "= sauce hot sauce ="
    assert lines[2] == "= filling cutlet ="
    assert lines[3] == "(==== black bun ====)"
    assert lines[5] == "Price: 400"


def test_get_receipt_no_ingredients(): # бургер только из булок
    burger = Burger()
    bun = Bun("red bun", 300)
    burger.set_buns(bun)
    receipt = burger.get_receipt()
    lines = receipt.strip().split('\n')
    assert lines[0] == "(==== red bun ====)"
    assert lines[1] == "(==== red bun ====)"
    assert lines[3] == "Price: 600"


def test_get_price_with_mocks(): #Демонстрация использования моков
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_price.return_value = 100
    mock_ing1 = Mock()
    mock_ing1.get_price.return_value = 30
    mock_ing2 = Mock()
    mock_ing2.get_price.return_value = 70

    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ing1)
    burger.add_ingredient(mock_ing2)

    price = burger.get_price()
    assert price == 300  # 2*100 + 30 + 70
    assert mock_bun.get_price.call_count == 1
    assert mock_ing1.get_price.call_count == 1
    assert mock_ing2.get_price.call_count == 1