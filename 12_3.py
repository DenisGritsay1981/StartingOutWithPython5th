

def main():
    
    ast="*"
    num=1
   
    end=int(input("How many end of asterisks: "))
    print()
    
   
    print_asterisk(ast, num, end)
    

def print_asterisk(ast, num, end):
    if end>num:
        print(ast*num) 
        num+=1
        return print_asterisk(ast, num, end)
    elif end==num:
        print(ast*num) 
        

main()

    
 
                                 
 
                               
        
       

    
     
 

        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

