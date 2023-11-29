def circle_length(radius):
    return 2*PI*radius

def circle_area(radius):
    return PI*(radius**2)

PI = 3.14159

def main():
    radius_ex = int(input("Какой радиус: "))
    print("Длина окружности: ", circle_length(radius_ex))
    print("Площадь окружности: ", circle_area(radius_ex))

main()