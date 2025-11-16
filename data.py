from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# Данные для булок
class BunData:
    BLACK_BUN_NAME = "black bun"
    BLACK_BUN_PRICE = 100
    WHITE_BUN_NAME = "white bun"
    WHITE_BUN_PRICE = 200
    RED_BUN_NAME = "red bun"
    RED_BUN_PRICE = 300
    TEST_BUN_NAME = "test bun"
    TEST_BUN_PRICE = 50


# Данные для соусов
class SauceData:
    HOT_SAUCE_NAME = "hot sauce"
    HOT_SAUCE_PRICE = 50
    HOT_SAUCE_TYPE = INGREDIENT_TYPE_SAUCE

    SOUR_CREAM_NAME = "sour cream"
    SOUR_CREAM_PRICE = 200
    SOUR_CREAM_TYPE = INGREDIENT_TYPE_SAUCE

    CHILI_SAUCE_NAME = "chili sauce"
    CHILI_SAUCE_PRICE = 300
    CHILI_SAUCE_TYPE = INGREDIENT_TYPE_SAUCE


# Данные для начинок
class FillingData:
    CUTLET_NAME = "cutlet"
    CUTLET_PRICE = 150
    CUTLET_TYPE = INGREDIENT_TYPE_FILLING

    DINOSAUR_NAME = "dinosaur"
    DINOSAUR_PRICE = 200
    DINOSAUR_TYPE = INGREDIENT_TYPE_FILLING

    SAUSAGE_NAME = "sausage"
    SAUSAGE_PRICE = 300
    SAUSAGE_TYPE = INGREDIENT_TYPE_FILLING


# Общие тестовые данные
class TestData:
    # данные для основных тестов
    DEFAULT_BUN_NAME = BunData.BLACK_BUN_NAME
    DEFAULT_BUN_PRICE = BunData.BLACK_BUN_PRICE
    DEFAULT_SAUCE_NAME = SauceData.HOT_SAUCE_NAME
    DEFAULT_SAUCE_PRICE = SauceData.HOT_SAUCE_PRICE
    DEFAULT_SAUCE_TYPE = SauceData.HOT_SAUCE_TYPE
    DEFAULT_FILLING_NAME = FillingData.CUTLET_NAME
    DEFAULT_FILLING_PRICE = FillingData.CUTLET_PRICE
    DEFAULT_FILLING_TYPE = FillingData.CUTLET_TYPE