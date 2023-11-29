def discriminant(a, b, c):
    return (b**2) - (4*a*c)

def larger_root(p, q):
    return (p + discriminant(1, p, q)**(1/2))/2

def smaller_root(p, q):
    return (p - discriminant(1, p, q)**(1/2))/2

def main():
    p_ex = float(input("b: "))
    q_ex = float(input("c: "))
    print("Дискриминант", discriminant(1, p_ex, q_ex))
    print("Меньший корень:", smaller_root(p_ex, q_ex))
    print("Больший корень:", larger_root(p_ex, q_ex))

main()