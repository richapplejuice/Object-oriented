#Execise3

#task1
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


#task3
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

#task4

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