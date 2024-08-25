# String splicing allows us to extract a subset of characters from a string.
# The format is string[start:stop:step], where start is the index of the first character,
# stop is the index of the last character, and step is the increment between characters.

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[0:10])  # From index 0 to index 10 (exclusive)
print(alphabet[0:10:1])  # Same as above, but with a step of 1
print(alphabet[0:10:2])  # From index 0 to index 10 (exclusive), with a step of 2

print("Number of characters in string = ",len(alphabet))
