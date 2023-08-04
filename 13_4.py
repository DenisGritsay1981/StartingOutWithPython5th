import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        
        self.mainwindow = tkinter.Tk()
        self.mainwindow.title("Из цельсия в фарингейта")
        
        self.oneframe = tkinter.Frame(self.mainwindow)
        self.twoframe = tkinter.Frame(self.mainwindow)
        self.threeframe = tkinter.Frame(self.mainwindow)
        

        self.c_label=tkinter.Label(self.oneframe,text="Введите градусы цельсия: ")
        self.c_entry=tkinter.Entry(self.oneframe,width=10)
        self.c_label.pack(side="left")
        self.c_entry.pack(side="left")

    
        self.r_label=tkinter.Label(self.twoframe,text="Градусы фарингейта: ")
        self.value = tkinter.StringVar()
        
        self.result_label=tkinter.Label(self.twoframe,textvariable=self.value)
        self.r_label.pack(side="left")
        self.result_label.pack(side="left")

        self.calc_button = tkinter.Button(self.threeframe,
                                          text="Посчитать",
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.threeframe,
                                          text="Выйти",
                                          command=self.mainwindow.destroy)
                                          
       
    
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
       
        self.oneframe.pack()
        self.twoframe.pack()
        self.threeframe.pack()
        
   
        tkinter.mainloop()

    def convert(self):

        self.c_entry = float(self.c_entry.get())
       
        self.v = (((self.c_entry)*9)/5)+32
        self.value.set(self.v)
          
def main():
    k = GUI()

main() 

    
 
                                 
 
                                
        
       

    
     
 

        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

