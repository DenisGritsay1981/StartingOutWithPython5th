def main():

    print("Введите месячные расходы, связанные с автомобилем")

    
    loan_payment =  float(input(" платеж по кредиту  : "))

    tech_service = t()

    insurance = float(input(" сумму страховки автомобиля  : "))

    petrol = float(input(" сумму расходов на бензин  : "))

    machine_oil = float(input(" расходы на машинное масло  : "))

    tires = float(input(" шины  : "))

    month = m(loan_payment,tech_service,insurance,petrol,machine_oil,tires)

    print(f"расходы за месяц: {month}")

    year = y(loan_payment,tech_service,insurance,petrol,machine_oil,tires)

    print(f"расходы за год:   {year}")
    
def t():
    x = float(input(" введите сумму техобслуживания  : "))
    return x

def m(loan_payment,tech_service,insurance,petrol,machine_oil,tires):
    x = loan_payment + tech_service + insurance + petrol + machine_oil + tires
    return x

def y(loan_payment,tech_service,insurance,petrol,machine_oil,tires):
    z = (loan_payment + tech_service + insurance + petrol + machine_oil + tires)*12
    return z








    
 
    

    

    



    
   
