import tkinter
import tkinter.font

class H:
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window,width=500,height=500)

    
        self.canvas.create_line(200,200,250,100,width=3,fill="green")
        self.canvas.create_line(250,100,300,200,width=3,fill="green")
        
        self.canvas.create_line(100,200,200,200,width=3,fill="green")
        self.canvas.create_line(300,200,400,200,width=3,fill="green")

        self.canvas.create_line(300,250,400,200,width=3,fill="green")
        self.canvas.create_line(100,200,200,250,width=3,fill="green")

        self.canvas.create_line(300,250,350,350,width=3,fill="green")
        self.canvas.create_line(200,250,150,350,width=3,fill="green")

        self.canvas.create_line(250,275,350,350,width=3,fill="green")
        self.canvas.create_line(250,275,150,350,width=3,fill="green")

        
        

        myfont = tkinter.font.Font(family="Helvetica",size=10,weight="bold")

        self.canvas.create_text(250,225,text="Денис",font=myfont,fill="Red")
        
        self.canvas.pack()
         
        tkinter.mainloop()
     
      
def main():
    s = H()
 
main()

    
 
                                 
 
                                
        
       

    
     
 

        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

