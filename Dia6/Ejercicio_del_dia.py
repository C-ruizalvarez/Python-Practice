import os
from os import system
from pathlib import Path
from time import sleep

"""
1 - Saludo
2 - Indicar donde estan las recetas
3 - tienes [x] recetas

Elegir opciones

1 - leer receta -> elegir categoria -> mostrar recetas -> elegir receta -> leer receta
2 - crear recceta -> elegir categoria -> crear nombre -> ccrear contenido
3 - crear categoria -> nombre de categoria a crear
4 - eliminar receta -> elegir categoria -> mostrar recetas -> elegir receta -> eliminar receta
5 - eliminar categoria -> elegir categoria -> eliminar categoria
6 - finalizar programa

usar system('clear')
"""
def not_correct_option():
    clear_screen()
    print("=======================================")
    print("La opción que escogiste no es correcta")
    print("=======================================")
    wait_screen()

def continue_enter():
    input("Para continuar presione Enter....")

def clear_screen():
    system("clear")

def wait_screen():
    sleep(1.5)

def main_folder_location():
    return Path.home() / "Recetas"

def count_number_of_recipes(base_folder):

    counter = 0

    for file in Path(base_folder).glob("**/*.txt"):
        counter += 1

    return counter

def detect_categories():
    directories = []

    for directory in Path(main_folder_location()).glob("*"):
        directories.append(directory.stem)

    return directories

def choose_category_menu(categories, create_recepie = False):

    options = {}

    clear_screen()

    for index, directory in enumerate(categories):
        print(f"{index + 1} - {directory}")
        options[str(index + 1)] = directory

    if not create_recepie:
        option = input("Which category would you like to see?: ")
    else:
        option = input("Which category would you like to choose?: ")

    if option not in options.keys():
        not_correct_option()
        choose_category_menu(categories)
    else:
        return options[option]


def detect_recipes(category):
    recipes = []

    for file in Path(category).glob("*.txt"):
        recipes.append(file.stem)

    return recipes

def choose_recipes_menu(category):
    
    options = {}

    recipes = detect_recipes(category)

    clear_screen()

    for index, recipe in enumerate(recipes):
        print(f"{index + 1} - {recipe}")
        options[str(index + 1)] = recipe

    option = input("Que receta te gustaria ver?: ")

    if option not in options.keys():
        not_correct_option()
        choose_recipes_menu(category)
    else:
        return options[option]

def recipe_flow():
    category = choose_category_menu(detect_categories())
    recipe = choose_recipes_menu(main_folder_location() / category)

    recipe_path = Path(main_folder_location() / category / (recipe + ".txt"))

    return recipe_path

def read_recipe():

    recipe_path = recipe_flow()

    clear_screen()
    print(recipe_path.read_text())

    continue_enter()

    return None

def create_recipe():
    category = choose_category_menu(detect_categories())

    recipe_path = Path(main_folder_location() / category)

    clear_screen()

    recipe_name = input("Cual es el nombre de la receta?: ") + ".txt"

    recipe = open(recipe_path / recipe_name, "w")

    recipe_content = input("Cual es la receta?: ")

    recipe.write(recipe_content)

    recipe.close()

    print("Receta creada exitosamente")

    wait_screen()

def create_category():
    category = input("Cual es el nombre de la nueva categoria?: ")

    category_path = Path(main_folder_location() / category)

    clear_screen()

    os.mkdir(category_path)

    print("Categoria creada con exito!")
    wait_screen()

def delete_recipe():
    category = choose_category_menu(detect_categories())

    recipe_path = Path(main_folder_location() / category)

    clear_screen()

    recipe = choose_recipes_menu(main_folder_location() / category)

    recipe_path = Path(main_folder_location() / category / (recipe + ".txt"))



def delete_category():
    pass

def main_menu():

    validator = ["1", "2", "3", "4", "5", "6"]

    clear_screen()

    print("""
    Menu principal:
    
    1 - Leer receta
    2 - Crear receta
    3 - Crear categoria
    4 - Eliminar receta
    5 - Eliminar categoria
    6 - Cerrar programa
    """)

    option = input("Que deseas hacer?: ")

    if option not in validator:
        not_correct_option()

        main_menu()
    else:
        return option

def show_recipe():
    pass

def main_execution():
    clear_screen()

    base_location = main_folder_location()

    print("Bienvenido!!\n")
    print(f"Las recetas estan en {base_location}")
    print(f"Tienes {count_number_of_recipes(base_location)} disponibles")

    continue_enter()

    while True:

        option = main_menu()

        if option == "1":
            read_recipe()
        elif option == "2":
            create_recipe()
        elif option == "3":
            create_category()
        elif option == "6":
            break

main_execution()