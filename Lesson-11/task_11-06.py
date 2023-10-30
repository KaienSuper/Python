recipe_list = [input(": ") for _ in range(int(input("Count text: ")))]
new_recipe_list = [i for i in recipe_list if "лук" not in i]
print(", ".join(new_recipe_list))