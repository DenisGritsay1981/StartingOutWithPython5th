import sqlite3

MIN_CHOICE = 1
MAX_CHOICE = 4

CREATE_TAB = 1
READ_TAB = 2
DELETE_TAB = 3
EXIT = 4

def main():
    choice = 0
    while choice != EXIT:
        display_menu()
        choice = get_menu_choice()
        if choice == CREATE_TAB:
            create_tab()
        elif choice == READ_TAB:
            read_tab()
        elif choice == DELETE_TAB:
            delete_tab()       
        
        
def display_menu():
    print("\n----- Меню ведения учета инструментов-----")
    print("1.Создать таблицы")
    print("2.Читать таблицы")
    print("3.Удалить таблицы")
    print("4.Выйти из программы")
    
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

def create_tab():
    MIN_CHOICE = 1
    MAX_CHOICE = 3
    print("\n----- Выберете, какую из трех таблиц хотите СОЗДАТЬ-----")
    print("1.Majors")
    print("2.Departments")
    print("3.Students")
    choice = None
    while choice is None:
        try:
            choice = int(input("Введите ваш номер: "))
            if choice < MIN_CHOICE or choice > MAX_CHOICE:
                print(f"Допустимые варианты таковы: {MIN_CHOICE} - {MAX_CHOICE}.")
                choice = None
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
    if choice == 1:
        create_majors()
    elif choice == 2:
        create_departments()
    elif choice == 3:
        create_students()
        
def create_majors():
    
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Majors (MajorID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT)""")                
        conn.commit()
        conn.close()
        print("Таблица Majors со столбцами MajorID и Name создана")
    except sqlite3.Error as e:
        print("Ошибка при создании таблицы Majors: ", e)
    
def create_departments():

    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Departments (DeptID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT)""")                
        conn.commit()
        conn.close()
        print("Таблица Departments со столбцами DeptID и Name создана")
    except sqlite3.Error as e:
        print("Ошибка при создании таблицы Departments: ", e)
        
def create_students():

    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Students (StudentsID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    MajorID INTEGER,
                    DeptID INTEGER,
                    FOREIGN KEY(MajorID) REFERENCES Majors(MajorID),
                    FOREIGN KEY(DeptID) REFERENCES Departments(DeptID))""")                
        conn.commit()
        conn.close()
        print("Таблица Students со столбцами StudentsID, Name, MajorID, DeptID создана")
    except sqlite3.Error as e:
        print("Ошибка при создании таблицы Students: ", e)

def read_tab():
    MIN_CHOICE = 1
    MAX_CHOICE = 3
    print("\n----- Выберете, какую из трех таблиц хотите ПРОЧИТАТЬ-----")
    print("1.Majors")
    print("2.Departments")
    print("3.Students")
    choice = None
    while choice is None:
        try:
            choice = int(input("Введите ваш номер: "))
            if choice < MIN_CHOICE or choice > MAX_CHOICE:
                print(f"Допустимые варианты таковы: {MIN_CHOICE} - {MAX_CHOICE}.")
                choice = None
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
    if choice == 1:
        read_majors()
    elif choice == 2:
        read_departments()
    elif choice == 3:
        read_students()

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

def read_students():
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
            print(f"  Name: {row[0]:10} MajorID: {row[1]:5} DeptID: {row[2]:5}")
        conn.close()
    except sqlite3.Error as e:
        print("Ошибка при чтении таблицы Students: ", e)

def delete_tab():

    MIN_CHOICE = 1
    MAX_CHOICE = 3
    print("\n----- Выберете, какую из трех таблиц хотите УДАЛИТЬ-----")
    print("1.Majors")
    print("2.Departments")
    print("3.Students")
    choice = None
    while choice is None:
        try:
            choice = int(input("Введите ваш номер: "))
            if choice < MIN_CHOICE or choice > MAX_CHOICE:
                print(f"Допустимые варианты таковы: {MIN_CHOICE} - {MAX_CHOICE}.")
                choice = None
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
    if choice == 1:
        delete_majors()
    elif choice == 2:
        delete_departments()
    elif choice == 3:
        delete_students()

def delete_majors():
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("""DROP TABLE IF EXISTS Majors""")                
        conn.commit()
        conn.close()
        print("Таблица Majors удалена")
    except sqlite3.Error as e:
        print("Ошибка удаления таблицы Majors: ", e)
        
def delete_departments():
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("""DROP TABLE IF EXISTS Departments""")                
        conn.commit()
        conn.close()
        print("Таблица Departments удалена")
    except sqlite3.Error as e:
        print("Ошибка удаления таблицы Departments: ", e)

def delete_students():
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute("""DROP TABLE IF EXISTS Students""")                
        conn.commit()
        conn.close()
        print("Таблица Students удалена")
    except sqlite3.Error as e:
        print("Ошибка удаления таблицы Students: ", e)


if __name__ == "__main__":
  main()
    
 
                                 
 
                                
        
       

    
     
 

        
 
  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

