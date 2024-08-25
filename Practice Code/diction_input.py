"""
Urdu-English Dictionary

A simple dictionary that translates Urdu words to English.

"""

def main():
    """
    Main function to interact with the Urdu-English dictionary.

    Returns:
        None
    """
    myDictionary = {
        "pani" : "water",
        "roshni" : "luminance",
        "kaam" : "work",
        "ghar" : "home"
    }
    """
    Note: The dictionary has duplicate key "roshni" which is not allowed in Python dictionaries.
          The last value for the key "roshni" will be retained, which is "luminance" in this case.
    """
    key = input("Enter an urdu word:")
    """
    Get user input for the Urdu word to translate.
    """
    if(myDictionary.get(key) == None):
        """
        Check if the Urdu word is present in the dictionary.
        """
        print("Value not found.\n")
    else:
        """
        Print the English translation of the Urdu word.
        """
        print("Meaning of the word",key,":",myDictionary.get(key))

if __name__ == "__main__":
    main()