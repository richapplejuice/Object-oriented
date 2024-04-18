#Task1

'''
a. Pseudocode:
Descrpition of a computer program that uses simple 
english statements to outline the basic logic of the
program to solve a problem or complete a task. even 
non-programmers can understand. Pseudocode saves time and avoids 
problems
    Example:
    # Step 1: Display("Hello world")
    print("Hello world")

b. Programming Algorithm:
Procedure or a formula used for solving a problem. Describes
logically and steps how to achieve what we want. Good
algorithm is effective, clear and easily understandable.
Could be a mathematical pattern, conditional sentences or
other programming structures.

c. Data attribute:
Structure that is used to store a data.
    Example in HTML: 
    <div data-role="header"> 

d. Method:
Associated with a class or object. Defines the behavior or actions
that objects of the class can perform. 

e. Constructor:
Special type of function to create an object. Prepares the 
new object for use, often accepting arguments that the constructor
uses to set required member variables

'''



#task2
import random

class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss_the_coin(self):
        outcome = random.randint(0,4)

        if outcome == 0:
            self.sideup = 'Heads'
        elif outcome == 1:
            self.sideup = 'Coin lands on the table uprigth.'
        elif outcome == 2:
            self.sideup = 'Coin drops on the ground and disappears in a rabbit hole.'
        elif outcome == 3:
            self.sideup = 'coin defies gravity and gets lost on a wormhole in space.'
        else:
            self.sideup ='tails'
        
    
    def get_sideup(self):
        return self.sideup

def main():
    my_coin = Coin()
    print("This side is up:", my_coin.get_sideup())

    print("Tossing the coin...")
    my_coin.toss_the_coin()

    print("Now this side is up:", my_coin.get_sideup())

main()


