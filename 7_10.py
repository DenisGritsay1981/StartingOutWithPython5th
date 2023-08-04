
def main():

    
    z = open("USpopulation.txt","r")
    z2 = []
   
    z2 = [int(line.strip()) for line in z]
        
    z.close()

    all_pop = sum(z2)

    
    print(f"вся сумма - {all_pop}")
    print(f"количество элементов в списке - {len(z2)}")
    print(f"среднее значение населения за {len(z2)}   лет {all_pop/len(z2):,.2f}")
    zad1(z2)
    
    din = [z2[i+1] - z2[i] for i in range(len(z2)-1)]
    print(f"Динамика населения США: {din}")

    max_index = din.index(max(din))
    max_pop_year = z2[max_index+1]  
    print(f"Год с наибольшим приростом населения: {max_pop_year}")

    min_index = din.index(min(din))
    min_pop_year = z2[min_index+1]  
    print(f"Год с наименьшим приростом населения: {min_pop_year}")



    


  

   
    

def zad1(z2):

    min_ = min(z2)
    max_ = max(z2)

    sred_ = max_ - min_

    print(f"среднегодовое изменение численности равно - {sred_}")

    
              
if __name__ == "__main__":
  main()


                            

                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

