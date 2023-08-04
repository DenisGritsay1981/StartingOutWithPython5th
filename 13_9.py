import tkinter
import tkinter.font

class H:
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window,width=500,height=500)

        

        self.canvas.create_oval(150,150,350,350,width=5)
        self.canvas.create_oval(130,130,370,370,width=5)
        self.canvas.create_oval(110,110,390,390,width=5)
        self.canvas.create_oval(90,90,410,410,width=5)
        self.canvas.create_oval(70,70,430,430,width=5)

        myfont = tkinter.font.Font(family="Helvetica",size=10,weight="bold")

        self.canvas.create_text(190,190,text="1й год",font=myfont)
        self.canvas.create_text(170,170,text="2й год",font=myfont)
        self.canvas.create_text(150,150,text="3й год",font=myfont)
        self.canvas.create_text(130,130,text="4й год",font=myfont)
        self.canvas.create_text(110,110,text="5й год",font=myfont)
        
        self.canvas.pack()
         
        tkinter.mainloop()
     
      
def main():
    s = H()
 
main()

    
 
                                 
 
                                
        
       

    
     
 

        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

