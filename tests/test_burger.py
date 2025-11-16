import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from Diplom_1.data import BunData


class TestBurger:
    def test_init_empty(self, empty_burger): #для сборки нового бургера
        assert empty_burger.bun is None
        assert empty_burger.ingredients == []

    def test_set_buns(self, empty_burger, default_bun):
        empty_burger.set_buns(default_bun)
        assert empty_burger.bun is default_bun


    def test_add_ingredient(self, empty_burger, default_filling): #Проверить добавление одного ингредиента в список
        empty_burger.add_ingredient(default_filling)
        assert len(empty_burger.ingredients) == 1 #длина списка увеличилась
        assert empty_burger.ingredients[0] is default_filling #объект сохранён по ссылке


    def test_remove_ingredient(self, empty_burger, hot_sauce, dinosaur_filling): # корректное удаление ингредиента по индексу
        empty_burger.add_ingredient(hot_sauce)
        empty_burger.add_ingredient(dinosaur_filling)
        empty_burger.remove_ingredient(0)
        assert empty_burger.ingredients == [dinosaur_filling]


    def test_move_ingredient(self,empty_burger, sour_cream_sauce, cutlet_filling): #логику перемещения слоя
        empty_burger.add_ingredient(sour_cream_sauce)
        empty_burger.add_ingredient(cutlet_filling)
        empty_burger.move_ingredient(0, 1)
        assert empty_burger.ingredients == [cutlet_filling, sour_cream_sauce]



    @pytest.mark.parametrize("bun_price,ing_prices,expected", [ #расчёт стоимости 5 сценариев в 1 тесте
        (100, [], 200),
        (100, [50], 250),
        (200, [10, 20], 430),
        (0, [1], 1),
        (500, [0, 0], 1000),
    ])
    def test_get_price(self, empty_burger, bun_price, ing_prices, expected):
        bun = Bun(BunData.TEST_BUN_NAME, bun_price)
        empty_burger.set_buns(bun)
        for price in ing_prices:
            empty_burger.add_ingredient(Ingredient("x", "x", price))
        assert empty_burger.get_price() == expected


    def test_get_price_no_bun_raises(self, empty_burger): #вызов get_price() без предварительного set_buns()
        with pytest.raises(AttributeError) as exc_info:
            empty_burger.get_price()
        assert "'NoneType' object has no attribute 'get_price'" in str(exc_info.value)


    def test_get_receipt(self, empty_burger, default_bun, default_sauce, default_filling): #формат финального чека
        empty_burger.set_buns(default_bun)
        empty_burger.add_ingredient(default_sauce)
        empty_burger.add_ingredient(default_filling)
        receipt = empty_burger.get_receipt()
        lines = receipt.strip().split('\n')
        assert lines[0] == "(==== black bun ====)"
        assert lines[1] == "= sauce hot sauce ="
        assert lines[2] == "= filling cutlet ="
        assert lines[3] == "(==== black bun ====)"
        assert lines[5] == "Price: 400"


    def test_get_receipt_no_ingredients(self, empty_burger, default_bun): # бургер только из булок
        empty_burger.set_buns(default_bun)
        receipt = empty_burger.get_receipt()
        lines = receipt.strip().split('\n')
        assert lines[0] == "(==== black bun ====)"
        assert lines[1] == "(==== black bun ====)"
        assert lines[3] == "Price: 200"


    def test_get_price_with_mocks(self, empty_burger, mock_bun, mock_ingredient):
        # Демонстрация использования моков для расчета стоимости
        empty_burger.set_buns(mock_bun)
        empty_burger.add_ingredient(mock_ingredient)
        empty_burger.add_ingredient(mock_ingredient)
        price = empty_burger.get_price()
        assert price == 300  # 2*100 + 50 + 50
        assert mock_bun.get_price.call_count == 1
        assert mock_ingredient.get_price.call_count == 2