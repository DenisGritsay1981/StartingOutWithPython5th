item1 = float(input("Стоимость первого товара равняется: "))
item2 = float(input("Стоимость второго товара равняется: "))
item3 = float(input("Стоимость третьего товара равняется: "))
item4 = float(input("Стоимость четвертого товара равняется: "))
item5 = float(input("Стоимость пятого товара равняется: "))

final_sales = item1 + item2 + item3 + item4 + item5
tax = final_sales * 0.07
final_profit = final_sales - tax 

print("стоимость приобретенных товаров:", final_sales )
print("налог с продаж: ", tax )
print("итоговая прибыль равна: ", final_profit )
              
              


 
