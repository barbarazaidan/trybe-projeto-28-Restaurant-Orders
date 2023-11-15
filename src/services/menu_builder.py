from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        menu_list = []

        for dish in self.menu_data.dishes:
            if (
                restriction is None
                or restriction not in dish.get_restrictions()
            ):
                menu_list.append(
                    {
                        "dish_name": dish.name,
                        "ingredients": dish.get_ingredients(),
                        "price": dish.price,
                        "restrictions": dish.get_restrictions(),
                    }
                )

        return menu_list


# é necessário que o método retorne uma lista de dicionários
# que contenham as chaves dish_name, ingredients, price e restrictions
# o método get_main_menu retorna uma lista de dicionários
# com o cardápio completo quando não é passado nenhum parâmetro;
# e uma lista de dicionários com o cardápio correto
# respeitando a restrição alimentar passada como parâmetro;
