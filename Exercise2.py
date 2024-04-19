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
'''



#task3
import time 

class AlarmClock: 
    def __init__(self): # Formats the object to current time and sets alarm attributes to default values
        self.current_time = time.strftime("%H:%M:%S", time.localtime())
        self.alarm_time = None 
        self.alarm_set = False  
    
    def set_alarm(self, alarm_time): #Sets/stores the alarm time
        self.alarm_time = alarm_time
        self.alarm_set = True 

    def check_time(self): #checks the time 24/7 and triggers when alarm time and current time matches
        while True: 
            current_time = time.strftime("%H:%M:%S", time.localtime()) #current time
            print("Current time:", current_time) #keeps printing out current time

            #The alarm time you set hits current time == Alarm clock hits.   
            if self.alarm_set and current_time == self.alarm_time: 
                print("WAKEY WAKEY! ITS TIME TO GO TO WORK!")
                break

def main():
    alarm_clock = AlarmClock()
    alarm_time = input("Set the alarm time (format HH:MM:SS): ")
    alarm_clock.set_alarm(alarm_time)
    alarm_clock.check_time()

if __name__ == "__main__":
    main()


