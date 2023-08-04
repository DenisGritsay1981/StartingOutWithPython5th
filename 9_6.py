
def main():
    
    with open("cities.txt") as myfile:
        lines = myfile.read().splitlines()

    cities = set()

    for line in lines:
        cities.add(line)

    

    

    with open("cities2.txt") as myfile:
        x = myfile.read().splitlines()

    cities2 = set()

    for z in x:
        cities2.add(z)

    

    unic (cities,cities2)
    vse (cities,cities2)
    unic1 (cities,cities2)
    unic2 (cities,cities2)
    oba (cities,cities2)

def unic (cities,cities2):
    print(f"слова, входящие в оба файла одновременно: {cities.intersection(cities2)}")

def vse (cities,cities2):
    print(f"все слова: {cities.union(cities2)}")
    
def unic1 (cities,cities2):
    print(f"yникальные слова первого списка: {cities.difference(cities2)}")
   
def unic2 (cities,cities2):
    print(f"yникальные слова второго списка: {cities2.difference(cities)}")

def oba (cities,cities2):
    print(f"yникальные слова каждого множества: {cities.symmetric_difference(cities2)}")

    





    
    
  
    

                
    
    
                          
if __name__ == "__main__":
  main()
 
                            
 
                                

                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

