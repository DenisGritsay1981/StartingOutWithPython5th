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

class ShiftSupervisor(Employee):

    def __init__(self,name,number,salary,prize):
        Employee.__init__(self,name,number)
        self.__salary  = salary
        self.__prize = prize

    def set_salary(self,salary):
        self.__salary  = salary

    def set_prize(self,prize):
        self.__prize = prize

    def get_salary(self):
        return self.__salary

    def get_prize(self):
        return self.__prize

def main():

    print("Введите данные но начальнику смены: ")
    name = input("Введите имя: ")
    number = int(input("Введите номер: "))
    salary = float(input("Введите зарплаты: "))
    prize = float(input("Введите премию: "))
    x = ShiftSupervisor (name,number,salary,prize)
    print("Вот данные, которые вы ввели:  ")
    print("Имя", x.get_name())
    print("Номер", x.get_number())
    print("Зарплата", format(x.get_salary(), ",.2f"), sep="")
    print("Премия", format(x.get_prize(), ",.2f"), sep="")
    
if __name__ == "__main__":
  main()

    

    
        
    
    
   

 
                            
 
                                 

                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

