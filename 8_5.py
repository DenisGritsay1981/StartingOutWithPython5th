
def main():

    morze = ['2abc', '3def', '4ghi', '5jkl',
             '6mno', '7pqrs', '8tuv', '9wxyz']

    print("Введите 10 символьный номер в формате ХХХ-ХХХ-ХХХХ")
    x = input().lower().split("-")

    x2 = []
    
    for word in x:
        for w in word:
            if w.isalpha():
                index = morze.index([i for i in morze if w in i][0])
                x2.append(str(morze[index].index(w) + 1))
            else:
                x2.append(w)
                
    print(x2)
    result = ''.join(x2)
    print(result)


                    
                    
                
             
            
if __name__ == "__main__":
  main()

                            
 
                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

