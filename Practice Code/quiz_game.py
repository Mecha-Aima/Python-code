def play():
    """
    Plays the computer quiz game.

    Asks the user a series of questions about computer hardware and keeps track of the score.

    Returns:
        int: The user's score out of 5.
    """
    print("Okay! Let's play :) ")
    score = 0

    answer = input("What does CPU stand for? ")
    if answer == "Central Processing Unit".lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does GPU stand for? ")
    if answer == "Graphics Processing Unit".lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does RAM stand for? ")
    if answer == "Random Access Memory".lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        
    answer = input("What does PSU stand for? ")
    if answer == "Power Supply Unit".lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does HDD stand for? ")
    if answer == "Hard Disk Drive".lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    
    return score

def main():
    """
    The main function of the program.

    Welcomes the user to the computer quiz and asks if they want to play.
    If they do, it calls the play function and prints the user's score.

    Returns:
        None   
    """
    print("Welcome to my Computer Quiz!")

    playing = input("Do you want to play? ")

    if playing != "yes".lower():
        quit() #terminate program

    score = play()
    print("You got " + str(score) + "/5 questions correct.")
    print("You got " + str((score/4)*100) + "%.")

# call main function if this file is run directly (not if it is imported)
if __name__ == "__main__":
    main()

