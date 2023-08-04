def main():
    

    stricture_price =  float(input("введите стоимость строения для страховки  : "))
 
    print(f"Стоимость строения равна:   {stricture_price}")

    print("процент для страховки должен быть от 0.8 до 1")

    stricture_percent = float(input("введите процент для страховки  : "))

    percent = tip(stricture_percent)

    print(f"процент :   {percent}")

    min_strah = strah(percent,stricture_price)

    print("Минимальная сумма, на которую нужно застраховать имущество равно:")

    print(f"{min_strah}")


def tip(stricture_percent):
    
    if stricture_percent >= 0.8 and stricture_percent <= 1:
        result = stricture_percent
    else:
        result = False
        print("Процент введет неверно")

    return result 
    
def strah(percent,stricture_price):
    x = percent * stricture_price
    return x

    



    
   
