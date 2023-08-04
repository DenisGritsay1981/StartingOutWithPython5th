

stock1 = 2000*40
tip1 = stock1 * 0.03

stock2 = 2000*42.75
tip2 = stock2 * 0.03

print("сумма, уплаченная в первый раз: ", stock1)
print("сумма, комиссии уплаченная в первый раз: ",tip1)
print("сумма, уплаченная в второй раз: ", stock2)
print("сумма, комиссии уплаченная в второй раз: ",  tip2)

profit = stock2 - stock1
final_profit = profit - (tip1+tip2)

print("итоговый доход Джона без учета комисии: ",final_profit)



 
