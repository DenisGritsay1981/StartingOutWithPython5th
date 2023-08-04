class RetailItem:
    def __init__(self, descr, units, price):
        self.__descr=descr
        self.__units=units
        self.__price=price
        
    def set_descr(self, descr):
        self.__descr=descr
        
    def set_units(self, units):
        self.__units
        
    def set_price(self, price):
        self.__price 
        
    def show_descr(self):
        return self.__descr
    
    def show_units(self):
        return self.__units 
    
    def show_price(self):
        return self.__price 
    
    def __str__(self):
        return "Description: " + self.__descr+ \
            "\nUnits in Inventory: " + str(self.__units) + \
            "\nPrice: $" + str(self.__price)

class CashRegister:
    def __init__(self):
       
        self.__cart=[]
    
    def purchase_item(self, item):
        
        cart_descriptions=[]
        for retail_item in self.__cart:
            cart_descriptions.append(retail_item.show_descr())
        
        
        if item.show_descr() not in cart_descriptions:
            self.__cart.append(item)
            
        
        else:
            for i in range(len(self.__cart)):
                if item.show_descr()==self.__cart[i].show_descr():
                    self.__cart[i].set_units(self.__cart[i].show_units()+item.show_units())
                    self.__cart[i].set_price(self.__cart[i].show_price()+ item.show_price())
    
    def get_total(self):
        total=0
        for item in self.__cart:
            total+=item.show_price()
            return format(total, ",.2f")
           
    def show_items(self):
        print("Your cart")
        for item in self.__cart:
            print(item)
            print("---------------")        
    
    def clear(self):
        
        self.__cart=[]

def main():

    cart=CashRegister()
    name=input("Enter the description of the item or q to quit: ")
    while name.lower()!="q":
    
        quantity=int(input("Enter the quantity you'd like to buy: "))
        price_per_unit=float(input("Enter the price for 1 of the item: "))
        price=quantity*price_per_unit
    
    
        item=RetailItem(name, quantity, price)
        cart.purchase_item(item)
    
    
        name=input("Enter the description of the item or 'q' to quit: ")
    

    print()
    cart.show_items()
    print("Your total: $", cart.get_total(), sep="")

    
if __name__ == "__main__":
  main()
 
        
        
    

        

    
    






    

    

