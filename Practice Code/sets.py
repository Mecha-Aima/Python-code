# Sets are unordered collections of unique objects
# Sets are useful for storing data that doesn't repeat itself, like a list of unique numbers
# Sets are mutable, meaning they can change after they are created
# Sets are also iterable, meaning they can be looped through like a list
# Sets are useful for quickly checking if an item is in a collection
# Sets are also useful for quickly combining collections of items

mySet = {1,2,3,20,40,60};   # sets can't have duplicate items
# alternative method to create a set
# s = set(); s.add(value) OR s.add(input())
set2 = {1,2,3,5,8}
mySet.add(80)  # add an item to the set
mySet.add("20")  # add an item to the set

print("Length of set :",len(mySet))  # get the number of items in the set

print("popped element :",mySet.pop())  # remove an item from the set
print("Length after pop :",len(mySet))

mySet.remove(40)  # remove an item from the set
print("Length of set after removing 40 :",len(mySet))

print("Intersection SET :",mySet.intersection(set2))  # get the items that are in both sets




