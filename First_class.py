class Animal:
    species = "unknown"
    
    def __init__(self, name):
        self.name = name
        
    def sound(self):
        raise NotImplementedError("Subclass must implement abstract method")
        
class Dog(Animal):
    species = "canine"
    
    def sound(self):
        return "Woof!"
        
class Cat(Animal):
    species = "feline"
    
    def sound(self):
        return "Meow!"
        
class Cow(Animal):
    species = "bovine"
    
    def sound(self):
        return "Moo!"
        
dog = Dog("Buddy")
cat = Cat("Smokey")
cow = Cow("Bessie")

animals = [dog, cat, cow]

for animal in animals:
    print("{} the {} says '{}'".format(animal.name, animal.species, animal.sound()))
