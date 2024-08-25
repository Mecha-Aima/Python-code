class Participant:
    """
    A class representing a participant in a game of Rock-Paper-Scissors-Lizard-Spock.

    Attributes:
        name (str): The name of the participant.
        points (int): The number of points the participant has.
        choice (str): The participant's current choice (rock, paper, scissor, lizard, or Spock).

    Methods:
        choose(): Asks the participant to select a choice and updates the choice attribute.
        toNumericalChoice(): Converts the participant's choice to a numerical value (0-4).
        incrementPoint(): Increments the participant's points by 1.
    """
    def __init__(self, name):
        """
        Initializes a new Participant object.

        Args:
            name (str): The name of the participant.
        """
        self.name = name
        self.points = 0
        self.choice = ""
    def choose(self):
        """
        Asks the participant to select a choice and updates the choice attribute.
        """
        self.choice = input("{name}, select rock, paper, scissor, lizard or Spock: ".format(name=self.name))
        print("{name} selects {choice}".format(name=self.name, choice=self.choice))
    def toNumericalChoice(self):
        """
        Converts the participant's choice to a numerical value (0-4).

        Returns:
            int: The numerical value of the participant's choice.
        """
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2,
            "lizard": 3,
            "spock": 4
        }
        return switcher[self.choice]
    def incrementPoint(self):
        self.points += 1

class GameRound:
    """
    Represents a single round of a game between two players.

    Attributes:
        rules (list): A 2D list representing the game's rules.
        p1 (Player): The first player.
        p2 (Player): The second player.

    Methods:
        __init__(p1, p2): Initializes the game round with two players.
        compareChoices(p1, p2): Compares the choices of the two players and returns the result.
        awardPoints(): Awards points to the winner (not implemented).
        getResultAsString(result): Converts the result to a string (e.g. "win", "loss", "draw").
    """
    def __init__(self, p1, p2):
        """
        Initializes the game round with two players.

        Args:
            p1 (Player): The first player.
            p2 (Player): The second player.
        """
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print("Round resulted in a {result}".format(result = self.getResultAsString(result) ))
        if result > 0:
           p1.incrementPoint()
        elif result < 0:
           p2.incrementPoint()

    def compareChoices(self, p1, p2):
        """
        Compares the choices of the two players and returns the result.

        Args:
            p1 (Player): The first player
            p2 (Player): The second player

        Returns:
            int: The result of the comparison (1 if p1 wins, -1 if p2 wins, 0 if it's a draw)
        """
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    def getResultAsString(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]

class Game:
    """
    Represents a game of Rock-Paper-Scissors-Lizard-Spock.

    Attributes:
        endGame (bool): Whether the game has ended.
        participant (Participant): The first participant.
        secondParticipant (Participant): The second participant.
    """

    def __init__(self):
        """
        Initializes a new Game object.
        """
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")

    def start(self):
        """
        Starts the game loop.
        """
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        """
        Checks whether the game has ended and if so prints the final score.
        """
        answer = input("Continue game y/n: ")
        if answer == 'y':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name, p1points= self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        """
        Determines the winner of the game.

        Returns:
            str: The winner of the game.
        """
        resultString = "It's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.secondParticipant.name)
        print(resultString)

game = Game()
game.start()
        