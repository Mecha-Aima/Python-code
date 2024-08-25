import random
"""
    Play a guessing game with the user.
"""
top_of_range = input("Type a number: ")
# Asks the user to input a number and validates the input.

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than zero next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

# Generate a random number in range (0-top_of_range)
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    # Validate input
    if user_guess.isdigit():
        user_guess = int(user_guess)    
    else:
        print("Please type a number next time.")
        continue 

    if user_guess == random_number:
        # Correct guess
        print("You got it!")
        break
    elif user_guess > random_number:
        # Provide hints
        print("You were above the number.")
    else:
        print("You were below the number.")

# Display results
print("You got it in", guesses, "guesses")
