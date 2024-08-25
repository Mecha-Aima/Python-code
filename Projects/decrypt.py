def lasso_letter(letter: str, shiftAmount: int) -> str:
    """
    Shift a letter by a certain amount in the alphabet.

    Args:
        letter (str): The letter to be shifted. This should be a single character.
        shiftAmount (int): The amount to shift the letter. This can be positive or negative.

    Returns:
        str: The letter after it has been shifted.
    """
    letter_code = ord(letter.lower())
    alphabet_size = 26
    a_ascii = ord('a')
    decoded_letter_code = a_ascii + (((letter_code - a_ascii) + shiftAmount) % alphabet_size)
    decoded_letter = chr(decoded_letter_code)
    return decoded_letter

def lasso_word(word: str, shiftAmount: int) -> str:
    """
    Shift a word by a certain amount in the alphabet.

    Args:
        word (str): The word to be shifted. This should be a string of letters.
        shiftAmount (int): The amount to shift the word. This can be positive or negative.

    Returns:
        str: The word after it has been shifted.
    """
    decoded_word = ""
    #Iterate thought every letter in the word
    for letter in word:
        decoded_word += lasso_letter(letter, shiftAmount)
    return decoded_word


print('Shifting Ncevy by 13 gives ' + lasso_word('Ncevy', 13))
print('Shifting gpvsui by 25 gives ' + lasso_word('gpvsui', 25))
print('Shifting ugflgkg by -18 gives ' + lasso_word('ugflgkg', -18))
print('Shifting wjmmf by -1 gives ' + lasso_word('wjmmf', -1))