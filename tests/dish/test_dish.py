import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction  # noqa: F401, E261, E501


# Req 2
def test_dish():
    salmao = Ingredient("salmão")
    farinha = Ingredient("farinha")
    mussarela = Ingredient("queijo mussarela")

    dish1 = Dish("Pizza", 45.0)
    dish2 = Dish("Sanduiche", 27.0)

    restritions_pizza = {
        Restriction.GLUTEN,
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
    }

    assert dish1.name == "Pizza"
    assert dish1.price == 45.0
    assert dish1.__hash__() != dish2.__hash__()
    assert dish1.__hash__() == dish1.__hash__()
    assert dish1.__eq__(dish2) is False
    assert dish1.__eq__(dish1) is True
    assert dish1.__repr__() == "Dish('Pizza', R$45.00)"
    with pytest.raises(ValueError):
        Dish("Dish price must be greater then zero.", -30)
    with pytest.raises(TypeError):
        Dish("Dish price must be float.", "30")

    dish1.add_ingredient_dependency(salmao, 50)
    dish1.add_ingredient_dependency(farinha, 200)
    dish1.add_ingredient_dependency(mussarela, 150)
    assert dish1.recipe.get(mussarela) == 150
    assert dish1.get_restrictions() == restritions_pizza
    assert dish1.get_ingredients() == {salmao, farinha, mussarela}
