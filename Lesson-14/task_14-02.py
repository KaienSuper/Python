def space_game():
    text = input("Text: ")
    if text.count(" ") // 2 == 0:
        print("You Win")
    else:
        print("You Lose")
space_game()