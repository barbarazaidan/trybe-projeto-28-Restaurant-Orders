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
        # print(self.data)
        # conjunto vazio para armazenar os pratos
        self.dishes = self.format_dishes()

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
        dishes_list = {}

        # print(self.data)
        # print(dishes_list)

        for dish, price, ingredient, recipe_amount in self.data:
            # cria um prato com os dados da linha
            new_dish = Dish(dish, float(price))
            component = Ingredient(ingredient)

            if dish not in dishes_list:
                # cria uma chave com o nome do prato e o valor é o prato
                dishes_list[dish] = new_dish

            # adiciona o ingrediente ao conjunto de ingredientes do prato
            dishes_list[dish].add_ingredient_dependency(
                component, int(recipe_amount)
            )

        # print(dishes_list)
        # retorna um conjunto de pratos com apenas os valores das chaves
        return set(dishes_list.values())


# menu_instance = MenuData("tests/mocks/menu_base_data.csv")

# exemplo do que está em self.data:
# [['lasanha presunto', '25.90', 'queijo mussarela', '15'],
# ['lasanha presunto', '25.90', 'presunto', '15']]

# exemplo do que está em dishes_list:
# {'lasanha presunto': Dish('lasanha presunto', R$25.90),
# 'lasanha berinjela': Dish('lasanha berinjela', R$27.00)}
