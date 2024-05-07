#Exercise 4

#Task 1

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