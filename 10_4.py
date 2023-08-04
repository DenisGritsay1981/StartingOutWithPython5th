class Employee:

    def __init__(self,name,number,department,position):

        self.__name = name
        self.__number = number
        self.__department = department
        self.__position = position

    def set_name(self,name):
        self.__name = name

    def set_number(self,number):
        self.__number = number

    def set_department(self,department):
        self.__department = department

    def set_position(self,position):
        self.__position = position

    def get_name(self):
        return self.__name 

    def get_number(self):
        return self.__number
    
    def get_department(self):
        return self.__department
    
    def get_position(self):
        return self.__position

def main():

    print("Введите данные Сьюзан Маерс")
    name = input("Введите имя:  ")
    number = int(input("Номер: "))
    department = input("Отдел: ")
    position = input("Должность: ")

    q = Employee(name,number,department,position)
    print("Вот данные Сьюзан Маерс:  ")
    print(q.get_name())
    print(q.get_number())
    print(q.get_department())
    print(q.get_position())


    print("Введите данные Марка Джоунса")
    name = input("Введите имя:  ")
    number = int(input("Номер: "))
    department = input("Отдел: ")
    position = input("Должность: ")

    a = Employee(name,number,department,position)
    print("Вот данные Марка Джоунса:  ")
    print(a.get_name())
    print(a.get_number())
    print(a.get_department())
    print(a.get_position())

    print("Введите данные Джой Роджерса")
    name = input("Введите имя:  ")
    number = int(input("Номер: "))
    department = input("Отдел: ")
    position = input("Должность: ")

    z = Employee(name,number,department,position)
    print("Вот данные Джой Роджерса:  ")
    print(z.get_name())
    print(z.get_number())
    print(z.get_department())
    print(z.get_position())
    
if __name__ == "__main__":
  main()
 
                            
 
                                 
 
                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

