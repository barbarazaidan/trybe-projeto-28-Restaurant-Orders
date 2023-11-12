from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    ingredient1 = Ingredient("salnão")
    ingredient2 = Ingredient("farinha")
    ingredient3 = Ingredient("queijo mussarela")
    ingredient4 = Ingredient("ovo")
    ingredient5 = Ingredient("bacon")

    dish1 = Dish("Pizza", 45.0)
    dish2 = Dish("Sanduiche", 27.0)

    assert dish1.name == "Pizza"
    assert dish1.price == 45.0
