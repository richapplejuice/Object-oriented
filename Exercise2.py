#Task 1
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


#task 2
'''
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


#task 3
'''
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
'''


#Task 4
'''
def factorials(n:int) -> dict: 
    factorial_dict = {} #creates empty dictionary to store factorial results.
    
    #loop throug numbers from 1 to n(maximum)
    for i in range(1, n + 1):
        factorial = 1   #Initialize facotrial value to 1 for each number
                        
                        #multiplies factorial numbers from 1 to i
        for j in range(1, i + 1):
            factorial *=j
        factorial_dict[i] = factorial #stores resulet in dictionary 

    return factorial_dict

k = factorials(5)
print(k[1])
print(k[3])
print(k[5]) # 1 * 1 * 2 * 3 * 4 * 5
'''



#task5
'''
def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    
    person1_avg = (person1['result1'] + person1['result2'] + person1['result3']) / 3
    person2_avg = (person2['result1'] + person2['result2'] + person2['result3']) / 3
    person3_avg = (person3['result1'] + person3['result2'] + person3['result3']) / 3

    smallest_avg = min(person1_avg, person2_avg, person3_avg)

    if smallest_avg == person1_avg:
        return person1
    elif smallest_avg == person2_avg:
        return person2
    else:
        return person3
    
person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

print(smallest_average(person1, person2, person3))
'''


#task 6
from datetime import date

def list_years(dates:list) -> list:
    years = [d.year for d in dates]
    sorted_years = sorted(years)
    return sorted_years

date1 = date(2019, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)

years = list_years([date1, date2, date3])
print(years)