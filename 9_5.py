
def main():
    
    with open("cities.txt") as myfile:
        lines = myfile.read().splitlines()
    
  
    words = set()
    
    
    spis = {}

    for line in lines:
        for word in line.split():
            words.add(word.lower())

    print(words)
    print(lines)

    for word in words:
        count = 0
        for line in lines:
            if word.lower() == line.strip().lower():
                count += 1
        spis[word] = count

    print(spis)


                
    
    
                          
if __name__ == "__main__":
  main()
 
                            
 
                                

                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

