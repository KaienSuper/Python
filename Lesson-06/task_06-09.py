count_all_ingredients = int(input("Enter a count of Ingredients: "))
my_ingredients_list = set()
ingr_for_recipe_list = set()
recipe_cook_list = set()
for _ in range(count_all_ingredients):
    my_ingredient = input("Ingredient: ")
    my_ingredients_list.add(my_ingredient)
print("\n")

count_recipe = int(input("Enter a count of recipe: \n"))
for _ in range(count_recipe):
    recipe_name = input("Recipe: ")
    count_ingr_for_recipe = int(input("Enter a count of Ingredients for recipe: "))

    for _ in range(count_ingr_for_recipe):
        ingr_for_recipe = input("Ingredient: ")
        ingr_for_recipe_list.add(ingr_for_recipe)

    for elem in ingr_for_recipe_list:
        if elem in my_ingredients_list:
            point = True
        else:
            point = False
            break
    
    if point == True:
        recipe_cook_list.add(recipe_name)
    print("\n")

print(recipe_cook_list)