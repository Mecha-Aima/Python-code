
"""
Demonstrates the usage of dictionaries in Python

This script creates a dictionary, updates it, and prints its contents.
"""
MyDiction = {
    "computer" : "a processing machine",
    "RAM" : "primary storage",
    "cookies" : "dessert",
    "logo" : "visual brand identity"

}

MyDiction.update({"pi" : "constant"})
MyDiction.update({"cookies" : "delicious"}) 

print(MyDiction)
print("The value of key 'cookies' is", MyDiction['cookies'])

"""
Iterates over the dictionary and prints each key-value pair

Args:
    MyDiction (dict): The dictionary to be iterated

Returns:
    None
"""
for a,b in MyDiction.items(): #stores the keys in a and the values in b
    print(a,":",b)

print(MyDiction.keys())
# using a for loop helps list the items in a line by line manner
"""
Iterates over the dictionary keys and prints each key

Args:
    MyDiction (dict): The dictionary to be iterated

Returns:
    None
"""
for key in MyDiction.keys():
   print(key)



  