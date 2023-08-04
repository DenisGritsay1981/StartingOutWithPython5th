import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        
        self.mainwindow = tkinter.Tk()
        self.mainwindow.title("Авторемонтная фирма Автоцех")
        
        self.oneframe = tkinter.Frame(self.mainwindow)
        self.twoframe = tkinter.Frame(self.mainwindow)
        self.threeframe = tkinter.Frame(self.mainwindow)

        self.cd_var1 = tkinter.IntVar()
        self.cd_var2 = tkinter.IntVar()
        self.cd_var3 = tkinter.IntVar()
        self.cd_var4 = tkinter.IntVar()
        self.cd_var5 = tkinter.IntVar()
        self.cd_var6 = tkinter.IntVar()
        self.cd_var7 = tkinter.IntVar()

        self.cd_var1.set(0)
        self.cd_var2.set(0)
        self.cd_var3.set(0)
        self.cd_var4.set(0)
        self.cd_var5.set(0)
        self.cd_var6.set(0)
        self.cd_var7.set(0)

        self.cd1 = tkinter.Checkbutton(self.oneframe,text="Замена масла 500р.",
                                       variable=self.cd_var1)
        self.cd2 = tkinter.Checkbutton(self.oneframe,text="Смазочные работы 300р.",
                                       variable=self.cd_var2)
        self.cd3 = tkinter.Checkbutton(self.oneframe,text="Промывка радиатора 700р.",
                                       variable=self.cd_var3)
        self.cd4 = tkinter.Checkbutton(self.oneframe,text="Замена жидкости в трансмиссии 1000 руб.",
                                       variable=self.cd_var4)
        self.cd5 = tkinter.Checkbutton(self.oneframe,text="Осмотр 800р.",
                                       variable=self.cd_var5)
        self.cd6 = tkinter.Checkbutton(self.oneframe,text="Замена глушителя выхлопа 1300р.",
                                       variable=self.cd_var6)
        self.cd7 = tkinter.Checkbutton(self.oneframe,text="Перестановка шин 1300 руб.",
                                       variable=self.cd_var7)

        self.cd1.pack()
        self.cd2.pack()
        self.cd3.pack()
        self.cd4.pack()
        self.cd5.pack()
        self.cd6.pack()
        self.cd7.pack()

        self.value = tkinter.StringVar()
        self.v = tkinter.Label(self.twoframe,textvariable=self.value)
        self.v.pack()

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

        self.value.set(0)

        if self.cd_var1.get() == 1:
            self.value.set(int(self.value.get()) + 500)
        if self.cd_var2.get() == 1:
            self.value.set(int(self.value.get()) + 300)
        if self.cd_var3.get() == 1:
            self.value.set(int(self.value.get()) + 700)
        if self.cd_var4.get() == 1:
            self.value.set(int(self.value.get()) + 1000)
        if self.cd_var5.get() == 1:
            self.value.set(int(self.value.get()) + 800)           
        if self.cd_var6.get() == 1:
            self.value.set(int(self.value.get()) + 1300)
        if self.cd_var7.get() == 1:
            self.value.set(int(self.value.get()) + 1300)
         
def main():
    k = GUI()

main() 

    
 
                                 
 
                                
        
       

    
     
 

        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

