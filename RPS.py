import numpy as np
count = 0
comp_choice = ''


def computer_choice():
    comp = np.random.randint(1, 100)
    global comp_choice
    if comp < 33:
        comp_choice = 'R'
    elif comp < 66:
        comp_choice = 'P'
    else:
        comp_choice = 'S'


def versus():
    global comp_choice, my_choice
    if my_choice == comp_choice:
        print("Draw!")
        print()
    elif my_choice == 'R' and comp_choice == 'P':
        print("Paper covers Rock!")
    elif my_choice == 'R' and comp_choice == 'S':
        print("Rock crushes Scissors")
    elif my_choice == 'P' and comp_choice == 'S':
        print("Scissors cuts Paper")

def round_winner():
    global count, comp_choice, my_choice
    winner = int  # USER
    if my_choice == comp_choice:
        winner = 0
    elif my_choice == 'R' and comp_choice == 'P':
        winner = 2
    elif my_choice == 'R' and comp_choice == 'S':
        winner = 1
    if my_choice == 'P' and comp_choice == 'S':
        winner = 2
    elif my_choice == 'P' and comp_choice == 'R':
        winner = 1
    if my_choice == 'S' and comp_choice == 'R':
        winner = 2
    elif my_choice == 'S' and comp_choice == 'P':
        winner = 1

    if winner == 1:
        print(f"Round {count} winner: You!")
        print()
    elif winner == 2:
        print(f"Round {count} winner: Python!")
        print()



print("--------------------------------Welcome to a game of Rock, Paper, Scissors!----------------------------------")
print("                                     Your choices are: R, P, S")
while count < 3:
    my_choice = input("Enter choice: ")
    if my_choice != 'R' and my_choice != 'P' and my_choice != 'S':
        print("Invalid choice!")
        print()
        continue

    computer_choice()
    print(f"Computer chose: {comp_choice}")
    versus()
    count += 1
    round_winner()


else:
    print("The game is over")


