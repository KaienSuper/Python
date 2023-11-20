def quarter(xcord, ycord):
    if xcord > 0:
        if ycord > 0:
            print("1 quarter")
        else:
            print("4 quartet")
    else:
        if ycord > 0:
            print("2 quarter")
        else:
            print("3 quarter")
quarter(3, 4)