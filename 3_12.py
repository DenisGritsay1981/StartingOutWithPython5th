prog_box = int(input("Введите количество приобретенных пакетов программного обеспечения:  "))

box_price = 99

if prog_box >= 10 and prog_box <=19:
    discount = 0.1
elif prog_box >= 20 and prog_box <=49:
    discount = 0.2
elif prog_box >= 50 and prog_box <=99:
    discount = 0.3
elif prog_box >= 100 :
    discount = 0.4
else:
    print("скидка не предоставляется")





print(f"скидка равняется:    {discount}")

print(f"общая стоимость покупок без скидок:    {prog_box*box_price}")



print(f"сумма скидок в рублях:    {prog_box*box_price*discount}")   

      
print(f"скидка, согластно сумме покупок равняется:    {(prog_box*box_price) - (prog_box*box_price*discount)}") 
    

    

