import pickle

def main():

    print("Введите цифру, что хотите сделать")
    print("1 - записать новый файл")
    print("2 - добавить новые данные в файл")
    print("3 - изменить существующие имя и почту")
    print("4 - удалить существующие имя и почту")
    print("5 - вывести на печать данные")
    
    z = int(input())

    if z == 1:
        new()
    elif z == 5:
        pechat()
    elif z == 2:
        add()

def add():

    x = open("name_email.dat","rb")
    emails = pickle.load(x)
    x.close()
    print(emails)
    
    print("Хотите добавить новое имя и адрес электронной почты? Д да Н нет")
    q = input("    ")
    
    if q.lower() == "д":
        while q.lower() == "д":
            name = input("Введите имя")
            if name.lower() not in emails:
                emails[name.lower()] = input("Введите почту")
            else:
                print("почта уже есть")
            print("Хотите добавить новое имя и адрес электронной почты? Д да Н нет")
            q = input("    ")
        

        z = open("name_email.dat","wb")
        pickle.dump (emails,z)
        z.close()

def pechat():

    input_file = open("name_email.dat","rb")
    while True:
        try:
            data = pickle.load(input_file)
            print("Имя:", data["name"])
            print ("Почта:", data["mail"])
        except EOFError:
            break

    input_file.close()
                   
def new():

    print("Введите имя и адрес почты")

    q = "д"
    output_file = open("name_email.dat","wb")
    

    while q.lower() == "д":
        spis = {}
        spis["name"] = input("Введите имя")
        spis["mail"] = input("Введите почту")
        pickle.dump(spis,output_file)
        q = input("Введите д если хотите повторить, н если не хотите")

    output_file.close()
    print("Данные записаны в файл")

        
    


    
            

   
    

    

    



        
        

    

    

                
  
            
            
            
            
            

    
    

    

    

        





    
    
  
    

                
    
    
                          
if __name__ == "__main__":
  main()
 
                            
 
                                

                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

