import sqlite3

MIN_CHOICE = 1
MAX_CHOICE = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5

def main():
    choice = 0
    while choice != EXIT:
        display_menu()
        choice = get_menu_choice()

        if choice == CREATE:
                create()
        elif choice == READ:
                read()
        elif choice == UPDATE:
                update()
        elif choice == DELETE:
                delete()
def display_menu():
    print("\n----- Меню ведения учета инструментов-----")
    print("1.Создать новую позицию")
    print("2.Прочитать позицию")
    print("3.Обновить позицию")
    print("4.Удалить позицию")
    print("5.Выйти из программы")
def get_menu_choice():
    choice = None
    while choice is None:
        try:
            choice = int(input("Введите ваш номер: "))
            if choice < MIN_CHOICE or choice > MAX_CHOICE:
                print(f"Допустимые варианты таковы: {MIN_CHOICE} - {MAX_CHOICE}.")
                choice = None
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
    return choice

def create():
    
    print("Создать новую позицию")
    name = input("Имя: ")
    telephone = int(input("Номер телефона: "))
    insert_row(name,telephone)
def insert_row(name,telephone):
    conn = None
    try:
        conn = sqlite3.connect("phonebook.db")
        cur = conn.cursor()
        cur.execute("""INSERT INTO Entries (Name,Telephone)
                    VALUES (?,?)""",
                    (name,telephone))
        conn.commit()
    except sqlite3.Error as err:
        print("Ошибка базы данных",err)
    finally:
        if conn != None:
            conn.close()
            
def read():
    name = input("Введите имя человека: ")
    num_found = display_item(name)
    print(f"{num_found} строк найдено")
def display_item(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect("phonebook.db")
        cur = conn.cursor()
        cur.execute("""SELECT *  FROM Entries
                    WHERE Name = ?""",
                    (name,))
        result = cur.fetchall()
        for row in result:
            results.append(row)
            print(f"PhoneID: {row[0]:<3} Name: {row[1]:<15}"
                  f"Telephone: {row[2]:<6}")
                
    except sqlite3.Error as err:
        print("Ошибка базы данных",err)
    finally:
        if conn != None:
            conn.close()
            
    return len(results)

def update():
    read()
    select_id = int(input("Выберете ID обновляемой позиции"))
    name = input("Введите новое имя: ")
    telephone = int(input("Введите новый телефон: "))
    num_updated = update_row(select_id,name,telephone)
    print(f"{num_updated} строк(а) обновлено.")
def update_row(select_id,name,telephone):
    conn = None
    try:
        conn = sqlite3.connect("phonebook.db")
        cur = conn.cursor()
        cur.execute("""UPDATE Entries
                    SET Name = ?,
                    Telephone = ? WHERE PhoneID ==?""",
                    (name,telephone,select_id))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
        print("Ошибка базы данных",err)
    finally:
        if conn != None:
            conn.close()
    return num_updated

def delete():
    read()
    select_id = int(input("Выберете ID обновляемой позиции"))
    sure = input("Вы уверены, что хотите удалить эту позицию? (д/н)")
    if sure.lower() == "д":
        num_deleted = delete_row(select_id)
        print(f"{num_deleted} строк(а) удалено")
def delete_row(select_id):
    num_deleted = 0
    conn = None
    try:
        conn = sqlite3.connect("phonebook.db")
        cur = conn.cursor()
        cur.execute("""DELETE FROM Entries
                    WHERE PhoneID == ?""",
                    (select_id,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print("Ошибка базы данных",err)
    finally:
        if conn != None:
            conn.close()
    return num_deleted

if __name__ == "__main__":
  main()
    
 
                                 
 
                                
        
       

    
     
 

        
 
  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

