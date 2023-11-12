from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    presunto = Ingredient("presunto")
    farinha = Ingredient("farinha")

    assert presunto.name == "presunto"
    assert presunto.restrictions == {"ANIMAL_DERIVED", "ANIMAL_MEAT"}
    assert presunto.__repr__() != "presunto"
    assert presunto.__repr__() == "Ingredient(presunto)"
    assert presunto != farinha
