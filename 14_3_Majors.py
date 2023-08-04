import sqlite3

MIN_CHOICE = 1
MAX_CHOICE = 6
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
FIND = 5
EXIT = 6

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
        elif choice == FIND:
                find()
            
def display_menu():
    print("\n----- Меню специальностей-----")
    print("1.Добавить новую специальность")
    print("2.Вывести на экран все специальности ")
    print("3.Обновить специальность")
    print("4.Удалить специальность")
    print("5.Найти существующую специальность")
    print("6.Выйти из программы")
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
    print("Добавить новую специальность")
    name = input("Название специальности: ")
    insert_row(name)
def insert_row(name):
    conn = None
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("""INSERT INTO Majors (Name)
                    VALUES (?)""",
                    (name,))
        conn.commit()
        print("Данные сохранены")
    except sqlite3.Error as err:
        print("Ошибка базы данных",err)
    finally:
        if conn != None:
            conn.close()

def read():
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("""SELECT *  FROM Majors""")                
        result = cur.fetchall()
        for row in result:
            print(f" MajorID: {row[0]:3} Name: {row[1]:15}")
        conn.close()
    except sqlite3.Error as e:
        print("Ошибка при чтении таблицы Majors: ", e)

def update():
    read()
    select_id = int(input("Выберете ID обновляемой позиции"))
    name = input("Введите новую специальность: ")
    num_updated = update_row(select_id,name)
    print(f"{num_updated} строк(а) обновлено.")
def update_row(select_id,name):
    conn = None
    num_updated = 0
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("""UPDATE Majors
                    SET Name = ?
                    WHERE MajorID == ?""",
                    (name,select_id))
        conn.commit()
        num_updated = cur.rowcount   
    except sqlite3.Error as err:
        print("Ошибка базы данных",err)
    finally:
        if conn != None:
            conn.close()
    return num_updated

def read_students():
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("""SELECT *  FROM Students""")                
        result = cur.fetchall()
        for row in result:
            print(f" StudentID: {row[0]:3} Name: {row[1]:15} MajorID: {row[2]:3} DeptID: {row[3]:3}")
        conn.close()
    except sqlite3.Error as e:
        print("Ошибка при чтении таблицы Students: ", e)
  

def delete():
    print("Вот данные таблицы Majors")
    read()
    print("Вот данные таблицы Students")
    read_students()
    print("Удаление строки из таблицы Majors не должно совпадать с налицием ее в Students")
    select_id = int(input("Выберете ID обновляемой позиции"))
    sure = input("Вы уверены, что хотите удалить эту позицию? (д/н)")
    if sure.lower() == "д":
        num_deleted = delete_row(select_id)
        print(f"{num_deleted} строк(а) удалено")
        
def delete_row(select_id):
    num_deleted = 0
    conn = None
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        cur.execute("""DELETE FROM Majors
                    WHERE MajorID == ?""",
                    (select_id,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.IntegrityError as err:
        print("Ошибка ",err)
    finally:
        if conn != None:
            conn.close()
    return num_deleted


  

def find():
    name = input("Введите специальность: ")
    num_found = display_item(name)
    print(f"{num_found} специальностей найдено")
def display_item(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("""SELECT *  FROM Majors
                    WHERE Name = ?""",
                    (name,))
        result = cur.fetchall()
        for row in result:
            results.append(row)
            print(f" MajorID: {row[0]:<3} Name: {row[1]:<15}")         
    except sqlite3.Error as err:
        print("Ошибка базы данных",err)
    finally:
        if conn != None:
            conn.close()
            
    return len(results)


if __name__ == "__main__":
  main()
    
 
                                 
 
                                
        
       

    
     
 

        
 
  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

