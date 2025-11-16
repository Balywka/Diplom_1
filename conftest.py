import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from Diplom_1.data import TestData, BunData, SauceData, FillingData


@pytest.fixture
def empty_burger(): # Фикстура для пустого бургера
    return Burger()


@pytest.fixture
def default_bun(): # Фикстура для стандартной булки
    return Bun(TestData.DEFAULT_BUN_NAME, TestData.DEFAULT_BUN_PRICE)


@pytest.fixture
def default_sauce(): # Фикстура для стандартного соуса
    return Ingredient(TestData.DEFAULT_SAUCE_TYPE, TestData.DEFAULT_SAUCE_NAME, TestData.DEFAULT_SAUCE_PRICE)


@pytest.fixture
def default_filling(): # Фикстура для стандартной начинки
    return Ingredient(TestData.DEFAULT_FILLING_TYPE, TestData.DEFAULT_FILLING_NAME, TestData.DEFAULT_FILLING_PRICE)


@pytest.fixture
def hot_sauce(): # Фикстура для острого соуса
    return Ingredient(SauceData.HOT_SAUCE_TYPE, SauceData.HOT_SAUCE_NAME, SauceData.HOT_SAUCE_PRICE)


@pytest.fixture
def dinosaur_filling(): # Фикстура для начинки 'динозавр'
    return Ingredient(FillingData.DINOSAUR_TYPE, FillingData.DINOSAUR_NAME, FillingData.DINOSAUR_PRICE)


@pytest.fixture
def sour_cream_sauce(): # Фикстура для соуса 'сметана'
    return Ingredient(SauceData.SOUR_CREAM_TYPE, SauceData.SOUR_CREAM_NAME, SauceData.SOUR_CREAM_PRICE)


@pytest.fixture
def cutlet_filling(): # Фикстура для начинки 'котлета'
    return Ingredient(FillingData.CUTLET_TYPE, FillingData.CUTLET_NAME, FillingData.CUTLET_PRICE)


@pytest.fixture
def mock_bun(): # Фикстура для мока булки
    mock_bun = Mock()
    mock_bun.get_price.return_value = 100
    return mock_bun


@pytest.fixture
def mock_ingredient(): # Фикстура для мока ингредиента
    mock_ing = Mock()
    mock_ing.get_price.return_value = 50
    return mock_ing