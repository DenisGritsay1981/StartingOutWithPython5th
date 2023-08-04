import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        
        self.mainwindow = tkinter.Tk()
        self.mainwindow.title("Показатель экономичности автомобиля")
        
        self.oneframe = tkinter.Frame(self.mainwindow)
        self.twoframe = tkinter.Frame(self.mainwindow)
        self.threeframe = tkinter.Frame(self.mainwindow)
        self.fourframe = tkinter.Frame(self.mainwindow)

        self.miles_label=tkinter.Label(self.oneframe,text="Введите мили: ")
        self.miles_entry=tkinter.Entry(self.oneframe,width=10)
        self.miles_label.pack(side="left")
        self.miles_entry.pack(side="left")

        self.gallon_label=tkinter.Label(self.twoframe,text="Введите галлоны: ")
        self.gallon_entry=tkinter.Entry(self.twoframe,width=10)
        self.gallon_label.pack(side="left")
        self.gallon_entry.pack(side="left")

        self.r_label=tkinter.Label(self.threeframe,text="Экономичность: ")
        self.value = tkinter.StringVar()
        self.result_label=tkinter.Entry(self.threeframe,textvariable=self.value)
        self.r_label.pack(side="left")
        self.result_label.pack(side="left")

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

        self.miles = float(self.miles_entry.get())
        self.gallon = float(self.gallon_entry.get())
        self.itog = self.miles/self.gallon
        self.value.set(self.itog)
          
def main():
    k = GUI()

main()

    
 
                                 
 
                                
        
       

    
     
 

        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

