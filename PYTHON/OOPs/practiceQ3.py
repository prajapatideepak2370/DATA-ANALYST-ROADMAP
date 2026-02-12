class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    
    def showDetails(self):
        print(self.item, "=", "Rs.",self.price)
     

    def __gt__(self, ord2):
        return self.price > ord2.price 
            

od1 = Order("Pen", 23)
od1.showDetails()

od2 = Order("Book", 13)
od2.showDetails()
print(od1 < od2)