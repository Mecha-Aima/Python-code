#NEEDS IMPROVEMENT
"""
Adventure Game

This is a simple text-based adventure game. The user is presented with a series of choices, and the outcome of the game depends on their decisions.

Example:
    >>> game()
    Type your name: John
    Welcome John to this adventure!
    You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? left
    You've come to a river. You can either walk around it or swim across it. Type 'walk' to walk around and 'swim' to swim across. walk
    You walked for several miles, ran out of water and died.
"""
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?").lower()
if answer == "left":
    answer == input("You've come to a river. You can either walk around it or swim across it. Type 'walk' to walk around and 'swim' to swim across.").lower()

    if answer == "walk":
        print("You walked for several miles, ran out of water and died.")
    elif answer == "swim":
        print("You swam across and were eaten by an alligator.")

    else: 
        print("Not a valid option. You lose!")

elif answer == "right":
    answer = input("You've come across a bridge. It looks wobbly. Do you want to cross it or head back?").lower()

    if answer == "back":
        print("You walk back to the main road. You lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them 'yes' or 'no'? ").lower()

        if answer == "yes":
            print("You talk to the stranger. They give you gold. You win!")
        elif answer == "no":
            print("You ignored the stranger and they are offended. You lose.")

    else:
        print("Not a valid option. You lose!")

else:
    print("Not a valid option. You lose!")