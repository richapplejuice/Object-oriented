import random

'''
#task1
print("Hello")

#☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#

#task2
def get_user_numbers(): #function asking user to place numbers
    numbers = [] #creates a list
    print("Please enter 10 numbers, one at a time:")
    for _ in range(10): #creates a loop 10x
        num = float(input()) 
        numbers.append(num) #adds to a number list
    return numbers #returns user the list

def get_user_strings():
    strings = [] 
    print("Please enter 10 strings, one at a time:")
    for _ in range(10): 
        string = input()
        strings.append(string) 
    return strings

user_numbers = get_user_numbers()
print("User numbers:", user_numbers)

user_strings = get_user_strings()
print("User strings:", user_strings)

random_numbers = [random.randint(1, 100) for _ in range(10)]
print("Random numbers:", random_numbers)

#☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#

#task3
sorted_user_numbers = sorted(user_numbers)
print("Sorted user numbers: ", sorted_user_numbers)

sorted_user_strings = sorted(user_strings, key=str.lower) #calculates everything in lowercase
print("Sorted user strings: ", sorted_user_strings)

#☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#



#task4

def read_integers():
    integers = []
    while True:
        num = int(input("Enter an number (enter 0 to stop): "))
        if num == 0:
            break
        integers.append(num)
    return integers

# Counts the amount of negative integers
def count_negative_integers(integers):
    count = 0
    for num in integers:
        if num < 0:
            count += 1
    return count


def main():
    numbers = read_integers()
    negative_count = count_negative_integers(numbers)
    print("Number of negative integers:", negative_count)


main()

#☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#



#task5 & task6

def count_even_integers():
    count = 0
    while True: 
        num = int(input("Enter even integers, 0 to exit: "))
        if num == 0: 
            break
        if num % 2 == 0:
            count += 1
    print("Amount of even integers", count)

        
def count_positive_integers():
    total = 0
    while True:


        num = int(input("Integers divisible by 3 adds up, 0 to exit: "))
        if num == 0:
            break
        if num > 0 and num % 3 == 0:
            total += num
    
    print("Sum of positive numbers divisible by three:", total)

count_even_integers()
count_positive_integers()

#☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#
 
'''

#task8
import random

def players_choice():
    while True:
        player_choice = input("Rock, Paper or Scissors?: ").lower()
        if player_choice in ['rock', 'paper', 'scissors']:
            return player_choice
        else:
            print("Invalid choice")

def npcs_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def winner(player_choice, npc_choice):
    if player_choice == npc_choice:
        return "IT'S A TIE. "
    elif(player_choice == 'rock' and npc_choice == 'scissors') or \
        (player_choice == 'paper' and npc_choice == 'rock') or \
        (player_choice == 'scissors' and npc_choice == 'paper'):
        return "YOU WIN."
    else: 
        return "NPC WINS."
    
def game():
    player_wins = 0
    npc_wins = 0

    while player_wins < 3 and npc_wins < 3:
        player_choice = players_choice()
        npc_choice = npcs_choice()
        print("You chose:", player_choice)
        print("NPC chose:", npc_choice)

        result = winner(player_choice, npc_choice)
        print(result)

        if result == "YOU WIN.":
            player_wins += 1
        elif result == "NPC WINS.":
            npc_wins += 1
        
        print("Your Wins:", player_wins)
        print("NPC wins:", npc_wins)
        print("⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒")
    
    if player_wins == 3:
        print("Congratulations, you win the game")
    else:
        print("NPC wins the game")

game() 
