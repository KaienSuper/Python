count_recipe = int(input("Enter a count of all recipe: "))
all_recipe_list = set()
recipe_for_day_list = set()
recipe_cook_list = set()
for _ in range(count_recipe):
    recipe = input("Recipe: ")
    all_recipe_list.add(recipe)
count_day = int(input("Enter a count of days: "))
for _ in range(count_day):
    count_recipe_in_day = int(input("Enter a count of recipe in day: "))
    for _ in range(count_recipe_in_day):
        recipe_for_day = input("Recipe: ")
        recipe_for_day_list.add(recipe_for_day)

for elem in all_recipe_list:
    if elem not in recipe_for_day_list:
        recipe_cook_list.add(elem)
print("\n")
for elem in recipe_cook_list:
    print(elem)