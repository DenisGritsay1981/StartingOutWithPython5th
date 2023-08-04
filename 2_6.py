purchase = float(input("введите величину покупки: "))
federal_tax = purchase * 0.05
region_tax = purchase * 0.025

print("общая сумма покупки: ", purchase)
print("федеральный налог: ", federal_tax)
print("региональный налог: ",region_tax)
print(f"общий налог с продаж равен: {federal_tax + region_tax}")
print(f"общую сумму продажи: {federal_tax + region_tax + purchase}")
