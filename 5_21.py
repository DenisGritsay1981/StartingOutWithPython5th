import random
r = 1
while r == 1:
    x = random.randint(1,4)
   
    print("Введите камень, ножницы или бумага")
    y = input("")
    
    if y == "камень":
        q = 1
    elif  y == "ножницы":
        q = 2
    else:
        q = 3

    if x == 1:
        print("компьютер выбрал:   камень")
    elif x == 2:
        print("компьютер выбрал:   ножницы")
    else:
        print("компьютер выбрал:   бумага")

    
    if x == 1 and q == 2:
        print ("победил компьютер")
    elif x == 2 and q == 1:
        print ("победил игрок")
    elif x == 2 and q == 3:
        print ("победил игрок")
    elif x == 3 and q == 2:
        print ("победил компьютер")
    elif x == 3 and q == 1:
        print  ("победил компьютер")
    elif x == 1 and q == 3:
        print ("победил игрок")
    else:
        r = 1
        print("Повторите выбор")
        
        
    
       
    
    

    

    

    




    

    
    

     

        
    
    

   
    





    
    
    

 





    
    


    
    


    
    
    
    


    
    




    

    
 

    






    

    

 

    


    
    









    
 
    

    

    



    
   
