# This program prints the unique numbers in user's provided list
# Set is used to avoid duplicate entries
mySet = set();
for i in range(8):
    # Add the number to the set
    mySet.add(int(input("Enter your number: "))) 

# Print the unique numbers in the set
print("Unique numbers in your set : ",mySet)
