import numpy as np
count = 0
comp_choice = ''

winner = int

my_points = 0
comp_points = 0


def computer_choice():
    comp = np.random.rand()
    global comp_choice
    if 0 <= comp < 1/3:
        comp_choice = 'R'
    elif 1/3 <= comp < 2/3:
        comp_choice = 'P'
    else:
        comp_choice = 'S'


def versus():
    global comp_choice, my_choice
    if my_choice == comp_choice:
        print("Fighting fire with fire")
    elif (my_choice == 'R' and comp_choice == 'P') or (my_choice == 'P' and comp_choice == 'R'):
        print("Paper covers Rock!")
    elif (my_choice == 'R' and comp_choice == 'S') or (my_choice == 'S' and comp_choice == 'R'):
        print("Rock crushes Scissors")
    elif (my_choice == 'P' and comp_choice == 'S') or (my_choice == 'S' and comp_choice == 'P'):
        print("Scissors cuts Paper")


def round_winner():
    global count, comp_choice, my_choice, winner
    winner = int  # 1 = USER, 2 = PYTHON
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
    else:
        print(f"Round {count} winner: Draw!")
        print()


def ulimate_winner():
    global winner,my_points, comp_points,count
    if winner == 1:
        my_points += 1
        comp_points += 0
    elif winner == 2:
        my_points += 0
        comp_points += 1
    else:
        my_points += 0
        comp_points += 0

    '''print("my points:",my_points)
    print("comp:",comp_points)
    print()'''




print("--------------------------------Welcome to a game of Rock, Paper, Scissors!----------------------------------")
print("                                     Your choices are: R, P, S")
while count < 3:
    computer_choice()
    my_choice = input("Enter choice: ")
    if my_choice != 'R' and my_choice != 'P' and my_choice != 'S':
        print("Invalid choice!")
        print()
        continue

    print(f"Computer chose: {comp_choice}")
    versus()
    count += 1
    round_winner()
    ulimate_winner()

    if count == 2 and (my_points == 2 or comp_points == 2):
        if my_points == 2:
            print("YOU WIN!")
        else:
            print("YOU LOSE!")
        break

    if count == 3:
        if my_points == comp_points:
            print("DRAW")
        elif my_points > comp_points:
            print("YOU WON THE GAME!!")
        elif my_points < comp_points:
            print("YOU LOST THE GAME!")
