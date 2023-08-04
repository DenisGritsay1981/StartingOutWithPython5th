

def main():

    

    q = open("steps.txt","r")
    line = []

    for x in q:
        amount = float(x)
        line.append(amount)
        

    print(line)

    z = int(input("Введите номер счета:  "))

    

    if z in line:
        print("Номер допустимый")

    else:
        print("Номер не допустимый")     


    
    q.close() 
                
if __name__ == "__main__":
  main()


                            

                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

