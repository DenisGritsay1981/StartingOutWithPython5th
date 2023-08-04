import matplotlib.pyplot as plt

def main():

    z = open ("USpopulation.txt","r")
    n = []
    a = z.readline()

    while a != "":
        a = a.rstrip()
        n.append(a)
        a = z.readline()

    z.close()

    q = [x for x in n]

    plt.plot(n,q)

    plt.title("График вверх")

    plt.xlabel("год")

    plt.ylabel("продажи")

    plt.xticks([1],[1])

    plt.yticks([2],[2])

    plt.grid(True)

    plt.show()



    
   




   
                  
if __name__ == "__main__":
  main()


                            
 
                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

