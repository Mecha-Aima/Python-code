# Tuples are an ordered, immutable collection of values. Tuples are declared with parentheses and values are separated by commas
# Tuples are useful for storing collections of values that shouldn't be changed after they are created
# Tuples are also useful for quickly checking if an item is in a collection
# Tuples can be used as a key in a dictionary

tupps = (45,89,70)
# get the index of a value in a tuple
print("Index of 70 in tupps : ",tupps.index(70))

tupps2 = (5,10,15,5,20,5,25)
# get the number of times a value appears in a tuple
print("integer 5 repetions in tupps2 : ",tupps2.count(5))

tupps3 = (1, "Hello")
# get a value by its index from a tuple
print(tupps3[1])
