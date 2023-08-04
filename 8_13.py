
def main():

    ammount = 10
    w = open ("pbnumbers.txt","r")

    x = w.readlines()

    z = [a.rstrip("\n") for a in x]

    print(z)

    w.close()

    for x in range (1,27):
        PowerBall (x,z)

    print()

    for t in range(1,70):
        Ball(t,z)

    print()

    rare_numbers = Ball_10min (z,ammount)
    print("10 самых редких чисел")
    for number in rare_numbers:
        print(number)

    common_numbers = Ball_10max (z,ammount)
    print("10 самых частых чисел")
    for number in common_numbers:
        print(number)
    
       
def PowerBall(d,z):  # 1 аргумент - число, кот нужно искать 2 список

    j = 0
    for s in z:
        q = s.split(" ")
        last_number = int(q[-1])
        if last_number == d:
            j += 1
    print(f"число {d} встречается в PowerBall {j} раз")

def Ball(p,z):  # 1 аргумент - число, кот нужно искать 2 список

    j = 0
    for s in z:
        q = s.split(" ")
        Number = int(q[-2])
        if Number == p:
            j += 1
        Number = int(q[-3])
        if Number == p:
            j += 1
        Number = int(q[-4])
        if Number == p:
            j += 1
        Number = int(q[-5])
        if Number == p:
            j += 1
        Number = int(q[-6])
        if Number == p:
            j += 1
            
    print(f"число {p} встречается в Ball {j} раз")
    
def Ball_10min (z,ammount):  

    j = {}
    p = 0

    for s in z:
        q = s.split(" ")
        for i in range(-1,-7,-1):
            number = int(q[i])
            p += 1
            j [number] = j.get(number,0)+1
    sorted_numbers = sorted(j.keys(),key=lambda x: j[x])
    return sorted_numbers[:ammount]
    
def Ball_10max (z,ammount):  

    j = {}
    p = 0

    for s in z:
        q = s.split(" ")
        for i in range(-1,-7,-1):
            number = int(q[i])
            p += 1
            j [number] = j.get(number,0)+1
    sorted_numbers = sorted(j.keys(),key=lambda x: j[x],reverse=True)
    return sorted_numbers[:ammount]
            
if __name__ == "__main__":
  main()
 
                            
 
                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

