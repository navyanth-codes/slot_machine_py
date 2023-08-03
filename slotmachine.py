import random

# Text based slot machine project

MAX_LINES =3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}
symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2,
}
def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings =winnings+ values[symbol]*bet
            winning_lines.append(line + 1 )
    return winnings,winning_lines
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():     #symbol.items()   for this we gets both keys and values from the dictionary
        for _ in range(symbol_count):              #we use _ for annanymous values
            all_symbols.append(symbol)
    
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:] #copy 
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    #all values of columns are rows so we have to flip them (transpose of amtrix)
    for row in range(len(columns[0])):
        #print only first values of the three lists
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
              print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()


def deposit(): #deposit from the user.
    while True:
        amount=input("What would you like to deposit ? $ :")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("please enter the number ")
    return amount

def get_number_of_lines():
    while True:
        lines=input("Enter the number of Lines: to bet on (1=" +str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
              print("please enter the number ")
    return lines
    
def get_bet():
    while True:
        amount=input("What would you like to bet on each line ? $ :")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <=MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please enter the number ")
    return amount

def spin(balance):
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet> balance:
            print(f"you dont have enough to bet , your current balance is ${balance}")
        else:
            break
    print("you are betting ${bet}on {lines}lines.Total bet is eqaul to :${total_bet}")

    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines=check_winnings(slots,lines,bet,symbol_value)
    print(f"you won {winnings}")
    print(f"you won on lines : ", *winning_lines) 
    return winnings-total_bet    

def main():
    balance=deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("press enter to play (q to Quit)")
        if answer =="q":
            break
        balance = balance+spin(balance)
    
    print(f"you left with ${balance}")
main()
