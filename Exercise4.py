#Exercise 4

#Task 1
"""
from collections import Counter #Importing the Counter class
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list): 
        count = Counter(my_list)
        most_common_item = count.most_common(1)[0][0] #Stores the most common item
        return most_common_item

    @classmethod
    def doubles(cls, my_list):
        count = Counter(my_list)
        num_doubles = sum(1 for item, freq in count.items() if freq >= 2) #Stores a unique items that appear at least twice
        return num_doubles
    
numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))
"""

#Task 2
'''
#Part-1
class Item:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} g)"
    
#Part-2 
"""
class Suitcase:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.__items = [] 
        self.__total_weight = 0
    
    def add_item(self, item):
        if self.__total_weight + item.weight() <= self.__max_weight:
            self.__items.append(item)
            self.__total_weight += item.weight()
"""
#Part-4
class Suitcase:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.__items = []
    
    def add_item(self, item):
        if self.weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)

    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        return sum(item.weight() for item in self.__items)

    def heaviest_item(self):
        if not self.__items:
            return None
        return max(self.__items, key=lambda item: item.weight())
    

    #Part-3
    def __str__(self):
        num_items = len(self.__items)
        if num_items == 0:
            return "0 items (0 g)"
        elif num_items == 1:
            return f"1 item ({self.__total_weight} g)"
        else:
            return f"{num_items} items ({self.__total_weight} g)"
    
    
book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400)
suitcase = Suitcase(1000)
suitcase.add_item(book)
suitcase.add_item(phone)
suitcase.add_item(brick)
print("The suitcase contains the following items:")
suitcase.print_items()
combined_weight = suitcase.weight()
print(f"Combined weight: {combined_weight} g")
'''


#Task 3

class Computer:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed
    
class LaptopComputer(Computer):
    def __init__(self, model, speed, weight):
        super().__init__(model,speed) # Calls the constructor of the parent class
        self.weight = weight
    
    def __str__(self):
        return f"{self.model}, {self.speed} MHz, {self.weight} kg."

laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
print(laptop) 