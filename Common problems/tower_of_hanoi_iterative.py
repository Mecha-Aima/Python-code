
"""
Tower of Hanoi game implementation in Python.

The Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
1) Only one disk can be moved at a time.
2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3) No disk may be placed on top of a smaller disk.

This implementation uses a dictionary to represent the rods, where each key is a rod label ('A', 'B', or 'C') and the value is a list of disks on that rod.
The disks are represented as integers, with the largest disk being 1 and the smallest being the number of disks.

"""
NUMBER_OF_DISKS = 4
number_of_moves = 2 ** NUMBER_OF_DISKS - 1
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}

def make_allowed_move(rod1, rod2):  
    """
    Make a move from rod1 to rod2 if it is allowed according to the Tower of Hanoi rules.

    Args:
        rod1 (str): The source rod.
        rod2 (str): The target rod.

    Returns:
        None
    """  
    forward = False
    if not rods[rod2]:
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True              
    if forward:
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        rods[rod2].append(rods[rod1].pop())
    else:
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())
    
    # display our progress
    print(rods, '\n')

def move(n, source, auxiliary, target):
    """
    Solve the Tower of Hanoi puzzle by moving n disks from the source rod to the target rod using the auxiliary rod.

    Args:
        n (int): The number of disks.
        source (str): The source rod.
        auxiliary (str): The auxiliary rod.
        target (str): The target rod.

    Returns:
        None
    """
    # display starting configuration
    print(rods, '\n')
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        if remainder == 1:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            else:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
        elif remainder == 2:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
            else:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
        elif remainder == 0:
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)

# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')