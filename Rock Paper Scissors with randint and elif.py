import random

winner = '' 
random_choice = random.randint(0,2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
elif random_choice == 2:
    computer_choice = 'scissors'

user_choice = input('rock, paper, scissors ')

if computer_choice == user_choice:
    winner = 'tie'
if computer_choice == 'paper' and user_choice == 'rock':
    winner = 'computer'
if computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'computer'
if computer_choice == "scissors" and user_choice == 'paper':
    winner = 'computer'

else:
    winner = 'user'

if winner == 'tie':
    print('The player and the computer chose the same option. Please play again')
else:
    print('The winner of the game is', winner, 'as the computer chose', computer_choice, 'and the user chose', user_choice)