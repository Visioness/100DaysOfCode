import random

rps = (
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
)

user = int(input("'0' for Rock, '1' for Paper, '2' for Scissors\n"))
if user > -1 and user < 3:
    print("\nUser: \n", rps[user])
    computer = random.choice((0, 1, 2))
    print("\nComputer: \n", rps[computer])
    if computer == 2 and user == 0:
        print("You won!")
    elif computer == 0 and user == 2:
        print("You lost!")
    elif computer > user:
        print("You lost!")
    elif computer < user:
        print("You won!")
    else:
        print("Draw!")
else:
    print("Wrong usage!")
