

def main():
    
    encrypt={'А':'?','B':'@','C':'#','D':'$','E':'%','F':'^','G':'&','H':'*','I':'(',
             'J':')','K':'-','L':'_','M':'+','N':'=','O':'`','P':'~','Q':'{','R':'[',
             'S':'}','T':']','U':':','V':';','W':'"','X':'<','Y':'>','Z':'0','a':'1',
             'b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'a',
             'k':'b','l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'j',
             't':'k','u':'l','v':'m','w':'n','x':'o','y':'p','z':'q'}

    textfile=open("plaintext.txt", "w")


    for x in encrypt:
        textfile.write(x + encrypt[x] + '\n')

    textfile.close()
                   
if __name__ == "__main__":
  main()
 
                            
 
                                

                               
        
       

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

