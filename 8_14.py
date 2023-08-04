
def main():

    
    w = open ("GasPrices.txt","r")

    x = w.readlines()

    data = [a.rstrip("\n") for a in x]

    w.close()
    

    for year in range(1993,2014,1):
        sred_price(data,year)

    sred_month(data)

    for year in range(1993,2014,1):
        min_price_in_year(data,year)

    for year in range(1993,2014,1):
        max_price_in_year(data,year)

def max_price_in_year(data,year):

    max_price = float('-inf')
    

    for row in data:
        elements = row.split(",")
        for item in elements:
            item_year = int(item.split("-")[-1].split(":")[0])
            item_znac = float(item.split(":")[-1])
            if item_year == year and item_znac > max_price:
                max_price = item_znac

    if max_price != float('inf'):
        print(f"Максимальная цена за {year} год: {max_price}")
    else:
        print(f"Данные за {year} год отсутствуют или невозможно найти минимальную цену.")          



        

def min_price_in_year(data,year):

    min_price = float('inf')
    

    for row in data:
        elements = row.split(",")
        for item in elements:
            item_year = int(item.split("-")[-1].split(":")[0])
            item_znac = float(item.split(":")[-1])
            if item_year == year and item_znac < min_price:
                min_price = item_znac

    if min_price != float('inf'):
        print(f"Минимальная цена за {year} год: {min_price}")
    else:
        print(f"Данные за {year} год отсутствуют или невозможно найти минимальную цену.")          
               

                    
def sred_price(data,year):  # средняя цена за год

    count = 0
    total = 0
    
    for row in data:
        elements = row.split(",")
        for item in elements:
            if str(year) in item:
                count += 1
                total += float(item.split(":")[-1])
               
        
    
    final = total/count
    print(f"средняя цена за: {year} год равна: {final:,.2f} ")

def sred_month(data):
    months = set()

    for row in data:
        elements = row.split(",")
        for item in elements:
            month = int(item.split("-")[0])
            months.add(month)
    

    for year in range(1993, 2014, 1):
        for month in months:
            count = 0
            total = 0

            for row in data:
                elements = row.split(",")
                for item in elements:
                    item_year = int(item.split("-")[-1].split(":")[0])
                    item_month = int(item.split("-")[0])
                    if item_year == year and item_month == month:
                        count += 1
                        total += float(item.split(":")[-1])

            if count > 0:
                final = total / count
                print(f"Средняя цена за {month:02d} месяц {year} года равна: {final:,.2f}")
                
    
                               
if __name__ == "__main__":
  main()
  
                            
 
                                

                               
        
    

    
     


        

  

    









    
    
    
    
       

 


 


            
        

    
     
    
    
   

     
   
    
   
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

