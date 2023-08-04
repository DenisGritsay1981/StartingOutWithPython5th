
def main():

    
    print("Данная функция определяет, является ли ваш список магическим квадратом Лу Шу")

    d = [[0,0,0],[0,0,0],[0,0,0]]

    for x in range(3):
        for z in range(3):
           c = int(input("Введите число для квадрата"))
           d[x][z] = c

    print(d)

    sums = [sum(d[i]) for i in range(3)] \
           + [sum(d[i][j] for i in range(3)) for j in range(3)] \
           + [sum(d[i][i] for i in range(3))] \
           + [sum(d[i][2-i] for i in range(3))]

    

   
    if len(set(sums)) == 1:
        print("Ваш квадрат - магический квадрат Лу Шу!")
    else:
        print("Ваш квадрат не является магическим квадратом Лу Шу.")

    
    




    

    
              
if __name__ == "__main__":
  main()


                            

                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

