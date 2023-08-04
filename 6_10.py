

def main():


    x = open("golf.txt","w")

    q = "Да"

    while q == "Да" or q == "да":

      print("Введите имя и очки игрока:  ")
      name = input("Введите имя игрока:  ")
      tax = int(input("Введите его очки:  "))

      x.write(f"{name}\n")
      x.write(f"{tax}\n")
      print("Если хотите продолжить введите Да")
      q = input(" ")
      

    x.close()


    
  

if __name__ == "__main__":
  main()




 
      

  


 
  

            
        

    
    
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

