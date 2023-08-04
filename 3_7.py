a = str(input("Введите цвет А:  "))

b = str(input("Введите цвет В:  "))

if a == "red" and b =="blue" or a == "blue" and b =="red":
    print("purple")
elif a == "red" and b =="yellow" or a == "yellow" and b =="red":
    print("orange")
elif a == "blue" and b =="yellow" or a == "yellow" and b =="blue":
    print("green")
elif a == "red" and b =="red":
    print("red")
elif a == "blue" and b =="blue":
    print("blue")
elif a == "yellow" and b =="yellow":
    print("yellow")
else:
    print("Ваше сочетание цветов не дает результат")
    

    
    
    

    

