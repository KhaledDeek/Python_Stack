

class product:
    def __init__(self , name , price , category):
        self.name = name
        self.price = price
        self.category = category
                

    def update_price(self, percent_change, is_increased):
        if is_increased == True: 
            self.price = (self.price * percent_change) + self.price 
            
        else:
            self.price = self.price - (self.price * percent_change)
            
        print(self.price)

    def print_info(self):
        print(self.name , self.price , self.category)


twix = product( "twix" , 4.99 , "chocolate" )
mars = product( "mars" , 4.99 , "chocolate" )
yogurt = product( "yogurt" , 3.99 , "yogurt" )
steak = product("steak" , 49.99 , "meat")
LM = product("L&M" , 25 , "cigarette")
marlboro = product("marlboro" , 26 , "cigarette")

twix.print_info()
twix.update_price(0.1 , is_increased = True)

class store: 
    def __init__(self, name , list_of_products):
        self.name = name
        self.list_of_products = list_of_products

        
    def add_product(self, new_product):
        list_of_products = self.list_of_products
        list_of_products.append(new_product)
        print(list_of_products)
    def sell_product(self, id ):
        for i in range(len(self.list_of_products)):
            i = id 
        self.list_of_products.pop(i)
        print(self.list_of_products)



shini = store("shini", ["mars" , "yogurt" , "L&M"])
shini.add_product("gummies")
shini.add_product("twix")
shini.add_product("steak")
shini.add_product("marlboro")
shini.sell_product(2)
#shini.inflation(0.5)



