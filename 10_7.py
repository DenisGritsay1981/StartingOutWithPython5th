import pickle
import employee

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = "employee.dat"

def main():

    my_employees = load_slovar()

    choice = 0
    while choice != QUIT:
        choice = load_choice()
        if choice == LOOK_UP:
            find(my_employees)
        if choice == ADD:
            add(my_employees)
        if choice == CHANGE:
            change(my_employees)
        if choice == DELETE:
            delete(my_employees)
            
    save(my_employees)

def save(z):
    q = open(FILENAME, "wb")
    pickle.dump(z,q)
    q.close()
              
def delete(z):
    while True:
        try:
            number = int(input("Введите номер сотрудника: "))
            break
        except ValueError:
            print("Некорректный ввод. Введите целое число.")

    if number in z:
        del z[number]
        print("Запись удалена")
    else:
        print("Сотрудника с таким номером не существует")
           
def change(z):

    while True:
        try:
            number = int(input("Введите номер сотрудника: "))
            break
        except ValueError:
            print("Некорректный ввод. Введите целое число.")

    if number in z:
        name = input("Введите имя сотрудника:  ")
        department = input("Введите отдел:  ")
        position = input("Введите должность сотрудника: ")
        x = employee.Employee(name,number,department,position)
        z[number] = x
        print("Запись изменена")
    else:
        print("Сотрудника с таким номером не существует")

def add(z):
    while True:
        try:
            number = int(input("Введите номер сотрудника: "))
            break
        except ValueError:
            print("Некорректный ввод. Введите целое число.")
    
    if number in z:
        print("Сотрудник с таким номером существует")
    else:
        name = input("Введите имя сотрудника:  ")
        department = input("Введите отдел:  ")
        position = input("Введите должность сотрудника: ")
        x = employee.Employee(name,number,department,position)
        z[number] = x
        print("Запись добавлена")
                 
def find(z):
    while True:
        try:
            x = int(input("Введите номер сотрудника: "))
            break
        except ValueError:
            print("Некорректный ввод. Введите целое число.")

    employee = z.get(x)
    if employee is not None:
        print(employee.get_number(), employee.get_name(), employee.get_department(), employee.get_position())
    else:
        print("Сотрудник с таким номером отсутствует")
    
def load_choice():
    
    print("1 - найти сотрудника в словаре")
    print("2 - добавить сотрудника в словарь")
    print("3 - изменить имя, отдел и должность существующего сотрудника")
    print("4 - удалить сотрудника из словаря")
    print("5 - выйти из меню")
    print("Выберете пункт меню: ")
    x = int(input(" "))
    if x < 1 or x > 5:
        print("Выберете пункт меню: ")
        x = int(input(" "))
    return x

def load_slovar():
    try:
        output_file = open(FILENAME,"rb")
        x = pickle.load(output_file)
        output_file.close()
    except:
        x = {}
    return x
  
if __name__ == "__main__":
  main()
 
                            
 
                                 
 
                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

