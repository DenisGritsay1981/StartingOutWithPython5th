

def main():
    
    
    
    # read the file
    myfile=open("cities.txt", "r")
    # read the lines
    lines=myfile.readlines()
    # close the file
    myfile.close()
    
    # create a set of words
    unique_words=set()
    
    # read each word.
    for line in lines:      # each line
        print(line.split())
        for word in line.split():   # each word: split words by space (a.k.a. word)
            unique_words.add(word)  # add the word to set
            
    # remember. Set does not have duplicate items. So you can just iterate
    # unique_words.add(word) without checking >>>> if word is not in unique_words. etc.
    
    print("Unique words are below: ")
    print(unique_words)
    

                   
if __name__ == "__main__":
  main()
 
                            
 
                                

                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

