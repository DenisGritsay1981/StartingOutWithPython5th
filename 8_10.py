
def main():

    x = str(input("Введите строковое значение"))
    z = {}

    for d in x:
        if d != " ":
            if d in z:
                z[d] += 1
            else:
                z[d] = 1
    print(z)




    most_frequent_char = ''
    most_frequent_count = 0
    for d, count in z.items():
        if count > most_frequent_count:
            most_frequent_char = d
            most_frequent_count = count

    print(f"максимально {most_frequent_count} раз встречается значение {most_frequent_char}")

    

    
    
if __name__ == "__main__":
  main()

                            
 
                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

