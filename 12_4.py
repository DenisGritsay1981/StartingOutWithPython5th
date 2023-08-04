

def main():
    
    
    x = [1,2,3,4,5,17,6,9,4,5,7]
    index = len(x)-1
    
    print(f"{z(x,index)}")
    
def z(x,index):

    if index == 0:
        return x[index]
    elif index>0:
        if x[index] > x[index-1]:
            del x[index-1]
            return z(x,index-1)
        else:
            del x[index]
            return z(x,index-1)
            

main()

    
 
                                 
 
                               
        
       

    
     
 

        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

