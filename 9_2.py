import random

def main():

    states = ["Алабама", "Аляска", "Аризона", "Арканзас", "Калифорния",
              "Колорадо", "Коннектикут", "Делавер", "Флорида", "Джорджия",
              "Гавайи", "Айдахо",
              "Иллинойс", "Индиана", "Айова", "Канзас",
              "Кентукки", "Луизиана", "Мэн", "Мэриленд",
              "Массачусетс", "Мичиган", "Миннесота", "Миссисипи",
              "Миссури", "Монтана", "Небраска", "Невада", "Нью-Гэмпшир",
              "Нью-Джерси", "Нью-Мексико", "Нью-Йорк", "Северная Каролина",
              "Северная Дакота", "Огайо", "Оклахома", "Орегон",
              "Пенсильвания", "Род-Айленд", "Южная Каролина",
              "Южная Дакота", "Теннесси", "Техас", "Юта", "Вермонт",
              "Виргиния", "Вашингтон", "Западная Виргиния", "Висконсин",
              "Вайоминг"]

    capitals = ["Монтгомери", "Джуно", "Феникс", "Литл Рок", "Сакраменто",
                "Денвер", "Хартфорд", "Дувр", "Таллахасси",
                "Атланта", "Гонолулу", "Боайсе", "Спрингфилд",
                "Индианаполис", "Де-Мойн", "Топика", "Франкфорт",
                "Батон-Руж", "Огаста", "Аннаполис", "Бостон", "Лансинг",
                "Сент-Пол", "Джексон", "Джефферсон-Сити", "Хелена",
                "Линколн", "Карсон Сити", "Конкорд", "Трентон", "Санта-Фе",
                "Албани", "Рали", "Бисмарк", "Колумбус", "Оклахома Сити",
                "Салем", "Харрисбург", "Провиденс", "Колумбия", "Пьер",
                "Нашвилл", "Остин", "Солть-Лейк-Сити", "Монтпилиер",
                "Ричмонд", "Олимпия", "Чарлстон", "Мэдисон", "Шайенн"]

    states_capitals = s_c(states,capitals)
    

    victorina(states_capitals)


def s_c(states,capitals):
    
    states_capitals = {}
    index = 0

    for x in states:
        states_capitals[x] = capitals[index]
        index += 1

    return states_capitals

def victorina(states_capitals):

    true = 0
    w = "д"

    while w.lower() == "д":
        x = random.choice(list(states_capitals))
        print(f"Штат, выбранный компьютером: {x}")
        z = input("Введите столицу выбранного штата:  ")
        if z == states_capitals [x]:
            print("Вы угадали")
            true += 1
        else:
            print("Вы не угадали")
            
        w = input("Желаете продолжить - д - да/ н - нет")

    print(f"количество правильных ответов {true}")
                
if __name__ == "__main__":
  main()
 
                            
 
                                

                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

