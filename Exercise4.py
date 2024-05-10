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
"""
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
"""

#Task 4
"""
class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year

class GameWarehouse:
    def __init__(self):
        self.__games = []

    def add_game(self, game: ComputerGame):
        self.__games.append(game)

    def list_games(self):
        return self.__games
    
class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def list_games(self):
        museum_games = []
        for game in self._GameWarehouse__games:
            if game.year < 1990:
                museum_games.append(game)
        return museum_games
    
museum = GameMuseum()
museum.add_game(ComputerGame("Pacman", "Namco", 1980))
museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))
for game in museum.list_games():
    print(game.name)
"""


#Task 5
'''
class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name)
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")

class SecretMagicPotion(MagicPotion):
    def __init__(self, name, password):
        super().__init__(name)
        self.password = password

    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if password == self.password:
            super().add_ingredient(ingredient, amount)
        else:
            raise ValueError("Wrong Password!")
        
    def print_recipe(self, password: str):
        if password == self.password:
            super().print_recipe()
        else:
            raise ValueError("Wrong Password!")

diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
diminuendo.print_recipe("hocuspocus")
diminuendo.print_recipe("pocushocus") 
'''

#Task 6
#part-1
import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

def roll_dice(dice_list):
    return [dice.roll() for dice in dice_list]

def play_game(dice_list):
    rolls = []
    for _ in range(2): 
        rolls.append(roll_dice(dice_list))

    player1_sum = sum(rolls[0])
    player2_sum = sum(rolls[1])

    print("Player 1 rolls:", rolls[0], "- Sum:", player1_sum)
    print("Player 2 rolls:", rolls[1], "- Sum:", player2_sum)

    if player1_sum > player2_sum:
        print("Player 1 wins!")
    elif player2_sum > player1_sum:
        print("Player 2 wins!")
    else:
        print("It's a tie! Roll again.")

#part-2
def main():
    num_dice = int(input("Enter the number of dice you want to use: "))
    dice_list = [Dice() for _ in range(num_dice)]
    print("Lets play dice with", num_dice, "dice!")
    play_game(dice_list)

if __name__ == "__main__":
    main()


'''
dice1 = Dice()
dice2 = Dice()
dice3 = Dice()
dice_list = [dice1, dice2, dice3]

print("Let's play dice!")
play_game(dice_list)
'''