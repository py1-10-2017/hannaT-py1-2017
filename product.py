class Product(object):
    def __init__(self, price, item_name, weight, brand, status='for sale'):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand= brand
        self.status = status
    
    def displayInfo(self):
        print '$' + str(self.price)
        print self.item_name
        print str(self.weight) + 'oz'
        print self.brand
        print self.status

    def sell(self):
        self.status = 'sold'
        return self
    def add_tax(self, tax):
        self.price += self.price* tax
        return self
    def return_reason(self, reason):
        if reason == "defective":
            self.status = 'defective'
            self.price = 0
        elif reason == 'like new':
            self.status = 'for sale'
        elif reason == 'open box':
            self.status = 'used'
            self.price -= (self.price * .2)
        return self

book = Product(12,'book', 1.2,'new brand' )
book.add_tax(.10).displayInfo()
book.sell().displayInfo()
book.return_reason('open box').displayInfo()
