class Information:

    def __init__(self,name,addres,age,t_number):

        self.__name = name
        self.__addres = addres
        self.__age = age
        self.__t_number = t_number

    def set_name(self,name):
        self.__name = name

    def set_addres(self,addres):
        self.__addres = addres

    def set_age(self,age):
        self.__age = age

    def set_t_number(self,t_number):
        self.__t_number = t_number
        

    def get_name(self):
        return self.__name

    def get_addres(self):
        return self.__addres
    
    def get_age(self):
        return self.__age
    
    def get_t_number(self):
        return self.__t_number

def main():

    name = input("Введите свое имя:  ")
    addres = input("Введите свой адрес: ")
    age = int(input("Введите свой возраст: "))
    t_number = int(input("Введите свой телефонный номер"))

    q = Information(name,addres,age,t_number)
    print("Вот данные, которые вы ввели:  ")
    print(q.get_name())
    print(q.get_addres())
    print(q.get_age())
    print(q.get_t_number())

    name = input("Введите имя друга:  ")
    addres = input("Введите  адрес друга: ")
    age = int(input("Введите возраст друга: "))
    t_number = int(input("Введите  телефонный номер друга"))

    w = Information(name,addres,age,t_number)
    print("Вот данные, которые вы ввели:  ")
    print(w.get_name())
    print(w.get_addres())
    print(w.get_age())
    print(w.get_t_number())

    print("Вот повтор ваших данных:  ")
    print(q.get_name())
    print(q.get_addres())
    print(q.get_age())
    print(q.get_t_number())

if __name__ == "__main__":
  main()
 
                            
 
                                 
 
                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

