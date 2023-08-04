import random

def main():


    x = open("steps.txt","w")
    
    print("Данный файл генерирует количество шагов за год или 365 дней")
    for i in range(1,366,1):
        y = random.randint(1,10000)
        z = str(y)
        x.write(f"{z}\n")


    print("данные записаны в файл steps.txt ")

    x.close()


    
  

if __name__ == "__main__":
  main()




 
      

  


 
  

            
        

    
    
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

