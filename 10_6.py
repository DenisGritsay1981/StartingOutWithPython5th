class Patient:

    def __init__(self,name,addres,phone,name_phone_friend):

        self.__name = name
        self.__addres = addres
        self.__phone = phone
        self.__name_phone_friend = name_phone_friend

    def set_name(self,name):
        self.__name = name

    def set_addres(self,addres):
        self.__addres = addres

    def set_phone(self,phone):
        self.__phone = phone

    def set_name_phone_friend(self,name_phone_friend):
        self.__name_phone_friend = name_phone_friend


    def get_name(self):
        return self.__name 

    def get_addres(self):
        return self.__addres
    
    def get_phone(self):
        return self.__phone
    
    def get_name_phone_friend(self):
        return self.__name_phone_friend

class Procedure:

    def __init__(self,procedure,date,doctor,value):

        self.__procedure = procedure
        self.__date = date
        self.__doctor = doctor
        self.__value = value

    def set_procedure(self,procedure):
        self.__procedure = procedure

    def set_date(self,date):
        self.__date = date

    def set_doctor(self,doctor):
        self.__doctor = doctor

    def set_value(self,value):
        self.__value = value

    def get_procedure(self):
        return self.__procedure 

    def get_date(self):
        return self.__date
    
    def get_doctor(self):
        return self.__doctor
    
    def get_value(self):
        return self.__value

def main():

    print("Введите данные  пациенте: ")
    name = input("Введите ФИО пациента:  ")
    addres = input("Введите адрес пациента: ")
    phone = input("Телефонный номер пациента: ")
    name_phone_friend = input("Имя и телефон друга пациента: ")
    q = Patient (name,addres,phone,name_phone_friend)

    
    print("Введите данные Процедуры № 1 ")
    procedure = input("Название процедуры:  ")
    date = input("Дата: ")
    doctor = input("Врач: ")
    value = float(input("Стоимость: "))
    a = Procedure (procedure,date,doctor,value)

    print("Введите данные Процедуры № 2 ")
    procedure = input("Название процедуры:  ")
    date = input("Дата: ")
    doctor = input("Врач: ")
    value = float(input("Стоимость: "))
    z = Procedure (procedure,date,doctor,value)

    print("Введите данные Процедуры № 3 ")
    procedure = input("Название процедуры:  ")
    date = input("Дата: ")
    doctor = input("Врач: ")
    value = float(input("Стоимость: "))
    w = Procedure (procedure,date,doctor,value)
    
    print()
    print("Вот данные Пациента:  ")
    print("ФИО:",q.get_name())
    print("Адрес:", q.get_addres())
    print("Телефон:", q.get_phone())
    print("Имя и адрес друга:", q.get_name_phone_friend())
    print()
    print("Вот данные Процедуры № 1:  ")
    print("Название: ",a.get_procedure())
    print("Дата: ",a.get_date())
    print("Врач: ",a.get_doctor())
    print("Стоимость: ",a.get_value())
    print()
    print("Вот данные Процедуры № 2:  ")
    print("Название: ",z.get_procedure())
    print("Дата: ",z.get_date())
    print("Врач: ",z.get_doctor())
    print("Стоимость: ",z.get_value())
    print()
    print("Вот данные Процедуры № 3:  ")
    print("Название: ",w.get_procedure())
    print("Дата: ",w.get_date())
    print("Врач: ",w.get_doctor())
    print("Стоимость: ",w.get_value())
    print()
    
if __name__ == "__main__":
  main()
 
                            
 
                                 
 
                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

