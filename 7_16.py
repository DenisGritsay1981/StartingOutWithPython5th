import matplotlib.pyplot as plt

def main():

    z = open ("coffee.txt","r")
    n = []
    k = []
    name = z.readline()
    

    while name != "":
        name = name.rstrip()
        n.append(name)
        kolvo = float(z.readline().strip())
        k.append(kolvo)
        name = z.readline()

    z.close()

    print(n)
    print(k)


    plt.pie(k, labels = n)

    plt.show()


   
                  
if __name__ == "__main__":
  main()


                            

                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

