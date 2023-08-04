import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        
        self.mainwindow = tkinter.Tk()
        self.mainwindow.title("Переводчик с латинского")
        
        self.oneframe = tkinter.Frame(self.mainwindow)
        self.twoframe = tkinter.Frame(self.mainwindow)
        self.threeframe = tkinter.Frame(self.mainwindow)
        self.fourframe = tkinter.Frame(self.mainwindow)

        self.value = tkinter.StringVar()
        self.wordlabel = tkinter.Label(self.oneframe, 
                                         textvariable=self.value)
        self.wordlabel.pack()


        self.button1 = tkinter.Button(self.twoframe,
                                          text="sinister",
                                          command=lambda: self.convert("Левый"))
        self.button2 = tkinter.Button(self.threeframe,
                                          text="dexter",
                                          command=lambda: self.convert("Правый"))
        self.button3 = tkinter.Button(self.fourframe,
                                          text="medium",
                                          command=lambda: self.convert("Центральный"))
        
        
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
       
        self.oneframe.pack()
        self.twoframe.pack()
        self.threeframe.pack()
        self.fourframe.pack()
   
        tkinter.mainloop()

    def convert(self, translation):
        self.value.set(translation)
          
def main():
    k = GUI()

main()

    
 
                                 
 
                                
        
       

    
     
 

        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

