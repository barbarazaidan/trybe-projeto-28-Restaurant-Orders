# Req 3
import csv  # módulo para ler arquivos csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        # caminho do arquivo csv
        self.path = source_path
        # lê o arquivo csv e armazena em self.data
        self.data = self.read_csv()
        # conjunto vazio para armazenar os pratos
        self.dishes_list = self.format_dishes()
        print(self.dishes_list)

    def read_csv(self):
        with open(self.path) as csvfile:
            data = []
            reader_csvfile = csv.reader(csvfile)
            # pula a primeira linha do arquivo, que é o cabeçalho
            next(reader_csvfile)
            for row in reader_csvfile:
                data.append(row)
            return data

    def format_dishes(self):
        dishes = set()
        for dish, price, ingredient, recipe_amount in self.data:
            # cria um prato com os dados da linha
            new_dish = Dish(dish, price)
            component = Ingredient(ingredient)
            if new_dish in dishes:
                # se o prato já existe, adiciona o ingrediente ao prato
                new_dish.add_ingredient_dependency(component, recipe_amount)
            else:
                # adiciona o prato ao conjunto de pratos
                dishes.add(new_dish)
        return dishes


menu_instance = MenuData(
    "sd-030-a-restaurant-orders/tests/mocks/menu_base_data.csv"
)

# exemplo do que está em self.data:
# [['lasanha presunto', '25.90', 'queijo mussarela', '15'],
# ['lasanha presunto', '25.90', 'presunto', '15']]

# 22/06 - simone
# 50% das mensalidades restantes
#  def add_ingredient_dependency(self, ingredient: Ingredient, amount: int):
# self.recipe[ingredient] = amount
