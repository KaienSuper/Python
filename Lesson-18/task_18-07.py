def solve(a=None, b=None, c=None):
    if b == None and c == None:
        return 0
    elif c == None:
        return -b/a
    elif a == None and b == None and c == None:
        return "None"
    else:
        D = b**2 - 4*a*c
        if D > 0:       
            x1, x2 = (-b + D**(1/2))/2*a, (-b - D**(1/2))/2*a
            return x1, x2
        elif D == 0:
            x1 = -b/2*a
            return x1
        else:
            return "None"

a, b, c = input("Введите коэффициенты: ").split(" ")
print(solve(int(a), int(b), int(c)))