eat = float(input("Стоимость заказаной еды равняется: "))

tax = eat * 0.07
tip = eat * 0.18 
 

print(f"налог: {tax:.1f}" )
print("чаевые: ", tip )
print(f"итоговая сумма равна: {eat + tax + tip}" )
              
              


 
