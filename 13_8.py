import tkinter

class H:
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window,width=500,height=500)

        self.canvas.create_rectangle(200,200,400,400,outline="black",fill="green")
        self.canvas.create_rectangle(230,230,280,280,outline="black",fill="yellow")
        self.canvas.create_rectangle(290,230,330,280,outline="black",fill="yellow")
        self.canvas.create_rectangle(340,230,380,400,outline="black",fill="blue")
        self.canvas.create_arc(0,0,400,400,start=0,extent=45,fill="red")

        self.canvas.create_oval(50,50,150,150,fill="yellow")
        self.canvas.create_line(100,100,199,199,width=3,fill="yellow",dash=(30,10))
        self.canvas.create_line(100,100,300,100,width=3,fill="yellow",dash=(30,10))
        self.canvas.create_line(100,100,100,300,width=3,fill="yellow",dash=(30,10))

        self.canvas.create_oval(80,30,40,60,fill="blue")
        self.canvas.create_oval(120,30,300,120,fill="blue")
        

        
        
      
        
        

        self.canvas.pack()
         
        tkinter.mainloop()
     
      
def main():
    s = H()
 
main()

    
 
                                 
 
                                
        
       

    
     
 

        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

