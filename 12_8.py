def main():
    
    
    m = int(input("Введите  число: "))
    n = int(input("Введите  числo: "))
    result = z(m,n)
    print(result)
    
def z(m,n):
    if m == 0:
        return n + 1
    elif n == 0:
        return z(m - 1,1)
    else:
        return z(m - 1, z(m,n-1))
    
main()

    
 
                                 
 
                                
        
       

    
     
 

        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

