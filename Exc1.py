#task1
print("Hello")

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




