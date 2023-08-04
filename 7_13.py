import random

def main():

    
    z = open ("8_ball_responses.txt","r")

    ball = [str(a.rstrip()) for a in z]

    z.close()

   

    repeat = True

    while repeat:
        w = len(ball)
        answer = random.randrange(w)
        print(ball[answer])
        r = input(f"введите д если повторить ответ:  ")
        if r.lower() != "д":
            repeat = False

    
        

    
    


        
        

                    
if __name__ == "__main__":
  main()


                            

                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

