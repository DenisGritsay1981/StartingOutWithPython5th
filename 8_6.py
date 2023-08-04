
def main():

    x = open("golf.txt", "r")
    z = x.readlines()
    z = [a.rstrip("\n") for a in z]
    x.close()

   
    lower = 0
    upper = 0
    digit = 0
    space = 0

    for e in z:
        for c in e:
            if c.islower():
                lower += 1
            if c.isupper():
                upper += 1
            if c.isdigit():
                digit += 1
            if c.isspace():
                space += 1

    print(f"нижний регистр - {lower} \
          верхний регистр - {upper} \
          цифры - {digit} \
          подчеркивания {space}")
            
            
    
if __name__ == "__main__":
  main()

                            
 
                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

