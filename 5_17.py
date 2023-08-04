



def is_prime(number):
    if number > 1:
        for x in range(2, number,1):
            if number%x == 0:
                return False
        else:
            return True
    else:
        return False
        

for number in range (10):
    x = is_prime(number)
    if x == False:
        print()
    else:
        print(f"число {number} является простым")
    

     

        
    
    

   
    





    
    
    

 





    
    


    
    


    
    
    
    


    
    




    

    
 

    






    

    

 

    


    
    









    
 
    

    

    



    
   
