class Mammal:
    def __init__(self):
        self.state = "Resting"
    
    def rest(self):
        if self.state == "Resting":
            self.state = "Resting"
            print("The mammal is resting.")
    
    def hunting(self):
        if self.state == "Resting":
            self.state = "Hunting"
            print("The mammal is now hunting.")

    def eating(self):
        if self.state == "Hunting":
            self.state = "Eating"
            print("The mammal is now feasting.")

    def drinking(self):
        if self.state == "Eating":
            self.state = "Drinking"
            print("The mammal found water")
            print("The mammal is drinking water.")

    def sleeping(self):
        if self.state == "Eating":
            self.state = "Sleeping"
            print("The mammal went to sleep.")



mammal = Mammal()
mammal.rest()
mammal.hunting()
mammal.eating()
mammal.drinking()
mammal.sleeping()

