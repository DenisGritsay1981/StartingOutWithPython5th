import tkinter

class GUI:
    def __init__(self):
        
        self.main_window = tkinter.Tk()
        self.one_frame = tkinter.Frame(self.main_window)
        self.two_frame = tkinter.Frame(self.main_window)
        self.value = tkinter.StringVar()
        self.addres_label = tkinter.Label(self.one_frame, 
                                         textvariable=self.value)
        self.addres_label.pack(side="left")
        self.info_button = tkinter.Button(self.two_frame,
                                          text = "Показать инфо",
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.two_frame,
                                          text = "Выйти",
                                          command=self.main_window.destroy)
        self.quit_button.pack(side="left")
        self.info_button.pack(side="left")
        
        self.one_frame.pack()
        self.two_frame.pack()
   
        tkinter.mainloop()

    def convert(self):

        
        miles = "162390,\n Россия,Волгоградская область\n г. Великий Устюг, \nПочта Деда Мороза"
        self.value.set(miles)
          
def main():
    k = GUI()

main()

    
 
                                 
 
                                
        
       

    
     
 

        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

