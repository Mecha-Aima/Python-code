import random                               
# 3 by 3 slot machine

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# the loop below is gonna iterate through this dictionary collecting key_value pairs
symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,    # multiplier
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        # if lines=1, check first line. If lines=2, check top 2 lines. If lines=3, check all 3 lines
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:   # this else belongs to the current for
            winnings += values[symbol] * bet        # values here is the passed dictionary containing the multipliers
            winning_lines.append(line + 1)      # line is an index

    return winnings, winning_lines      # POOF! double returns!


def get_slot_machine_spin(rows, cols, symbols):
    # a list that will contain every possible resulting symbol
    all_symbols = []
    # run through the passed dictionary
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):   # _ is an anonymous variable only meant for counting purposes
            all_symbols.append(symbol)  # the symbol read from the dictionary should be added to list. 
                                        # number of additions should be equal to the symbol's respective count
    columns = []  # nested lists. Each element list represents a column
    for _ in range(cols):
        column = []    # generating columns equal to COLS
        current_symbols = all_symbols[:]    # place a ':' so that lvalue doesn't copy the object(mirror changes) of the rvalue. Making a copy so that items are not removed from the original list when next iteration is run.
        for _ in range(rows):   # creating a single column
            value = random.choice(current_symbols)
            current_symbols.remove(value)   # value  is removed so that it is not repeated within the same column
            column.append(value)
        
        columns.append(column)  
    
    return columns # return the nested list


def print_slot_machine(columns):
    # the columns are actually lists but we want their elemnets to be printed out vertically just like in a real slot machine.
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):   # enumerate returns index as well as item
            if i != len(columns) - 1:   # so that the last column isn't followed by a pipe
                print(column[row], end=" | ")   # tells the print function what to end the line with
            else:
                print(column[row], end="")
        print()     # empty print. Brings us down to the new line.
    # we loop through every single row we have. For every single row we loop through every column. For every column, we only print the current row that we are on.
        

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():    # is amount a number?
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a positive number.")
    return amount


def get_num_of_lines():     
    while True:
        lines = input("Enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():    
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():    
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a positive number.")
    return amount

def spin(balance):
    lines  = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough to bet that amount. Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winning_lines)     # '*' is called the unpack operator. It is going to pass every single line from winning_lines to the print function
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press ENTER to play. (q to quit): ")
        if answer == "q":
            break
        else:
            balance += spin(balance)

    print(f"You left with ${balance}")

main()