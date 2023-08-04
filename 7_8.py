
def main():

    b = open("boys_names.txt","r")
    g = open("girl_names.txt","r")
    b2 = []
    g2 = []

    value = b.readline()

    while value != "":
        value = value.rstrip("\n")
        b2.append(value)
        value = b.readline()

    v = g.readline()

    while v != "":
        v = v.rstrip("\n")
        g2.append(v)
        v = g.readline()

    g.close()
    b.close()
    
    print(g2)
    print()
    print(b2)

    boy = input("Введите имя мальчика")

    if boy in b2:
        print(f"Имя {boy} входит в список самых популярных имен мальчиков")
    else:
        print("Имя не входит в популярные")

    
    girl = input("Введите имя девочки")

    if girl in g2:
        print(f"Имя {girl} входит в список самых популярных имен девочек")
    else:
        print("Имя не входит в популярные")
    

           
if __name__ == "__main__":
  main()


                            

                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

