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
    print("\n----- Меню студентов-----")
    print("1.Добавить нового студента")
    print("2.Вывести на экран всех студентов ")
    print("3.Обновить студента")
    print("4.Удалить студента")
    print("5.Найти существующего студента")
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

def read_departments():
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("""SELECT *  FROM Departments""")                
        result = cur.fetchall()
        for row in result:
            print(f" DeptID: {row[0]:3} Name: {row[1]:15}")
        conn.close()
    except sqlite3.Error as e:
        print("Ошибка при чтении таблицы Departments: ", e)
def read_majors():
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

def create():
    try:
        print("Добавить студента")
        name = input("Имя студента: ")
        print("Добавить специальность и факультет из существующих таблиц: ")
        read_departments()
        major = int (input("Добавить НОМЕР специальности"))
        read_majors()
        dept = int (input("Добавить НОМЕР факультета"))
        insert_row(name,major,dept)
    except sqlite3.Error as err:
        print("Ошибка ввода данных",err)
def insert_row(name,dept,major):
    conn = None
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        cur.execute("""INSERT INTO Students (Name,MajorID,DeptID)
                    VALUES (?,?,?)""",
                    (name,major,dept))
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
        cur.execute("PRAGMA foreign_keys=ON")
        cur.execute(
            """SELECT Students.Name,Majors.MajorID,Departments.DeptID
               FROM Students,Majors,Departments
               WHERE Students.MajorID == Majors.MajorID and  Students.DeptID == Departments.DeptID""")                           
        result = cur.fetchall()
        for row in result:
            print(f"  Name: {row[0]:15} MajorID: {row[1]:10} DeptID: {row[2]:2}")
        conn.close()
    except sqlite3.Error as e:
        print("Ошибка при чтении таблицы Students: ", e)


def update():
    try:
        read()
        select_id = int(input("Выберете ID обновляемой позиции"))
        name = input("Имя студента: ")
        num_updated = update_row(select_id,name)
        print(f"{num_updated} строк(а) обновлено.")  
    except sqlite3.Error as err:
        print("Ошибка ввода данных",err)
def update_row(select_id,name):
    conn = None
    num_updated = 0
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        cur.execute("""UPDATE Students
                    SET Name = ?
                    WHERE StudentID == ?""",
                    (name,select_id))
        conn.commit()
        num_updated = cur.rowcount   
    except sqlite3.Error as err:
        print("Ошибка базы данных",err)
    finally:
        if conn != None:
            conn.close()
    return num_updated

def delete():
    try:
        read()
        select_id = int(input("Выберете ID удаляемой позиции"))
        sure = input("Вы уверены, что хотите удалить эту позицию? (д/н)")
        if sure.lower() == "д":
            num_deleted = delete_row(select_id)
            print(f"{num_deleted} строк(а) удалено")       
    except sqlite3.Error as err:
            print("Ошибка ввода данных",err)
    
def delete_row(select_id):
    num_deleted = 0
    conn = None
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        cur.execute("""DELETE FROM Students
                    WHERE StudentID == ?""",
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
    name = input("Введите имя студента: ")
    num_found = display_item(name)
    print(f"{num_found} студентов найдено")
def display_item(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        cur.execute(
            """SELECT Students.StudentID,Students.Name,Majors.MajorID,Departments.DeptID
               FROM Students,Majors,Departments
               WHERE
               Students.Name = ? and
               Students.MajorID == Majors.MajorID and
               Students.DeptID == Departments.DeptID""",(name,))                     
        result = cur.fetchall()
        for row in result:
            results.append(row)
            print(f" StudentID: {row[0]:3} Name: {row[1]:15} MajorID: {row[2]:3} DeptID: {row[3]:3}")                
    except sqlite3.Error as err:
        print("Ошибка базы данных",err)
    finally:
        if conn != None:
            conn.close()
            
    return len(results)

if __name__ == "__main__":
  main()
    
 
                                 
 
                                
        
       

    
     
 

        
 
  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

