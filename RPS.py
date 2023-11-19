import numpy as np
count = 0
comp_choice = ''


def computer_choice():
    comp = np.random.randint(1, 100)
    global comp_choice
    if comp < 33:
        comp_choice = 'R'
    elif 33 < count < 66:
        comp_choice = 'P'
    else:
        comp_choice = 'S'


def versus():
    global comp_choice, my_choice
    if my_choice == comp_choice:
        print("Draw!")
    elif my_choice == 'R' and comp_choice == 'P':
        print("Paper wins!")
    elif my_choice == 'R' and comp_choice == 'S':
        print("Rock wins!")
    elif my_choice == 'P' and comp_choice == 'S':
        print("Scissors wins!")


print("--------------------------------Welcome to a game of Rock, Paper, Scissors!----------------------------------")
print("                                     Your choices are: R, P, S")
while count < 3:
    my_choice = input("Enter choice: ")
    if my_choice != 'R' and my_choice != 'P' and my_choice != 'S':
        print("Invalid choice!")
        continue

    computer_choice()
    print(f"Computer chose: {comp_choice}")
    versus()

    count += 1
else:
    print("The game is over")


