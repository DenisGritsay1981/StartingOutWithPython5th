class Employee:

    def __init__(self,name,number):

        self.__name = name
        self.__number = number
        
    def set_name(self,name):
        self.__name = name

    def set_number(self,number):
        self.__number = number

    def get_name(self):
        return self.__name 

    def get_number(self):
        return self.__number

class ProductionWorker(Employee):

    def __init__(self,name,number,num_change,rate):
        Employee.__init__(self,name,number)
        self.__num_change  = num_change 
        self.__rate = rate

    def set_num_change(self,num_change):
        num_change = int(input("Введите номер смены - 1 дневная, 2 - ночная: "))
        if num_change == 1 and num_change == 2:
            self.__num_change = num_change
            print("Данные смены присвоены")
        else:
            print("Вы ввели неверный номер")

    def set_rate(self,rate):
        self.__rate = rate

    def get_num_change(self):
        return self.__num_change 

    def get_rate(self):
        return self.__rate

def main():

    print("Введите данные но рабочему смены: ")
    name = input("Введите имя сотрудника: ")
    number = int(input("Введите номер сотрудника"))
    num_change = int(input("Введите номер смены 1 дневной 2 ночной: "))
    rate = int(input("Введите ставку почасовой оплаты труда: "))
    x = ProductionWorker (name,number,num_change,rate)
    print("Вот данные, которые вы ввели:  ")
    print("Имя", x.get_name())
    print("Номер", x.get_number())
    print("Номер смены", x.get_num_change())
    print("Ставка оплаты", x.get_rate())
    
if __name__ == "__main__":
  main()

    

    
        
    
    
   

 
                            
 
                                 

                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

