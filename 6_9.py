

def main():

  try:

    x = open("number_list.txt","r")
  
    q = 0
    z = 0
    for line in x:
      q += int(line)
      z += 1

    w = q/z
   
 
    print(f"сумма {q} ")
    print(f"количество {z} ")
    print(f"среднее {w} ")

    x.close()

  except IOError:
    print("Ошибка IOError ")

  except ValueError:
    print("Ошибка ValueError ")

  except:
    print("Ошибка")
    
  

if __name__ == "__main__":
  main()




 
      

  


 
  

            
        

    
    
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

