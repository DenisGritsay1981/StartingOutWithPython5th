

month = 3
full_month = 0
full_charge = 0

for x in range (month):
    sum_month = float(input("Введите выделенную на месяц сумму:   "))
    full_month += sum_month
    print(f"1. сумма доходов нарастающим итогом равна:  {full_month} ")


    
    for z in [1]:
        
        charge_tax = float(input("2. Введите расходы на зп в текущем месяце:   "))
        charge_free = float(input("2. Введите расходы на ремонт в текущем месяце:   "))
        charge_other = float(input("2. Введите прочие расходы в текущем месяце:   "))

        full_charge = full_charge + charge_tax + charge_free + charge_other

        print(f"3. Расходы нарастающим итогом равны:  {full_charge}   ")



result = full_month - full_charge


print("Итого сумма превышения/недостатка доходов над расходами равна:   ")
print(result)
 










              







    
    

 







    

    

