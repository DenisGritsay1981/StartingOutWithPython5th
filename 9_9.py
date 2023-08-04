import random

class Coin:

    def __init__(self):
        self.__sideup = "Орел"
        
    def toss(self):
        if random.randint(0,1) == 1:
            self.__sideup = "Орел"
        else:
            self.__sideup = "Решка"
    def get_sideup(self):
        return self.__sideup

def main():

    my_coin = Coin()

    print("Эта сторона обращена вверх:  ", my_coin.get_sideup())

    print("Подбрасывать монету 10 раз")

    for x in range(10):
        my_coin.toss()
        print("Эта сторона обращена вверх:  ", my_coin.get_sideup())


if __name__ == "__main__":
  main()
 
                            
 
                                 

                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

