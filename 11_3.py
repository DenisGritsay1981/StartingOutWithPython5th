class Person:

    def __init__(self,name,addres,phone):

        self.__name = name
        self.__addres = addres
        self.__phone = phone
        
    def set_name(self,name):
        self.__name = name

    def set_addres(self,addres):
        self.__addres = addres

    def set_phone(self,phone):
        self.__phone = phone
 
    def get_name(self):
        return self.__name 

    def get_addres(self):
        return self.__addres

    def get_phone(self):
        return self.__phone

class Customer(Person):

    def __init__(self,name,addres,phone,number,want):
        
        Person.__init__(self,name,addres,phone)
        self.__number = number
        self.__want = want
            
    def set_number(self,number):
        self.__number = number

    def set_prize(self,want):
        self.__want = want

    def get_number(self):
        return self.__number

    def get_want(self):
        if self.__want.lower() == "да":
            print("Клиент хочет быть в спивке рассылки")
        elif self.__want.lower() == "нет":
            print("Клиент  не хочет быть в спивке рассылки")
        else:
            print("Ответ не корректен")
        return self.__want

def main():

    print("Введите данные по Клиенту: ")
    name = input("Введите имя: ")
    addres = input("Введите адрес: ")
    phone = input("Введите номер телефона: ")
    number = int(input("Введите номер клиента: "))
    want = input("Введите, хочет ли клиент получать рассылку да/нет: ")
    
    x = Customer (name,addres,phone,number,want)
    print("Вот данные, которые вы ввели:  ")
    print("Имя: ", x.get_name())
    print("Адрес: ", x.get_addres())
    print("Телефон: ", x.get_phone())
    print("Номер Клиента: ", x.get_number())
    print("Желает ли клиент получать подписку: ", x.get_want())

        
if __name__ == "__main__":
  main()

    

    
        
    
    
   

 
                            
 
                                 

                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

