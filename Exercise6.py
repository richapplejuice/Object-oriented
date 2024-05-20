class Prey:
    def being_hunted(self):
        print("Prey: I am being hunted.")

class Habitat:
    def resting(self):
        print("Habitat: The mammal is resting.")

class Mammal:
    def __init__(self):
        self.prey = Prey()
        self.habitat = Habitat()
    
    def hunt(self):
        print("Mammal: I am hunting.")
        self.prey.being_hunted()
    
    def eat(self):
        print("Mammal: I am eating.")
    
    def move_to_rest(self):
        print("Mammal: I am moving to rest.")
        self.habitat.resting()


mammal = Mammal()
mammal.hunt()
mammal.eat()
mammal.move_to_rest()
