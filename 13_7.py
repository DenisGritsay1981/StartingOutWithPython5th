import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        
        self.mainwindow = tkinter.Tk()
        self.mainwindow.title("Междугородние звонки")
        
        self.oneframe = tkinter.Frame(self.mainwindow)
        self.twoframe = tkinter.Frame(self.mainwindow)
        self.threeframe = tkinter.Frame(self.mainwindow)
        self.fourframe = tkinter.Frame(self.mainwindow)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.oneframe,text="Дневное время с 6:00\n до 17.59 тариф 10 руб\n в минуту",
                                       variable=self.radio_var,value=1)
        self.rb2 = tkinter.Radiobutton(self.oneframe,text="Вечернее время с 18:00\n до 23.59 тариф 12 руб\n в минуту",
                                       variable=self.radio_var,value=2)
        self.rb3 = tkinter.Radiobutton(self.oneframe,text="Не пиковое время с полуночи\n до 05.59 тариф 5 руб\n в минуту",
                                       variable=self.radio_var,value=3)
        
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.price_label=tkinter.Label(self.twoframe,text="Введите количество минут: ")
        self.price_entry=tkinter.Entry(self.twoframe,width=10)
        self.price_label.pack(side="left")
        self.price_entry.pack(side="left")

        self.value = tkinter.StringVar()
        self.price_la=tkinter.Label(self.threeframe,text="Стоимость вызова равна: ")
        self.v = tkinter.Label(self.threeframe,textvariable=self.value)
        self.price_la.pack()
        self.v.pack()
        
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

        self.value.set(0)

        if self.radio_var.get() == 1:
            self.value.set(int(self.price_entry.get())*10)
        if self.radio_var.get() == 2:
            self.value.set(int(self.price_entry.get())*12)
        if self.radio_var.get() == 3:
            self.value.set(int(self.price_entry.get())*5)
        
         
def main():
    k = GUI()

main() 

    
 
                                 
 
                                
        
       

    
     
 

        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

