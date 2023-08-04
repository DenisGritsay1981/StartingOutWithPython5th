

print("введите время падения в секундах")
t = float(input(""))

def falling_distance(t):
    d = 1/2*(9.8*t**2)
    return d

x = falling_distance(t)
print("расстояние полета, метров:")
print(x)

   
    

for t in range(1,11,1):
    x = falling_distance(t)
    print(f"{x:,.2f}")
    
    
    


    
    
    
    


    
    




    

    
 

    






    

    

 

    


    
    









    
 
    

    

    



    
   
