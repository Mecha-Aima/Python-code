# Get the number of characters in the string
str1 = "Hello, World"
print("number of characters in str1 : ", len(str1))
str1 = "Parallel Arrays"       #Double quotes are used to encompass strings containing single quotes
str2 = 'big O notation'

# Check if the string ends with a specific substring
print("Does str1 ends with 'rays' ? ", str1.endswith("rays"))

# Check if a string starts with a specific substring
print("Does str2 starts with 'Big'? ", str2.startswith("big"))

# Count the number of times a character appears in a string
print("Number of times letter 'a' is repeated in str1 : ", str1.count('a'))

# Returns the string with the first character capitalized
print("str2 capitalized : ", str2.capitalize())

# Find the index of the first occurrence of a substring
print("index of 'Arrays' in str1 : ", str1.find("Arrays"))

# Replace a substring with another string
print("Replacing 'Arrays' with 'Processing', str1 is : ", str1.replace("Arrays", "Processing"))
