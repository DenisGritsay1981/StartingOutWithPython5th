weight_1 = int(input("Введите массу одного пакета, г:  "))



if weight_1 <= 200:
    fee = 150
elif weight_1 > 200 and weight_1 <= 600 :
    fee = 300
elif weight_1 > 600 and weight_1 <= 1000 :
    fee = 400
else:
    fee = 475

print(f"ставка за 100г: {fee} рублей")





    

    

