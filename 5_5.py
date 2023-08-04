def main():

    TAX = 0.6

    print("Введите фактическую стоимость имущеста")

    fact_value = float(input(" "))

    value = x(fact_value, TAX)

    print(f"Оценочная стоимость имущества:  {value}")

    tax_n = q(value)

    print(f"Налог на имущество:  {tax_n:,.2f}")
    
def x(fact_value, TAX):
    z = fact_value * TAX
    return z

def q(value):
    g = (value /100)*0.72
    return g




    


    
    









    
 
    

    

    



    
   
