weight = float(input("Введите массу человека, кг:  "))
height = float(input("Введите рост человека, м:  "))

IMT =weight//(height**2) 

if  18.5 <= IMT and IMT <= 25:
    print(f"Ваша масса соответствует норме {IMT}")
elif IMT > 25:
    print(f"Ваша масса выше нормы {IMT}")
else:
    print(f"Ваша масса ниже нормы {IMT}")







    

    

