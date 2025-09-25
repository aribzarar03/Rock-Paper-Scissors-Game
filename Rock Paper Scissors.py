import random

draws = ['Rock', 'Paper', 'Scissors']
player_choice = input("Rock, Paper or Scissors? ")
computer_choice = random.choice(draws)
print('The Computer Chose', computer_choice)

if computer_choice == 'Rock' and player_choice == 'Paper':
    print('Paper of the player wrapped the rock of the computer')
if computer_choice == 'Rock' and player_choice == 'Scissors':
    print('Rock of the computer broke the scissors of the player')
if computer_choice == 'Paper' and player_choice == 'Rock':
    print('Paper of the computer wrapped the rock of the player')
if computer_choice == 'Paper' and player_choice == 'Scissors':
    print('Scissors of the player cut the paper of the computer')
if computer_choice == 'Scissors' and player_choice == 'Paper':
    print('Scissors of the computer cut the paper of the player')
if computer_choice == 'Scissors' and player_choice == 'Rock':
    print('Rock of the player broke the scissors of the computer')
if computer_choice == player_choice:
    print('Ah you guys had to choose the same thing huh!')