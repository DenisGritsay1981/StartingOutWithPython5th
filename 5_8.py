def main():

 
    s = float(input(" Введите площадь окрашиваемой поверхности:     "))
    
    value = float(input(" Введите цену 5 литровой емкости краски:     "))

    kol_vo_kraski = k(s)

    print(f"количество емкостей с краской равно {kol_vo_kraski}")

    kol_vo_rabot = r(s)

    print(f"количество часов работы равно {kol_vo_rabot}")

    value_kraski = v(kol_vo_kraski, value)

    print(f"стоимость краски равно  {value_kraski }")

    value_rabot = n(kol_vo_rabot)

    print(f"стоимость работы равно {value_rabot}")

    all_value = b(value_kraski,value_rabot)

    print(f"общая стоимость работ равно {all_value}")

    



def k(s):
    z = (s / 10)
    return z

def r(s):
    t = (8*s)/10
    return t

def v(kol_vo_kraski, value):
     z = kol_vo_kraski * value
     return z

def n(kol_vo_rabot):
    z = 2000*kol_vo_rabot
    return z


def b(value_kraski,value_rabot):
    z = value_kraski + value_rabot
    return z



    

    
 

    






    

    

 

    


    
    









    
 
    

    

    



    
   
