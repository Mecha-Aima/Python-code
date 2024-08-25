import copy
import random

class Hat:
    """
    A class representing a hat containing balls of different colors.

    Attributes:
        colors (dict): A dictionary where keys are color names and values are the number of balls of each color.
        contents (list): A list of balls in the hat, where each ball is represented by its color.

    Methods:
        reset: Resets the hat to its initial state.
        draw: Draws a specified number of balls from the hat.
    """
    def __init__(self, **kwargs):
        """
        Initializes a Hat object with the given color distribution.

        Args:
            **kwargs: A dictionary where keys are color names and values are the number of balls of each color.

        Example:
            hat = Hat(black=6, red=4, green=3)
        """
        self.colors = kwargs
        self.contents = []
        for color in self.colors:
            for _ in range(self.colors[color]):
                self.contents.append(color)

    # Reset the hat before each new draw
    def reset(self):
        """
        Resets the hat to its initial state.

        """
        self.contents = []
        for color, count in self.colors.items():
            self.contents.extend([color] * count)

    def draw(self, quantity):
        """
        Draws a specified number of balls from the hat.

        Args:
            quantity (int): The number of balls to draw.

        Returns:
            list: A list of drawn balls.

        """
        drawn_balls = []
        # Return all balls if quantity exceeds length
        if quantity >= len(self.contents):
            drawn_balls = copy.copy(self.contents)
            self.contents = []
        # Draw balls at random
        else:
            drawn_balls = random.sample(self.contents, quantity)
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Runs an experiment to estimate the probability of drawing a certain distribution of balls.

    Args:
        hat (Hat): The hat object to use for the experiment.
        expected_balls (dict): A dictionary where keys are color names and values are the minimum number of balls of each color to draw.
        num_balls_drawn (int): The total number of balls to draw in each experiment.
        num_experiments (int): The number of experiments to run.

    Returns:
        float: The estimated probability of drawing the expected distribution of balls.

    """
    # To count how many times expected_balls were drawn
    successful_experiments = 0
    for _ in range(num_experiments):
        hat.reset()
        drawn = hat.draw(num_balls_drawn)
        if all(drawn.count(color) >= expected_balls.get(color, 0) for color in expected_balls):
            successful_experiments += 1
    # Return the probability
    return successful_experiments / num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)

hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

