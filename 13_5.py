import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        
        self.mainwindow = tkinter.Tk()
        self.mainwindow.title("Налог на недвижимость")
        
        self.oneframe = tkinter.Frame(self.mainwindow)
        self.twoframe = tkinter.Frame(self.mainwindow)
        self.threeframe = tkinter.Frame(self.mainwindow)
        self.fourframe = tkinter.Frame(self.mainwindow)
         

        self.price_label=tkinter.Label(self.oneframe,text="Введите цену недвижимости: ")
        self.price_entry=tkinter.Entry(self.oneframe,width=10)
        self.price_label.pack(side="left")
        self.price_entry.pack(side="left")

        self.estimation_label=tkinter.Label(self.twoframe,
                                            text="Оценочная цена недвижимости: ")
        self.estimation = tkinter.StringVar()
        self.e_label=tkinter.Label(self.twoframe,textvariable=self.estimation)
        self.estimation_label.pack(side="left")
        self.e_label.pack(side="left")

        self.nalog_label=tkinter.Label(self.threeframe,
                                            text="Налог: ")
        self.nalog = tkinter.StringVar()
        self.n_label=tkinter.Label(self.threeframe,textvariable=self.nalog)
        self.nalog_label.pack(side="left")
        self.n_label.pack(side="left")

        self.calc_button = tkinter.Button(self.fourframe,
                                          text="Посчитать",
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.fourframe,
                                          text="Выйти",
                                          command=self.mainwindow.destroy)
                                          
       
    
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
       
        self.oneframe.pack()
        self.twoframe.pack()
        self.threeframe.pack()
        self.fourframe.pack()
   
        tkinter.mainloop()

    def convert(self):

        self.v = float(self.price_entry.get())
        self.value = self.v*0.6
        self.estimation.set(self.value)
        x = self.value//100 
        self.nalog.set(x*0.75)
        
          
def main():
    k = GUI()

main() 

    
 
                                 
 
                                
        
       

    
     
 

        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

