lenght1 = int(input("введите длину первого прямоугольника:   "))
width1 = int(input("введите ширину первого прямоугольника:   "))

s1 = lenght1*width1

print(f"площаль первого равна: {s1}")

lenght2 = int(input("введите длину второго прямоугольника:   "))
width2 = int(input("введите ширину второго прямоугольника:   "))

s2 = lenght2*width2

print(f"площаль второго равна: {s2}")

if s1>s2:
    print("первый больше")
elif s1<s2:
    print("второй больше")
else:
    print("они одинаковы")
