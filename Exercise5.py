class Mammal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def move(self):
        print(f"{self.name} is moving.")


class Prey:
    def __init__(self, type):
        self.type = type


class Cat(Mammal):
    def __init__(self, name, age, gender, breed, is_friendly, prey_type):
        super().__init__(name, age, gender)
        self.breed = breed
        self.is_friendly = is_friendly
        self.prey = Prey(prey_type)

    def meow(self):
        print(f"{self.name} says Meow!")


class Dog(Mammal):
    def __init__(self, name, age, gender, breed, is_friendly, prey_type):
        super().__init__(name, age, gender)
        self.breed = breed
        self.is_friendly = is_friendly
        self.prey = Prey(prey_type)

    def bark(self):
        print(f"{self.name} barks!")


class Elephant(Mammal):
    def __init__(self, name, age, gender, chunk_size, weight, prey_type):
        super().__init__(name, age, gender)
        self.chunk_size = chunk_size
        self.weight = weight
        self.prey = Prey(prey_type)

    def trumpet(self):
        print(f"{self.name} trumpets!")


cat = Cat("Whiskers", 3, "Female", "Bombay cat", True, "Mouse")
dog = Dog("Rover", 5, "Male", "Golden Retriever", True, "Rabbit")
elephant = Elephant("Dumbo", 10, "Male", "Large", 1200, "Grass")

cat.eat()
cat.sleep()
cat.move()
cat.meow()
print(f"{cat.name} hunts {cat.prey.type}")

dog.eat()
dog.bark()
print(f"{dog.name} hunts {dog.prey.type}")

elephant.move()
elephant.trumpet()
print(f"{elephant.name} eats {elephant.prey.type}")
