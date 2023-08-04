

def main():

    

    x = (["CS101","CS102","CS103","CS104","CS105"])
    z = (["3004","4501","6755","1244","1411"])
    d = (["Хайнс","Альварадо","Рич","Берк","Ли"])
    y = (["8:00","9:00","10:00","11:00","13:00"])


    tab_1 = slova(x,z)
    tab_2 = slova(x,d)
    tab_3 = slova(x,y)

    print(tab_1)

    print(tab_2)

    print(tab_3)

    choice (tab_1,tab_2,tab_3)
    

def slova(x,z):
    tab1 = {}

    index = 0

    for a in x:
        tab1[a] = z[index]
        index +=1

    return tab1

def choice (tab_1,tab_2,tab_3):

    key = input("Введите номер курса:  ")

    if key in tab_1:
        print(f" Номеру курса {key}, соответствует номер аудитории: {tab_1[key]}")
    if key in tab_2:
        print(f" Номеру курса {key}, соответствует преподователь: {tab_2[key]}")
    if key in tab_3:
        print(f" Номеру курса {key}, соответствует время(значение): {tab_3[key]}")
    else:
        print(f"Ключа {key} не существует")
    
    
if __name__ == "__main__":
  main()
 
                            
 
                                

                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

