import sqlite3

MIN_CHOICE = 1
MAX_CHOICE = 8
PRINT_SORT_MIN = 1
PRINT_SORT_MAX = 2
PRINT_CITIES = 3
PRINT_ALL_PEOPLE = 4
PRINT_SRED_PEOPLE = 5
PRINT_CITY_MAX = 6
PRINT_CITY_MIN = 7
EXIT = 8

def main():
    choice = 0
    while choice != EXIT:
        display_menu()
        choice = get_menu_choice()
        if choice == PRINT_SORT_MIN:
            print_sort_min()
        elif choice == PRINT_SORT_MAX:
            print_sort_max()
        elif choice == PRINT_CITIES:
            print_cities()
        elif choice == PRINT_ALL_PEOPLE:
            print_ALL_PEOPLE()
        elif choice == PRINT_SRED_PEOPLE:
            print_SRED_PEOPLE()
        elif choice == PRINT_CITY_MAX:
            print_CITY_MAX()
        elif choice == PRINT_CITY_MIN:
            print_CITY_MIN()
                        
def display_menu():
    print("\n----- Меню ведения учета инструментов-----")
    print("1.Города, по возростанию численности населения")
    print("2.Города, по убыванию численности населения")
    print("3.Города, отсортированные по названию")
    print("4.Общая численность населения всех городов")
    print("5.Средняя численность населения всех городов")
    print("6.Город с наибольшей численностью населения")
    print("7.город с наименьшей численностью населения")
    print("8.Выйти из программы")
    
def get_menu_choice():
    choice = int(input("Введите ваш номер: "))
    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f"Допустимые варианты таковы: {MIN_CHOICE} - {MAX_CHOICE}.")
        choice = int(input("Введите ваш номер: "))
    return choice

def print_sort_min():

    conn = sqlite3.connect("cities.db")
    cur = conn.cursor()
    cur.execute("""SELECT *  FROM Cities ORDER BY Population""")                
    result = cur.fetchall()
    print("Список городов в порядке возрастания населения: ")
    for row in result:
        print(f"{row[0]:3}{row[1]:15}{row[2]:10}")
    conn.close()

def print_sort_max():

    conn = sqlite3.connect("cities.db")
    cur = conn.cursor()
    cur.execute("""SELECT *  FROM Cities ORDER BY Population DESC""")                
    result = cur.fetchall()
    print("Список городов по численности населения в порядке убывания: ")
    for row in result:
        print(f"{row[0]:3}{row[1]:15}{row[2]:10}")
    conn.close()

def print_cities():

    conn = sqlite3.connect("cities.db")
    cur = conn.cursor()
    cur.execute("""SELECT *  FROM Cities ORDER BY CityName""")                
    result = cur.fetchall()
    print("Список городов по названию: ")
    for row in result:
        print(f"{row[0]:3}{row[1]:15}{row[2]:10}")
    conn.close()

def print_ALL_PEOPLE():

    conn = sqlite3.connect("cities.db")
    cur = conn.cursor()
    cur.execute("""SELECT Population FROM Cities""")                
    result = cur.fetchall()
    all_ = 0
    for row in result:
        all_ += int(row[0])

    print(f"Общая численность населения всех городов: {all_:,.2f} ")
    conn.close()

def print_SRED_PEOPLE():

    conn = sqlite3.connect("cities.db")
    cur = conn.cursor()
    cur.execute("""SELECT Population FROM Cities""")                
    result = cur.fetchall()
    all_ = 0
    for row in result:
        all_ += int(row[0])
    sred = all_/len(result)

    print(f"Средняя численность населения всех городов: {sred:,.5f} ")
    conn.close()


def print_CITY_MAX():

    conn = sqlite3.connect("cities.db")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM Cities ORDER BY Population DESC""")                
    result = cur.fetchone()
    print(f"Город с максимальным населением: {result[1]} население равно {result[2]} ")
    conn.close()

def print_CITY_MIN():

    conn = sqlite3.connect("cities.db")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM Cities WHERE Population = (SELECT MIN(Population) FROM CITIES)""")                
    result = cur.fetchone()
    print(f"Город с минимальным населением: {result[1]} население равно {result[2]} ")
    conn.close()
    

    
if __name__ == "__main__":
  main()
    
 
                                 
 
                                
        
       

    
     
 

        
 
  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

