def triangle(a, b, c):
    if a + b > c:
        if a + c > b:
            if b + c > a:
                print('This is a triangle')
            else:
                print("This not is a triangle")
        else:
            print("This not is a triangle")
    else:
        print("This not is a triangle")
triangle(1, 1, 2)
triangle(7, 6, 10)