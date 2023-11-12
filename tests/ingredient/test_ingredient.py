from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    presunto = Ingredient("presunto")
    farinha = Ingredient("farinha")
    presunto2 = Ingredient("presunto")
    presunto_restrictions = {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    assert presunto.name == "presunto"
    assert presunto.restrictions == presunto_restrictions
    assert presunto.__repr__() != "presunto"
    assert presunto.__repr__() == "Ingredient('presunto')"
    assert presunto != farinha
    assert presunto.__hash__() != farinha.__hash__()
    assert presunto.__hash__() == presunto2.__hash__()
    assert presunto.__eq__(farinha) is False
    assert presunto.__eq__(presunto2) is True
