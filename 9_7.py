
def main():
    
    with open("WorldSeriesWinners.txt") as myfile:
        lines = myfile.read().splitlines()

    com_sumpobed (lines)
    com_year(lines)
    free (lines)
    

def com_sumpobed(lines):

    WSW = {}

    for line in lines:
        if line in WSW:
            WSW[line] += 1  
        else:
            WSW[line] = 1
    print()
    print("Перечень побед команда : кол-во побед")
    print()
    print(WSW)

def com_year(lines):

    first_year = 1903
    WSW2 = {}
   
    for line in lines:
        WSW2[first_year] = line
        first_year += 1
    print() 
    print("Год - команда победитель")
    print()
    print(WSW2)

def free (lines):

    WSW = {}
    for line in lines:
        if line in WSW:
            WSW[line] += 1  
        else:
            WSW[line] = 1

    first_year = 1903
    WSW2 = {}
    for line in lines:
        WSW2[first_year] = line
        first_year += 1

    print()
    year = int(input("Введите год, в котором хотите видеть\
                     название команты и кол-во побед"))

    if year > 1902 and year < 2010:
        True
        print(f"команда победитель в {year} году - {WSW2[year]}")
        print(f"количество побед команды {WSW2[year]} равно {WSW[WSW2[year]]}")
    else:
        False
        print("введите правильное значение от 1903 до 2009 года включительно")
    
        

   
   

    

    



        
        

    

    

                
  
            
            
            
            
            

    
    

    

    

        





    
    
  
    

                
    
    
                          
if __name__ == "__main__":
  main()
 
                            
 
                                

                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

