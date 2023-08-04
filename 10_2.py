class Car:

    def __init__(self,year_model,make):

        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def set_accelerate(self,speed):
        self.__speed = speed + 5

    def set_break(self,speed):
        self.__speed = speed - 5

    def get_speed(self):
        return self.__speed

def main():
    year_model = int(input("Введите год выпуска:  "))
    make = input("Введите фирму изготовителя модели:  ")
    q = Car(year_model,make)
    for x in range(1,6):
        
        speed = int(input("Введите текущую скорость:  "))
        q.set_accelerate(speed)
        print("Скорость равна:", q.get_speed())

    for x in range(1,6):
        
        speed = int(input("Введите текущую скорость:  "))
        q.set_break(speed)
        print("Скорость равна:", q.get_speed())
                  
if __name__ == "__main__":
  main()
 
                            
 
                                 
 
                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

