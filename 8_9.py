
def main():

    x = str(input("Введите строковое значение"))
    g(x)
    

def g(x):

    glas = ["а", "у", "о", "ы", "и", "э", "я", "ю", "е", "е"]
    soglas = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]

    l_glas = 0
    l_soglas = 0

    for z in x:
        if z in glas:
            l_glas += 1
        else:
            None
    for z in x:
        if z in soglas:
            l_soglas += 1
        else:
            None

    print (l_glas)
    print(l_soglas)

    

    
        
            
            
        
       
        
        
    
    
  
            
            
    
if __name__ == "__main__":
  main()

                            
 
                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

