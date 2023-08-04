
years = int(input("введите количество лет:   "))

fallout_all_years = 0


for x in range (1,years+1):
    fallout_all = 0
    for z in range(1,13):
        
        fallout_month = int(input(f"введите количество мм дождевых осадков в {z} месяце:  "))
        fallout_all = fallout_all + fallout_month
        print(f"количество осадков нарастающим итогом в {x} году равно:  {fallout_all}")
    print(f"количество осадков в {x} году равно:  {fallout_all}")
    fallout_all_years += fallout_all
    print(f"осадки нарастающим итогом за {x} лет равны: {fallout_all_years}")



    
all_month = x*12
print(f"кол-во месяцев:  {all_month}")
print(f"общее количество осадков за все {x} лет равно: {fallout_all_years}")
average_thickness = fallout_all_years//all_month
print(f"средняя толщина слоя осадков в месяц за {x} лет:  {average_thickness} ")


 
    

    

    
        



    
    











              







    
    

 







    

    

