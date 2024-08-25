"""
Spam Detector

This script checks if an email contains spam words.

"""
# List of spam words to check for
SpamWords = ['buy this','subscribe to this','click here','make a lot of money']     #words are case-sensitive
spam = False

email = input("Enter your email: ").lower() #will convert all string characters to lowercase

if('buy this' in email):
    spam = True
if('click here' in email):
    spam = True
if('subscribe to this' in email):
    spam = True
if('make a lot of money' in email):
    spam = True

print("Spam is :",spam)