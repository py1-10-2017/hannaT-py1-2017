class Bike(object):
    def __init__(self, price, max_speed, miles =0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    
    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        #return self

    def ride(self):
        self.price += 10
        print "Riding {}".format(self.price) + "mph"
        return self
    
    def reverse(self):
        if self.miles - 5 < 0:
            self.miles = 0
            print "Reversing {}".format(self.miles)
        else:
            self.miles -= 5
            print "Reversing {}".format (self.miles)
        return self

bike_1 = Bike(200,20,45)
bike_2 = Bike(250,30,45)
bike_3 = Bike(300,40,45)

bike_1.ride().ride().ride().reverse().displayInfo()
bike_2.ride().ride().reverse().reverse().displayInfo()
bike_3.reverse().reverse().reverse().displayInfo()

