
def main():

    print("Напишите предложение без пробелов но каждое слово с большой буквы")
    sentence = input("")
    words = []
    i = 0
    while i < len(sentence):
        if i == 0:
            word = sentence[i]
        elif sentence[i].isupper():
            words.append(word)
            word = sentence[i]
        else:
            word += sentence[i]
        i += 1
    words.append(word)
    result = " ".join(words).capitalize()
    print(result) 
    
    
   
if __name__ == "__main__":
  main()

                            
 
                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

