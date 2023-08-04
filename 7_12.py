
def main():

    
    z = int(input("Введите число больше 1"))
   
    if z > 1:
        spis = [a for a in range (2,z+1)]
    else:
        print("Вы ввели неверное число")

    print(spis)

    for x in spis:
        result = is_prime(x)
        if not result:
            print(f"число {x} составное")
        else:
            print(f"число {x} простое")

    
    

def is_prime(number):
    if number > 1:
        for x in range(2, number,1):
            if number%x == 0:
                return False
        else:
            return True
    else:
        return False

        
        

                    
if __name__ == "__main__":
  main()


                            

                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

