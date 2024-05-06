#Execise3

#task 1
'''
a. Encapsulation:
One of the fundamental concepts in OOP. Hides the details from
the outside world, providing some kind of abstraction and prevents
direct access to the state of an object. Helps with controlling &
modifying through class methods. 

b. Client:
In software development clients make requests or call methods on 
objects to perform specific tasks or operations.

c. Data attributes:
Variables that belong to a class or object and hold data 
associated with that class or object. It can store various types of
data such as integers, strings, lists, dictionaries or even objects.

d. Instance:
Refers to specific realization or occurence of a class.
when an object is created based on that class, it is called an
instance of that class. Instance allowmultiple objects with similar 
characteristics to exist independetly, each maintaining its own state 
and behaviour.
'''


#task 3
'''
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros."
    
    def eat_ordinary(self):
        price = 2.95
        if self.balance >= price: # Checks the balance.
            self.balance -= price # "If the balance is enough,
                                  #  reduce the price from the balance"
    
    def eat_luxury(self):
        price = 5.90
        if self.balance >= price:
            self.balance -= price

    def deposit_money(self, amount: float):
        if amount < 0:
            raise ValueError("Amount to deposit cannot be negative")
        else:
            self.balance += amount

    
card = LunchCard(10)
print(card)

card.eat_ordinary()
print(card)

card.eat_luxury()
print(card)

card.deposit_money(200)
print(card)
'''

#task 4
'''
class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points

def passed(submissions: list, lowest_passing: int):
    passed_submissions = [] # list to store passed submissions
    for submission in submissions:
        if submission.points >= lowest_passing:
            passed_submissions.append(submission) # if the submission passes, adds to the list
    return passed_submissions

submissions = [
    ExamSubmission("Alice", 80),
    ExamSubmission("Peikko", 60),
    ExamSubmission("Stitch", 90)
]

lowest_passing_grade = 70
passed_submissions = passed(submissions, lowest_passing_grade)
for submission in passed_submissions:
    print(submission.examinee, submission.points)
'''

#task 5
#part1 
'''
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"Balance {self.balance:.1f}"

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount: #checks if you got the money to cover
            self.balance -= amount #substracts the money if sufficient
            return True 
        else:
            return False
        
card = LunchCard(10)
print(card)
print("Payment successful:", card.subtract_from_balance(8))
print(card)
print("Payment successful:", card.subtract_from_balance(6))
print(card)
'''

#task 6 Part 1 & 2
'''
#part-1
class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} g)"


book = Present("Ta-Nehisi Coates: The Water Dancer", 200)
print("The name of the present:", book.name)
print("The weight of the present:", book.weight)
print("Present:", book)

#part-2
class Box:
    def __init__(self):
        self.presents = []

    def add_present(self, present: Present):
        self.presents.append(present)

    def total_weight(self):
        return sum(present.weight for present in self.presents)


book = Present("Ta-Nehisi Coates: The Water Dancer", 200)
box = Box()
box.add_present(book)
print(box.total_weight())

cd = Present("Pink Floyd: Dark Side of the Moon", 50)
box.add_present(cd)
print(box.total_weight())
'''

#task 7 - Part 1, 2 & 3
#part-1
class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        if self.is_empty():
            print("The room is empty.")
        else:
            total_height = sum(person.height for person in self.persons)
            print(f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm.")
            for person in self.persons:
                print(f"{person.name} ({person.height} cm)")
                
    #Part-2
    def shortest(self):
        if self.is_empty():
            return None
        else:
            shortest_person = min(self.persons, key=lambda person: person.height)
            return shortest_person.name
        

    #Part-3
    def remove_shortest(self):
        if self.is_empty():
            return None
        else:
            shortest_person = min(self.persons, key=lambda person: person.height)
            self.persons.remove(shortest_person)
            return shortest_person

room = Room()
room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Ally", 166))
room.add(Person("Nina", 162))
room.add(Person("Dorothy", 175))
print("Is the room empty?", room.is_empty())  
print("Shortest:", room.shortest())  
print()

removed = room.remove_shortest()
if removed:
    print(f"Removed from room: {removed.name}")
print()

room.print_contents()

