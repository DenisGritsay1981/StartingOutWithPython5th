
def main():

    q = open("students_solution.txt","r")

    right = []

    value = q.readline()

    while value != "":
        value = value.rstrip("\n")
        right.append(value)
        value = q.readline()

    print(right)

    final = []

    for i in range(20):
        x = input(f"Введите итоговую оценку за {i+1} урок из 20-ти ")
        final.append(x)

    s = 0

    for q in range(20):
        if right[q] == final [q]:
            s +=1

    print(f"количество правильных ответов было:  {s}")
    print(f"количество неправильных ответов было:  {20-s}")

    if s >= 15:
        print("Экзамен сдан")
    else:
        print("Экзамен не сдан")

    for u in range(20):
        if right[u] != final [u]:
            print(f"Ответ на вопрос {u}  был не верен")

if __name__ == "__main__":
  main()


                            

                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

