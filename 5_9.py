def main():

 
    value = float(input(" Введите бщий обьем продаж:     "))

    mun = k(value)

    print(f"муниципальный налог с продаж {mun}")
    
    fed = f(value)

    print(f"муниципальный налог с продаж {fed}")

    all_n = a(mun,fed)

    print(f"общий налог с продаж {all_n}")
 


def k(value):
    z = value * 0.025
    return z

def f(value):
    z = value * 0.05
    return z

def a(mun,fed):
    w = mun + fed
    return w




    

    
 

    






    

    

 

    


    
    









    
 
    

    

    



    
   
