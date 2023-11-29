friends_dict = {}
def add_friends(name, names_friends):
    friends_dict[name] = names_friends

def are_friends(name, names_friends):
    if names_friends in friends_dict[name]:
        return True
    else:
        return False
    
def print_friends(name):
    print(friends_dict[name])

add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))
