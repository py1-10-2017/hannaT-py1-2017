class Car(object):
    def __init__(self, price, speed, fuel, milage, tax=.12):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        self.tax = tax
    
    def display_all(self):
        print self.price 
        print str(self.speed) + 'mph'
        print self.fuel 
        print str(self.milage) + 'mph'
        print self.tax 

    def calc_tax(self):
        if self.price > 10000:
            self.tax = .15
        return self
a = Car(2000, 35, 'Full', 15)
b = Car(2000, 5, 'Not Full', 105)
c = Car(2000, 15, 'Kind of Full', 95)
d = Car(2000, 25, 'Full', 25)
e = Car(2000, 45, 'empty', 25)
f = Car(20000000, 35, 'empty', 15)

a.calc_tax().display_all()
b.calc_tax().display_all()
c.calc_tax().display_all()
d.calc_tax().display_all()
e.calc_tax().display_all()
f.calc_tax().display_all()





