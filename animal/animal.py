class Animal(object):   
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print self.health

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health += 150
    def pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health += 170
    def fly(self):
        self.health += 10
        return self
    
    def display_health(self):
        super(Dragon,self).display_health()
        print "I am a dragon"

    


animal_1 = Animal('bird', 10)
animal_dog = Dog('mut', 10)
animal_dragon = Dragon('one',15)
new_animal = Animal('cat', 10)

# animal_1.run().display_health()
# animal_1.walk().display_health()
# animal_dog.walk().walk().walk().run().run().pet().display_health()
# animal_dragon.display_health()
new_animal.display_health()

    