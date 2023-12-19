def matrix(n=None, m=None, a=None):
    if (n is None) and (m is None) and (a is None):
        print("0")
    elif m is None and a is None:
        for _ in range(n):
            for _ in range(n):
                print("0", end=" ")
            print()
    elif a is None:
        for _ in range(n):
            for _ in range(m):
                print("0", end=" ")
            print()
    else:
        for _ in range(n):
            for _ in range(m):
                print(a, end=" ")
            print()
    print()

matrix()
matrix(2)
matrix(2, 3)
matrix(2, 3, 1)