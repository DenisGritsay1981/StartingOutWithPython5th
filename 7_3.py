

def main():

    year = ["январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"]

    rain = []
    all_rain = 0
    for x in year:
        z = int(input("введите осадки за {}" .format(x)))
        rain.append(z)
        all_rain += z

    print(rain)
    print(f"суммарное количество осадков за год равно {all_rain}")
    print(f"среднее количество осадков за год равно {all_rain/12}")

    c = min(rain)
    if c in rain:
        item_index = rain.index(c)
        print(item_index)
        print(f"Минимальные осадки в   -   {year[item_index]}")
        
    v = max(rain)
    if v in rain:
        item_index = rain.index(v)
        print(item_index)
        print(f"Максимальные осадки в   -   {year[item_index]}")
        
            

   

    
        


        
if __name__ == "__main__":
  main()


                            

                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

