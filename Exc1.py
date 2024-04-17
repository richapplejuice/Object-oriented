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



#task5

def count_even_integers():
    count = 0
    while True:
        num = int(input("Enter an number (0 to exit): "))
        if num == 0:
            break
        if num % 2 == 0:
            count += 1
    print("Number of even integers:", count)

count_even_integers()

#☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆#

'''