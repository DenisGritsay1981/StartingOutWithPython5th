year = int (input("Введите год:  "))


if year % 100 == 0 and year%400 == 0:
    print(f"В {year} году в феврале 29 дней")
elif year % 100 != 0 and year%4 == 0:
    print(f"В {year} году в феврале 29 дней")
else:
    print(f" {year} год не является высокостным") 


    
    

 







    

    

